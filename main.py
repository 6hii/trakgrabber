# trakGrab.py
# Daniel Guilbert
# 12.11.19 - 07.08.24
# v1.1

from urllib.request import urlopen, URLError, Request
from bs4 import BeautifulSoup
import re
import os



 # Download music from traktrain short link
import sys

short_url = input("Paste the traktrain link here (e.g.: https://traktra.in/t/xxxx): ").strip()

if not short_url:
    print("No link provided.")
    sys.exit(1)

try:
    req = Request(short_url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36')
    response = urlopen(req)
    real_url = response.geturl()
    html = response.read().decode('utf-8')
except URLError:
    print("Could not access the provided link.")
    sys.exit(1)

print("Connected! Real URL:", real_url)

 # Extract artist name from real URL
import urllib.parse
parsed = urllib.parse.urlparse(real_url)
try:
    artist = parsed.path.strip('/').split('/')[0]
except Exception:
    print("Could not extract artist from URL.")
    sys.exit(1)

urlmatch = re.compile('(.)*var AWS_BASE_URL(.)*')
m = urlmatch.search(html)
if not m:
    print("Could not find AWS_BASE_URL on the page.")
    sys.exit(1)
baseUrl = m.group().split("'")[1]

pwd = os.getcwd() + "\\songs\\" + artist + "\\"
if not os.path.exists(pwd):
    os.makedirs(pwd)

 # Extract src and song name from HTML
try:
    src_match = re.search(r"data-player-info='([^']+)'", html)
    if not src_match:
        raise Exception('data-player-info not found')
    src = src_match.group(1)
    import json
    info = json.loads(src)
    songname = info.get('name', 'track')
    srcstr = info.get('src')
    if not srcstr:
        raise Exception('src not found')
except Exception:
    print("Could not extract song information.")
    sys.exit(1)

songUrl = baseUrl + srcstr
print("Downloading '" + songname + "'")
req = Request(songUrl)
req.add_header('Referer', 'https://traktrain.com/')
songname = re.sub(r'[^\w ]', '', songname)
outfile = open(pwd+songname+".mp3", 'wb')
outfile.write(urlopen(req).read())
outfile.close()

print(f"\nDownload finished! File saved at: {pwd+songname}.mp3")
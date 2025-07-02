# trakGrab

A simple Python script to download songs from Traktrain using a short link (e.g., https://traktra.in/t/xxxx).

## Features
- Downloads a single song from a Traktrain short link.
- Automatically creates a folder for the artist and saves the song as an MP3 file.

## Requirements
- Python 3.x
- The following Python packages (all are standard in most Python installations):
  - urllib
  - re
  - os
  - sys
  - json

## How to Use

1. **Download or clone this repository.**
2. **Open a terminal (Command Prompt or PowerShell on Windows) in the project folder.**
3. **Run the script:**
   
   ```sh
   python main.py
   ```
4. **When prompted, paste the Traktrain short link** (e.g., `https://traktra.in/t/2s847LLB3q`) and press Enter.
5. The script will automatically download the song and save it in the `songs/<artist>/` folder.

## Notes
- The script only works with public Traktrain links that are not protected or expired.
- The downloaded file will be named after the song title, with invalid filename characters removed.
- If you encounter errors, make sure the link is correct and you have an active internet connection.

## Example
```
Cole aqui o link do traktrain (ex: https://traktra.in/t/xxxx): https://traktra.in/t/2s847LLB3q
Conectado! URL real: https://traktrain.com/artist/song-title
Downloading 'Song Title'

Download finalizado! Arquivo salvo em: .../songs/artist/Song Title.mp3
```

---

Created by Daniel Guilbert. Modified for automation and ease of use.

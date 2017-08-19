# Crast
Crast is a simple open-source interface to Chromecast.

In the future I'd like to add:
- Simple controls (play/pause/stop/skip)
- Basic GUI, something like https://airflowapp.com/

Maybe transcoding, but muuuuch later.

# Example

    python3 src/crast.py http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4

Or choose a device:

    python3 src/crast.py --device "Chromecast Bitch" http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4

# Playing local files
Host the files:

    python3 -m http.server

Then tell Chromecast to play the file:

    http://192.168.0.122:8000/video.mp4
    http://192.168.0.122:8000/music.mp3
    http://192.168.0.122:8000/picture.jpg

# Development

    git clone https://github.com/tompreston/crast.git
    cd crast
    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt


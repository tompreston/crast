# Crast
Crast is a simple open-source interface to Chromecast.

In the future I'd like to add:
- ~~Simple controls (play/pause/stop/skip)~~
- Interactive controls (so you don't have to search for chromecasts everytime)
- Feedback, current state, messages, etc
- Basic GUI, something like https://airflowapp.com/

Maybe transcoding, but muuuuch later.

# Play URL

    python3 src/crast.py --url http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4

Or choose a device:

    python3 src/crast.py --device "Chromecast Bitch" -u http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4

# Controls

    python3 src/crast.py -d "Chromecast Bitch" -c play
    python3 src/crast.py -d "Chromecast Bitch" -c pause
    python3 src/crast.py -d "Chromecast Bitch" -c stop
    python3 src/crast.py -d "Chromecast Bitch" -c skip
    python3 src/crast.py -d "Chromecast Bitch" -c rewind

# Playing local files
Host the files:

    python3 -m http.server

Then tell Chromecast to play the file:

    python3 src/crast.py -u http://192.168.0.122:8000/video.mp4
    python3 src/crast.py -u http://192.168.0.122:8000/music.mp3
    python3 src/crast.py -u http://192.168.0.122:8000/picture.jpg

# Development

    git clone https://github.com/tompreston/crast.git
    cd crast
    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt


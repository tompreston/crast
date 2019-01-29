# Crast
Crast is a simple open-source interface to Chromecast.

In the future I'd like to add:
- ~~Simple controls (play/pause/stop/skip)~~
- Interactive controls (so you don't have to search for chromecasts everytime)
- Feedback, current state, messages, etc
- Basic GUI, something like https://airflowapp.com/

Maybe transcoding, but muuuuch later.

Let's get started:

    git clone https://github.com/tompreston/crast.git
    cd crast
    pipenv install -r requirements.txt
    pipenv shell

# Play URL

    python src/crast.py --url http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4

Or choose a device:

    python src/crast.py --device "Living Room TV" -u http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4

# Controls

    python src/crast.py -d "Living Room TV" -c play
    python src/crast.py -d "Living Room TV" -c pause
    python src/crast.py -d "Living Room TV" -c stop
    python src/crast.py -d "Living Room TV" -c skip
    python src/crast.py -d "Living Room TV" -c rewind

# Playing local files
Host the files:

    python -m http.server

Then tell Chromecast to play the file:

    python src/crast.py -u http://192.168.0.122:8000/video.mp4
    python src/crast.py -u http://192.168.0.122:8000/music.mp3
    python src/crast.py -u http://192.168.0.122:8000/picture.jpg

# Development

    git clone https://github.com/tompreston/crast.git
    cd crast
    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt


# Crast
Crast is a simple open-source interface to pychromecast. It aims to make
streaming local (or remote) files to a Chromecast device trivial.

It currently supports:
- Command line interface
- Searching and displaying local Chromecasts
- Playing local and remote URLs
- Basic commands

In the future I'd like to add:
- Interactive controls
    - So you don't have to search for Chromecasts everytime
    - Display feedback, current state, messages, etc
    - Press keys to send commands immediately
- Stream desktop
    - https://trac.ffmpeg.org/wiki/Capture/Desktop
    - https://trac.ffmpeg.org/wiki/StreamingGuide
- Basic GUI
    - Something like https://airflowapp.com/

Let's get started:

    git clone https://github.com/tompreston/crast.git
    cd crast
    make init
    pipenv shell
    python crast.py --help

# Play URL

    python crast.py --device "Living Room TV" --url http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4
    python crast.py -d L -u http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4
    python crast.py -u http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4

# Controls

    python crast.py --device "Living Room TV" --command play
    python crast.py -d "Living Room TV" -c pause
    python crast.py -d L -c stop
    python crast.py -d L -c skip
    python crast.py -d L -c rewind

# Playing local files
Host the files:

    python -m http.server

Then tell Chromecast to play the file:

    python crast.py -u http://192.168.0.122:8000/video.mp4
    python crast.py -u http://192.168.0.122:8000/music.mp3
    python crast.py -u http://192.168.0.122:8000/picture.jpg

# Launch apps

    python crast.py --app-start youtube
    python crast.py -a spotify

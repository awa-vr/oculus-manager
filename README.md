# Oculus Manager
An gui application to manage your oculus quest 2

⚠️ WIP, stuff will break and not everything is working

## To do:
- [x] General
- [x] Performance
    - [x] Style UI
    - [x] cpu level
    - [x] gpu level
    - [x] texture res
    - [x] ffr
    - [x] dynamic ffr
- [ ] Recording
    - [x] UI
    - [x] capture size
    - [ ] presets
    - [x] fps
    - [x] bitrate
- [x] Misc
    - [x] install apk
    - [x] install [oculus killer v2](https://github.com/LibreQuest/OculusKiller)
    - [x] Pause gardian
    - [x] Chromatic aberration
    - [x] Experimental features
- [ ] Settings
    - [ ] remote adb (probably for v1.1)
- [x] Remove adb.exe from repo

## Usage
1. download `main.exe`
2. connect your quest 2
3. run `main.exe`

## Contributing
Please make an issue/pr if you want to see anything added or changed. Feel free to make my code better, I'm new to python.

quest adb commands can be found [here](https://smartglasseshub.com/quest-2-adb-commands/)

## Development
Install the required dependencies

`pip install -r requirements.txt`

### Make exe
0. Install pyinstaller:
`pip install pyinstaller`
1. Get location of customtkinter:
`pip show customtkinter`
2. Run pyinstaller:
`pyinstaller --noconfirm --onefile --windowed --add-data "<CustomTkinter Location>/customtkinter;customtkinter/"  "./main.py"`
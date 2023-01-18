# oculus-manager
An gui application to manage your oculus quest 2

⚠️ WIP, stuff will break and not everything is working

# To do:
- [x] General
- [ ] Performance
    - [ ] Style UI
    - [ ] cpu level
    - [ ] gpu level
    - [ ] texture res
    - [ ] ffr
- [ ] Recording
    - [ ] capture size
    - [ ] presets
    - [ ] fps
    - [ ] bitrate
- [ ] Misc
    - [ ] install apk
    - [ ] install [oculus killer](https://github.com/LibreQuest/OculusKiller)
- [ ] Settings
    - [ ] adb selector
    - [ ] remote adb

# Contributing
Please make an issue/pr if you want to see anything added or changed. Feel free to make my code better, I'm new to python.

quest adb commands can be found [here](https://smartglasseshub.com/quest-2-adb-commands/)

# Development
Install `customtkinter` and `pure-python-adb`

`pip install customtkinter`

`pip install pure-python-adb`

## Make exe
0. Install pyinstaller:
`pip install pyinstaller`
1. Get location of customtkinter:
`pip show customtkinter`
2. Run pyinstaller:
`pyinstaller --noconfirm --onedir --windowed --add-data "<CustomTkinter Location>/customtkinter;customtkinter/"  "./main.py"`
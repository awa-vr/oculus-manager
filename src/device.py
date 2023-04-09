import os
import appdirs
import zipfile
import requests
from ppadb.client import Client as AdbClient

from vars import *

app_name = "Oculus Manager"

# Download platform tools if not installed
if not os.path.exists(appdirs.user_data_dir(app_name)):
    print("download platform tools")
    os.makedirs(appdirs.user_data_dir(app_name))
    url = 'https://dl.google.com/android/repository/platform-tools-latest-windows.zip'
    file = requests.get(url)
    open(f'{appdirs.user_data_dir(app_name)}/platform-tools.zip', 'wb').write(file.content)
    with zipfile.ZipFile(f'{appdirs.user_data_dir(app_name)}/platform-tools.zip', 'r') as zip_ref:
        zip_ref.extractall(f'{appdirs.user_data_dir(app_name)}/platform-tools')

if not debug:
    os.system(f'{appdirs.user_data_dir(app_name)}/platform-tools/platform-tools/adb.exe start-server')
    client = AdbClient(host="127.0.0.1", port=5037)
    devices = client.devices()
    if len(devices) == 0:
        warning = Warning()
        warning.mainloop()
    else:
        device = client.devices()[0]
        adb_connected = True
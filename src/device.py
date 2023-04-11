import os
import sys
import customtkinter
import appdirs
import zipfile
import requests
from ppadb.client import Client as AdbClient

from vars import *
from common import *

app_name = "Oculus-manager"
adb_connected = False

class Warning(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        self.geometry("200x100")
        self.title("Oculus manager - No adb devices")
        self.lbl = customtkinter.CTkLabel(self, text="No adb devices found", font=customtkinter.CTkFont(size=18))
        self.lbl.pack(padx=10, pady=10, fill="both", expand=True)

        self.btn = customtkinter.CTkButton(self, text="Ok", command=self.btn_action)
        self.btn.pack(padx=10, pady=10)
    
    def btn_action(self):
        quit()

# Download platform tools if not installed
if not os.path.exists(appdirs.user_data_dir(app_name)):
    logger.info("Downloading platform tools...")
    os.makedirs(appdirs.user_data_dir(app_name))
    url = 'https://dl.google.com/android/repository/platform-tools-latest-windows.zip'
    logger.debug("Actually downloading platform tools")
    file = requests.get(url)
    open(f'{appdirs.user_data_dir(app_name)}/platform-tools.zip', 'wb').write(file.content)
    logger.info("Unzipping platfrom tools...")
    with zipfile.ZipFile(f'{appdirs.user_data_dir(app_name)}/platform-tools.zip', 'r') as zip_ref:
        zip_ref.extractall(f'{appdirs.user_data_dir(app_name)}/platform-tools')

if not debug:
    logger.info("Starting adb server")
    try:
        os.system(f'{appdirs.user_data_dir(app_name)}/platform-tools/platform-tools/adb.exe start-server')
    except:
        logger.critical("Couldn't start adb server")

    try:
        client = AdbClient(host="127.0.0.1", port=5037)
    except:
        logger.critical("Adb client couldn't connect (try to reconnect)")
        try:
            os.system(f'{appdirs.user_data_dir(app_name)}/platform-tools/platform-tools/adb.exe reconnect')
        except:
            logger.critical("Adb client still couldn't connect, now existing")
            sys.exit()
        
    try:
        devices = client.devices()
    except:
        logger.critical("Couldn't get adb devices, now exiting")
        sys.exit()

    if len(devices) == 0:
        logger.info("No adb devices found")
        warning = Warning()
        warning.mainloop()
    else:
        logger.debug("Devices:" + devices)
        device = client.devices()[0]
        adb_connected = True

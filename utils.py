import os
from ppadb.client import Client as AdbClient
from vars import *

# ---------------------------------------------------------------------------- #
#                                      adb                                     #
# ---------------------------------------------------------------------------- #
os.system(".\\adb.exe start-server")
client = AdbClient(host="127.0.0.1", port=5037)
device = client.device("1WMHHB63D52024") # TODO change this

# ---------------------------------------------------------------------------- #
#                                     other                                    #
# ---------------------------------------------------------------------------- #
def set_brightness(value):
    device.shell("settings put system screen_brightness " + str(int(value)))

def get_refresh() -> str:
    if debug:
        return str(var_refresh) + "Hz"
    else:
        # return os.popen("adb shell getprop debug.oculus.refreshRate").read().strip() + "Hz"
        var: str = device.shell("getprop debug.oculus.refreshRate")
        return var.strip() + "Hz"

def set_refresh_rate(value):
    device.shell("setprop debug.oculus.refreshRate " + value.replace("Hz", ""))

def set_cpu(value): # TODO: Add funtionality
    print("cpu: " + value)

def set_gpu(value): # TODO: Add funtionality
    print("gpu: " + value)

def set_texture(choice): # TODO: Add funtionality
    print("Tex: " + choice)

def set_ffr(choice): # TODO: Add funtionality
    print("FFR: " + choice)

# ---------------------------------------------------------------------------- #
#                                    Battery                                   #
# ---------------------------------------------------------------------------- #
def get_l_bat() -> str:
    if not debug:
        var: str = device.shell("dumpsys OVRRemoteService | grep Battery")
        var = var.strip().split(",")
        lbat = var[8].split(":")[1].strip()[:-1]
        return lbat
    else:
        return str(var_lcon_bat)

def get_r_bat() -> str:
    if not debug:
        # var = os.popen("adb shell \"dumpsys OVRRemoteService | grep Battery\"").read().strip().split(",")
        var: str = device.shell("dumpsys OVRRemoteService | grep Battery")
        var = var.strip().split(",")
        rbat = var[3].split(":")[1].strip()[:-1]
        return rbat
    else:
        return str(var_rcon_bat)

def get_hmd_bat() -> str:
    if not debug:
        var = os.popen("adb shell \"dumpsys CompanionService | grep Battery\"").read().strip()
        # var: str = device.shell("dumpsys OVRRemoteService | grep Battery")
        var = var.strip().split(":")[1].strip()
        hmd_bat = var
        return hmd_bat
    else:
        return str(var_hmd_bat)
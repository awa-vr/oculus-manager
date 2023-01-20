import os
from ppadb.client import Client as AdbClient
from customtkinter import filedialog
from vars import *

# ---------------------------------------------------------------------------- #
#                                      adb                                     #
# ---------------------------------------------------------------------------- #
if not debug:
    os.system(".\\adb.exe start-server")
    client = AdbClient(host="127.0.0.1", port=5037)
    device = client.device("1WMHHB63D52024") # TODO change this to be dynamic

# ---------------------------------------------------------------------------- #
#                                     other                                    #
# ---------------------------------------------------------------------------- #
def install_apk():
    file = filedialog.askopenfilename()
    if vars.debug:
        print(file)
    else:
        device.install(file)

def set_brightness(value):
    if not debug:
        device.shell("settings put system screen_brightness " + str(int(value)))

class RefreshRate:
    def __init__(self):
        pass

    def get():
        if debug:
            return str(var_refresh) + "Hz"
        else:
            var: str = device.shell("getprop debug.oculus.refreshRate")
            return var.strip() + "Hz"

    def set(value):
        if not debug:
            device.shell("setprop debug.oculus.refreshRate " + value.replace("Hz", ""))

def set_cpu(value):
    print(f"setprop debug.oculus.cpuLevel {value}")
    if not debug:
        device.shell(f"setprop debug.oculus.cpuLevel {value}")

def set_gpu(value):
    print(f"setprop debug.oculus.gpuLevel {value}")
    if not debug:
        device.shell(f"setprop debug.oculus.gpuLevel {value}")

tex_w = 1440
tex_h = 1584
def tex_width(eh):
    switch={
        "default": 1440,
        "512": 512,
        "768": 768,
        "1024": 1024,
        "1280": 1280,
        "1440": 1440,
        "1536": 1536,
        "2048": 2048,
        "2560": 2560,
        "3072": 3072
    }
    return switch.get(eh)

def tex_height(eh):
    switch={
        "default": 1584,
        "512": 563,
        "768": 845,
        "1024": 1127,
        "1280": 1408,
        "1440": 1584,
        "1536": 1690,
        "2048": 2253,
        "2560": 2816,
        "3072": 3380
    }
    return switch.get(eh)

def set_texture(choice):
    tex_w = tex_width(choice)
    tex_h = tex_height(choice)
    print(f"setprop debug.oculus.textureWidth {tex_w}")
    print(f"setprop debug.oculus.textureHeight {tex_h}")
    # print(f"settings put system font_scale 0.85 && settings put system font_scale 1.0")
    if not debug:
        device.shell(f"setprop debug.oculus.textureWidth {tex_w}")
        device.shell(f"setprop debug.oculus.textureHeight {tex_h}")
        # device.shell(f"settings put system font_scale 0.85 && settings put system font_scale 1.0")

def switch_ffr(eh):
    switch={
        "off": 0,
        "low": 1,
        "medium": 2,
        "high": 3,
        "max": 4
    }
    return switch.get(eh)
class FFR:
    def __init__(self):
        pass

    def set(choice):
        eh = switch_ffr(choice)
        print(f"debug.oculus.foveation.level {eh}")
        if not debug:
            device.shell(f"debug.oculus.foveation.level {eh}")

# ---------------------------------------------------------------------------- #
#                                     Video                                    #
# ---------------------------------------------------------------------------- #
def set_cs(value):
    print(value)

# ---------------------------------------------------------------------------- #
#                                    Battery                                   #
# ---------------------------------------------------------------------------- #
class Battery:
    def __init__(self):
        pass

    def get_l():
        if not debug:
            var: str = device.shell("dumpsys OVRRemoteService | grep Battery")
            var = var.strip().split(",")
            lbat = var[8].split(":")[1].strip()[:-1]
            return lbat
        else:
            return str(var_lcon_bat)

    def get_r():
        if not debug:
            var: str = device.shell("dumpsys OVRRemoteService | grep Battery")
            var = var.strip().split(",")
            rbat = var[3].split(":")[1].strip()[:-1]
            return rbat
        else:
            return str(var_rcon_bat)

    def get_hmd():
        if not debug:
            var = os.popen("adb shell \"dumpsys CompanionService | grep Battery\"").read().strip() # TODO: Change to use python adb
            # var: str = device.shell("dumpsys OVRRemoteService | grep Battery")
            var = var.strip().split(":")[1].strip()
            hmd_bat = var
            return hmd_bat
        else:
            return str(var_hmd_bat)

# ---------------------------------------------------------------------------- #
#                                 Oculus Killer                                #
# ---------------------------------------------------------------------------- #
def install_killer_v2(): # TODO: Do stuff
    print("Install oculus killer v2")

def install_killer(): # TODO: Do stuff
    print("Install oculus killer")
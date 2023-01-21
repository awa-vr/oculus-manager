import os
import customtkinter
from ppadb.client import Client as AdbClient
from vars import *

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

# ---------------------------------------------------------------------------- #
#                                      adb                                     #
# ---------------------------------------------------------------------------- #
if not debug:
    os.system(".\\adb.exe start-server")
    client = AdbClient(host="127.0.0.1", port=5037)
    devices = client.devices()
    if len(devices) == 0:
        warning = Warning()
        warning.mainloop()
    else:
        device = client.devices()[0]
        adb_connected = True


# ---------------------------------------------------------------------------- #
#                                     other                                    #
# ---------------------------------------------------------------------------- #
def install_apk():
    file = customtkinter.filedialog.askopenfilename()
    if vars.debug:
        print(file)
    else:
        device.install(file)

class Brightness:
    def __init__(self):
        pass

    def set(value):
        if not debug:
            device.shell("settings put system screen_brightness " + str(int(value)))

    def get():
        if not debug:
            var: str = device.shell("settings get system screen_brightness")
            return var.strip()
        else:
            return 255

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

class PLevel:
    def __init__(self):
        pass

    def cpu(value):
        print(f"setprop debug.oculus.cpuLevel {value}")
        if not debug:
            device.shell(f"setprop debug.oculus.cpuLevel {value}")

    def gpu(value):
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
# Capture size
cs_w = 1024
cs_h = 1024
def cs_width(eh):
    switch={
        "640x480": 640,
        "1280x720": 1280,
        "1920x1080": 1920,
        "1024x1024 (default)": 1024,
        "1600x1600": 1600
    }
    return switch.get(eh)

def cs_height(eh):
    switch={
        "640x480": 480,
        "1280x720": 720,
        "1920x1080": 1080,
        "1024x1024 (default)": 1024,
        "1600x1600": 1600
    }
    return switch.get(eh)

def set_cs(value):
    cs_w = cs_width(value)
    cs_h = cs_height(value)
    if not debug:
        device.shell(f"setprop debug.oculus.capture.width {tex_w}")
        device.shell(f"setprop debug.oculus.capture.height {tex_h}")

# fps
def fps(eh):
    switch={
        "24fps": 24,
        "30fps": 30,
        "60fps": 60
    }
    return switch.get(eh)

def set_fps(value):
    new_fps = fps(value)
    if not debug:
        device.shell(f"setprop debug.oculus.capture.fps {new_fps}")

# bitrate
def bitrate(eh):
    switch={
        "5mbps": 5000000,
        "10mbps": 10000000,
        "15mbps": 15000000,
        "20mbps": 20000000
    }
    return switch.get(eh)

def set_bitrate(value):
    new_bitrate = bitrate(value)
    if not debug:
        device.shell(f"setprop debug.oculus.capture.bitrate {new_bitrate}")

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
            var: str = device.shell("dumpsys CompanionService | grep Battery")
            hmd_bat = var.strip().split(":")[1].strip()
            return hmd_bat
        else:
            return str(var_hmd_bat)
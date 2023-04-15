from common import *

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
        adbdevice.device.shell(f"setprop debug.oculus.capture.width {cs_w}")
        adbdevice.device.shell(f"setprop debug.oculus.capture.height {cs_h}")


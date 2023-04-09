from common import *

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


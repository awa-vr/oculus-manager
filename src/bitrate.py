from common import *

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
        adbdevice.device.shell(f"setprop debug.oculus.capture.bitrate {new_bitrate}")

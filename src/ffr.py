from common import *

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
        logger.debug(f"debug.oculus.foveation.level {eh}")
        if not debug:
            device.shell(f"debug.oculus.foveation.level {eh}")
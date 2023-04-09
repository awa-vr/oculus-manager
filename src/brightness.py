from common import *

class Brightness:
    def __init__(self):
        pass

    def set(value):
        logging.debug("Brightness set " + str(int(value)))
        if not debug:
            device.shell("settings put system screen_brightness " + str(int(value)))

    def get():
        if not debug:
            var: str = device.shell("settings get system screen_brightness")
            logging.debug("Brightness = " + var.strip())
            return var.strip()
        else:
            logging.debug("Brightness = " + str(255))
            return 255
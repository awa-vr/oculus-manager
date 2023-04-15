import customtkinter

from vars import *
from common import *

def install_apk():
    file = customtkinter.filedialog.askopenfilename()
    if vars.debug:
        logger.debug(file)
    else:
        adbdevice.device.install(file)
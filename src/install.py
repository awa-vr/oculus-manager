import customtkinter

from vars import *
from common import *
import device

def install_apk():
    file = customtkinter.filedialog.askopenfilename()
    if vars.debug:
        logger.debug(file)
    else:
        device.install(file)
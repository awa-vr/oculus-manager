import customtkinter

from vars import *
import device

def install_apk():
    file = customtkinter.filedialog.askopenfilename()
    if vars.debug:
        print(file)
    else:
        device.install(file)
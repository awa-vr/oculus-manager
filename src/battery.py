from common import *
import sys

class Battery:
    def __init__(self):
        pass

    def get_l():
        if not debug:
            var: str = adbdevice.device.shell("dumpsys OVRRemoteService | grep Battery")
            var = var.strip().split(",")
            try:
                lbat = var[8].split(":")[1].strip()[:-1]
            except:
                logger.critical("Connected device is not a quest, now exiting")
                warning = adbdevice.Warning()
                warning.geometry("350x100")
                warning.title("Oculus manager - Wrong adb device")
                warning.lbl.configure(text="Connected device is not a quest")
                warning.mainloop()
                sys.exit()
            logger.debug("lbat: " + lbat)
            return lbat
        else:
            logger.debug("lbat: " + str(var_lcon_bat))
            return str(var_lcon_bat)

    def get_r():
        if not debug:
            var: str = adbdevice.device.shell("dumpsys OVRRemoteService | grep Battery")
            var = var.strip().split(",")
            rbat = var[3].split(":")[1].strip()[:-1]
            logger.debug("rbat: " + rbat)
            return rbat
        else:
            logger.debug("rbat: " + str(var_rcon_bat))
            return str(var_rcon_bat)

    def get_hmd():
        if not debug:
            var: str = adbdevice.device.shell("dumpsys CompanionService | grep Battery")
            hmd_bat = var.strip().split(":")[1].strip()
            logger.debug("hmdbat: " + hmd_bat)
            return hmd_bat
        else:
            logger.debug("hmdbat: " + str(var_hmd_bat))
            return str(var_hmd_bat)
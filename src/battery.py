from common import *

class Battery:
    def __init__(self):
        pass

    def get_l():
        if not debug:
            var: str = device.shell("dumpsys OVRRemoteService | grep Battery")
            var = var.strip().split(",")
            lbat = var[8].split(":")[1].strip()[:-1]
            logging.debug("lbat: " + lbat)
            return lbat
        else:
            logging.debug("lbat: " + str(var_lcon_bat))
            return str(var_lcon_bat)

    def get_r():
        if not debug:
            var: str = device.shell("dumpsys OVRRemoteService | grep Battery")
            var = var.strip().split(",")
            rbat = var[3].split(":")[1].strip()[:-1]
            logging.debug("rbat: " + rbat)
            return rbat
        else:
            logging.debug("rbat: " + str(var_rcon_bat))
            return str(var_rcon_bat)

    def get_hmd():
        if not debug:
            var: str = device.shell("dumpsys CompanionService | grep Battery")
            hmd_bat = var.strip().split(":")[1].strip()
            logging.debug("hmdbat: " + hmd_bat)
            return hmd_bat
        else:
            logging.debug("hmdbat: " + str(var_hmd_bat))
            return str(var_hmd_bat)
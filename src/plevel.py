from common import *

class PLevel:
    def __init__(self):
        pass

    def cpu(value):
        logging.debug(f"setprop debug.oculus.cpuLevel {value}")
        if not debug:
            device.shell(f"setprop debug.oculus.cpuLevel {value}")

    def gpu(value):
        logging.debug(f"setprop debug.oculus.gpuLevel {value}")
        if not debug:
            device.shell(f"setprop debug.oculus.gpuLevel {value}")
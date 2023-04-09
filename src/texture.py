from common import *

tex_w = 1440
tex_h = 1584
def tex_width(eh):
    switch={
        "default": 1440,
        "512": 512,
        "768": 768,
        "1024": 1024,
        "1280": 1280,
        "1440": 1440,
        "1536": 1536,
        "2048": 2048,
        "2560": 2560,
        "3072": 3072
    }
    return switch.get(eh)

def tex_height(eh):
    switch={
        "default": 1584,
        "512": 563,
        "768": 845,
        "1024": 1127,
        "1280": 1408,
        "1440": 1584,
        "1536": 1690,
        "2048": 2253,
        "2560": 2816,
        "3072": 3380
    }
    return switch.get(eh)

def set_texture(choice):
    tex_w = tex_width(choice)
    tex_h = tex_height(choice)
    logging.debug(f"setprop debug.oculus.textureWidth {tex_w}")
    logging.debug(f"setprop debug.oculus.textureHeight {tex_h}")
    # logging.debug(f"settings put system font_scale 0.85 && settings put system font_scale 1.0") # idk if this is needed
    if not debug:
        device.shell(f"setprop debug.oculus.textureWidth {tex_w}")
        device.shell(f"setprop debug.oculus.textureHeight {tex_h}")
        # device.shell(f"settings put system font_scale 0.85 && settings put system font_scale 1.0") # idk if this is needed
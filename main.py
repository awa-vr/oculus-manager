import customtkinter
# import json
import os
import vars
import utils

customtkinter.set_appearance_mode("system")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()
app.geometry("400x400")
app.title("Oculus manager")
app.minsize(width=360, height=400)

# ---------------------------------------------------------------------------- #
#                                   Functions                                  #
# ---------------------------------------------------------------------------- #
def prox():
    print("switch toggled, current value:", prox_var.get())
    if not vars.debug:
        if prox_var.get() == "on":
            utils.device.shell("am broadcast -a com.oculus.vrpowermanager.automation_disable")
        else:
            utils.device.shell("am broadcast -a com.oculus.vrpowermanager.prox_close")

def refresh():
    l_bat_pro.set(int(utils.get_l_bat()) / 100)
    r_bat_pro.set(int(utils.get_r_bat()) / 100)
    hmd_bat_pro.set(int(utils.get_hmd_bat()) / 100)
    l_bat_lbl.configure(text="Left controller battery: " + utils.get_l_bat() + "%")
    r_bat_lbl.configure(text="Right controller battery: " + utils.get_r_bat() + "%")
    hmd_bat_lbl.configure(text="Headset battery: " + utils.get_hmd_bat() + "%")
    if int(utils.get_hmd_bat()) <= 15:
        hmd_bat_pro.configure(progress_color="red")
    if int(utils.get_l_bat()) <= 15:
        l_bat_pro.configure(progress_color="red")
    if int(utils.get_r_bat()) <= 15:
        r_bat_pro.configure(progress_color="red")
    app.after(5000, refresh)

def set_theme(choice):
    customtkinter.set_appearance_mode(choice)

# ---------------------------------------------------------------------------- #
#                                Create tabview                                #
# ---------------------------------------------------------------------------- #
tabview = customtkinter.CTkTabview(app, width=500)
tabview.pack(padx=10, pady=10, fill="both", expand=True)

general = tabview.add("General")
performance = tabview.add("Performance")
recording = tabview.add("Recording")
misc = tabview.add("Misc")
settings = tabview.add("Settings")

# ---------------------------------------------------------------------------- #
#                                    General                                   #
# ---------------------------------------------------------------------------- #
# Brightness
brightness_lbl = customtkinter.CTkLabel(general, text="Brightness:")
brightness_slider = customtkinter.CTkSlider(general, from_=0, to=255, command=utils.set_brightness)
brightness_lbl.pack(side="top", anchor="w")
brightness_slider.pack(side="top", anchor="w", padx=20)

# Battery bars
l_bat_pro = customtkinter.CTkProgressBar(general)
r_bat_pro = customtkinter.CTkProgressBar(general)
hmd_bat_pro = customtkinter.CTkProgressBar(general)

l_bat_pro.set(int(utils.get_l_bat()) / 100)
r_bat_pro.set(int(utils.get_r_bat()) / 100)
hmd_bat_pro.set(int(utils.get_hmd_bat()) / 100)

# Battery labels
hmd_bat_lbl = customtkinter.CTkLabel(general) # text gets updated in refresh()
l_bat_lbl = customtkinter.CTkLabel(general) # text gets updated in refresh()
r_bat_lbl = customtkinter.CTkLabel(general) # text gets updated in refresh()

# Place battery labels and bars
hmd_bat_lbl.pack(side="top", anchor="w", pady=(10, 0))
hmd_bat_pro.pack(side="top", anchor="w", padx=20)

l_bat_lbl.pack(side="top", anchor="w", pady=(10, 0))
l_bat_pro.pack(side="top", anchor="w", padx=20)

r_bat_lbl.pack(side="top", anchor="w", pady=(10, 0))
r_bat_pro.pack(side="top", anchor="w", padx=20)

# Refresh rate
refresh_lbl = customtkinter.CTkLabel(general, text="Refresh rate:")
refresh_button = customtkinter.CTkSegmentedButton(general, values=["60Hz", "72Hz", "90Hz", "120Hz"], command=utils.set_refresh_rate)
refresh_button.set(utils.get_refresh())

refresh_lbl.pack(side="top", anchor="w", pady=(10, 0))
refresh_button.pack(side="top", anchor="w", padx=10)

# Proximity sensor
prox_lbl = customtkinter.CTkLabel(general, text="Proximity sensor:")
prox_var = customtkinter.StringVar(value="on")
prox_switch = customtkinter.CTkSwitch(general, text="Proximity sensor", command=prox, variable=prox_var, onvalue="on", offvalue="off")
prox_lbl.pack(side="top", anchor="w", pady=(10, 0))
prox_switch.pack(side="top", anchor="w", padx=20)

# ---------------------------------------------------------------------------- #
#                                  Performance                                 #
# ---------------------------------------------------------------------------- #
cpu_lbl = customtkinter.CTkLabel(performance, text="cpu level")
gpu_lbl = customtkinter.CTkLabel(performance, text="gpu level")

cpu_button = customtkinter.CTkSegmentedButton(performance, values=["0", "1", "2", "3", "4"], command=utils.set_cpu)
gpu_button = customtkinter.CTkSegmentedButton(performance, values=["0", "1", "2", "3", "4"], command=utils.set_gpu)
cpu_lbl.pack(side="top", anchor="w")
cpu_button.pack(side="top", anchor="w", padx=10)
gpu_lbl.pack(side="top", anchor="w", pady=(10, 0))
gpu_button.pack(side="top", anchor="w", padx=10)

# texture values from sidequest
tex_size_lbl = customtkinter.CTkLabel(performance, text="Texture size:")
tex_size_cb = customtkinter.CTkComboBox(performance, values=["default", "512", "768", "1024", "1280", "1440", "1536", "2048", "2560", "3072"], command=utils.set_texture)
tex_size_lbl.pack(side="top", anchor="w", pady=(10, 0))
tex_size_cb.pack(side="top", anchor="w", padx=10)

# ffr
ffr_lbl = customtkinter.CTkLabel(performance, text="FFR:")
ffr_cb = customtkinter.CTkComboBox(performance, values=["off", "low", "medium", "high", "max"], command=utils.set_ffr)
ffr_lbl.pack(side="top", anchor="w", pady=(10, 0))
ffr_cb.pack(side="top", anchor="w", padx=10)

# ---------------------------------------------------------------------------- #
#                                   Recording                                  #
# ---------------------------------------------------------------------------- #
# capture size
cs_lbl = customtkinter.CTkLabel(recording, text="Capture size")
cs_cb = customtkinter.CTkComboBox(recording, values=["640x480", "1280x720", "1920x1080", "1024x1024 (default)", "1600x1600"], width=170, command=utils.set_cs)
cs_cb.set("1024x1024 (default)")
cs_lbl.pack(side="top", anchor="w")
cs_cb.pack(side="top", anchor="w", padx=10)

# fps
fps_lbl = customtkinter.CTkLabel(recording, text="FPS:")
fps_cb = customtkinter.CTkComboBox(recording, values=["24fps", "30fps", "60fps"])
fps_lbl.pack(side="top", anchor="w", pady=(10, 0))
fps_cb.pack(side="top", anchor="w", padx=10)


# Bitrate
bitrate_lbl = customtkinter.CTkLabel(recording, text="Bitrate:")
bitrate_cb = customtkinter.CTkComboBox(recording, values=["5mpbs", "10mpbs", "15mpbs", "20mpbs"])
bitrate_lbl.pack(side="top", anchor="w", pady=(10, 0))
bitrate_cb.pack(side="top", anchor="w", padx=10)

# ---------------------------------------------------------------------------- #
#                                     Misc                                     #
# ---------------------------------------------------------------------------- #
apk_install_btn = customtkinter.CTkButton(misc, text="Choose apk to install", command=utils.install_apk)
apk_install_btn.pack()

# TODO: Oculus killer (https://github.com/LibreQuest/OculusKiller)
killer_v2_btn = customtkinter.CTkButton(misc, text="Install Oculus Killer v2", command=utils.install_killer_v2, fg_color="yellow", text_color="black")
killer_v2_btn.pack(pady=(10,0))

killer_btn = customtkinter.CTkButton(misc, text="Install Oculus killer", command=utils.install_killer, fg_color="yellow", text_color="black")
killer_btn.pack(pady=(10,0))

# ---------------------------------------------------------------------------- #
#                                   Settings                                   #
# ---------------------------------------------------------------------------- #
theme = customtkinter.CTkComboBox(settings, values=["system", "light", "dark"], command=set_theme)
theme.pack()

my_font = customtkinter.CTkFont(size=18)
love_lbl = customtkinter.CTkLabel(settings, text="Made with 💖", font=my_font)
love_lbl.pack(side="bottom", anchor="s")

# ---------------------------------------------------------------------------- #
#                                     Loop                                     #
# ---------------------------------------------------------------------------- #
refresh()
app.mainloop()
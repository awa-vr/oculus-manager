import customtkinter
# import json
import os
import vars
import utils

customtkinter.set_appearance_mode("system")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()
app.geometry("600x400")
app.title("Oculus manager")
app.minsize(width=350, height=350)

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

def install_apk():
    file = customtkinter.filedialog.askopenfilename()
    if vars.debug:
        print(file)
    else:
        os.system(str("adb install " + file)) # TODO: Change to use pure-python-adb

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

hmd_bat_lbl.pack(side="top", anchor="w")
hmd_bat_pro.pack(side="top", anchor="w", padx=20)

l_bat_lbl.pack(side="top", anchor="w")
l_bat_pro.pack(side="top", anchor="w", padx=20)

r_bat_lbl.pack(side="top", anchor="w")
r_bat_pro.pack(side="top", anchor="w", padx=20)

# Refresh rate
refresh_lbl = customtkinter.CTkLabel(general, text="Refresh rate:")
refresh_button = customtkinter.CTkSegmentedButton(general, values=["60Hz", "72Hz", "90Hz", "120Hz"], command=utils.set_refresh_rate)
refresh_button.set(utils.get_refresh())

refresh_lbl.pack(side="top", anchor="w")
refresh_button.pack(side="top", anchor="w", padx=10)

# Proximity sensor
prox_lbl = customtkinter.CTkLabel(general, text="Proximity sensor:")
prox_var = customtkinter.StringVar(value="on")
prox_switch = customtkinter.CTkSwitch(general, text="Proximity sensor", command=prox, variable=prox_var, onvalue="on", offvalue="off")
prox_lbl.pack(side="top", anchor="w")
prox_switch.pack(side="top", anchor="w", padx=20)

# ---------------------------------------------------------------------------- #
#                                  Performance                                 #
# ---------------------------------------------------------------------------- #
cpu_lbl = customtkinter.CTkLabel(performance, text="cpu level")
gpu_lbl = customtkinter.CTkLabel(performance, text="gpu level")

cpu_button = customtkinter.CTkSegmentedButton(performance, values=["0", "1", "2", "3", "4"], command=utils.set_cpu)
gpu_button = customtkinter.CTkSegmentedButton(performance, values=["0", "1", "2", "3", "4"], command=utils.set_gpu)
cpu_lbl.pack()
cpu_button.pack(padx=20, pady=10)
gpu_lbl.pack()
gpu_button.pack(padx=20, pady=10)

# texture values from sidequest
tex_size_cb = customtkinter.CTkComboBox(performance, values=["default", "512", "768", "1024", "1280", "1536", "2048", "2560", "3072"], command=utils.set_texture)
tex_size_cb.pack()

ffr_cb = customtkinter.CTkComboBox(performance, values=["off", "low", "medium", "high", "max"], command=utils.set_ffr)
ffr_cb.pack()

# ---------------------------------------------------------------------------- #
#                                   Recording                                  #
# ---------------------------------------------------------------------------- #
# TODO: Everything

# ---------------------------------------------------------------------------- #
#                                     Misc                                     #
# ---------------------------------------------------------------------------- #
apk_install_btn = customtkinter.CTkButton(misc, text="Choose apk to install", command=install_apk)
apk_install_btn.pack()
# TODO: Rest of functionality
    # TODO: Oculus killer (https://github.com/LibreQuest/OculusKiller)

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
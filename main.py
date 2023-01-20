import customtkinter
# import json
import os
import vars
import utils

customtkinter.set_appearance_mode("system")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

# ---------------------------------------------------------------------------- #
#                                   Functions                                  #
# ---------------------------------------------------------------------------- #
def prox():
    pass
#     print("switch toggled, current value:", prox_var.get())
#     if not vars.debug:
#         if prox_var.get() == "on":
#             utils.device.shell("am broadcast -a com.oculus.vrpowermanager.automation_disable")
#         else:
#             utils.device.shell("am broadcast -a com.oculus.vrpowermanager.prox_close")



def set_theme(choice):
    customtkinter.set_appearance_mode(choice)

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("400x400")
        self.title("Oculus manager")
        self.minsize(width=360, height=400)

        # ---------------------------------------------------------------------------- #
        #                                Create tabview                                #
        # ---------------------------------------------------------------------------- #
        self.tabview = customtkinter.CTkTabview(self, width=500)
        self.tabview.pack(padx=10, pady=10, fill="both", expand=True)

        self.general_tab = self.tabview.add("General")
        self.performance_tab = self.tabview.add("Performance")
        self.recording_tab = self.tabview.add("Recording")
        self.misc_tab = self.tabview.add("Misc")
        self.settings_tab = self.tabview.add("Settings")

        self.my_battery = utils.Battery

        self.general()
        self.performance()
        self.recording()
        self.misc()
        self.settings()


    # ---------------------------------------------------------------------------- #
    #                                    General                                   #
    # ---------------------------------------------------------------------------- #
    def general(self):
        # Brightness
        brightness_lbl = customtkinter.CTkLabel(self.general_tab, text="Brightness:")
        brightness_slider = customtkinter.CTkSlider(self.general_tab, from_=0, to=255, command=utils.set_brightness)
        brightness_lbl.pack(side="top", anchor="w")
        brightness_slider.pack(side="top", anchor="w", padx=20)

        # Battery bars
        self.l_bat_pro = customtkinter.CTkProgressBar(self.general_tab)
        self.r_bat_pro = customtkinter.CTkProgressBar(self.general_tab)
        self.hmd_bat_pro = customtkinter.CTkProgressBar(self.general_tab)

        self.l_bat_pro.set(int(self.my_battery.get_l()) / 100)
        self.r_bat_pro.set(int(self.my_battery.get_r()) / 100)
        self.hmd_bat_pro.set(int(self.my_battery.get_hmd()) / 100)

        # Battery labels
        self.hmd_bat_lbl = customtkinter.CTkLabel(self.general_tab) # text gets updated in refresh()
        self.l_bat_lbl = customtkinter.CTkLabel(self.general_tab) # text gets updated in refresh()
        self.r_bat_lbl = customtkinter.CTkLabel(self.general_tab) # text gets updated in refresh()

        # Place battery labels and bars
        self.hmd_bat_lbl.pack(side="top", anchor="w", pady=(10, 0))
        self.hmd_bat_pro.pack(side="top", anchor="w", padx=20)

        self.l_bat_lbl.pack(side="top", anchor="w", pady=(10, 0))
        self.l_bat_pro.pack(side="top", anchor="w", padx=20)

        self.r_bat_lbl.pack(side="top", anchor="w", pady=(10, 0))
        self.r_bat_pro.pack(side="top", anchor="w", padx=20)

        # Refresh rate
        refresh_lbl = customtkinter.CTkLabel(self.general_tab, text="Refresh rate:")
        refresh_button = customtkinter.CTkSegmentedButton(self.general_tab, values=["60Hz", "72Hz", "90Hz", "120Hz"], command=utils.RefreshRate.set)
        refresh_button.set(utils.RefreshRate.get())

        refresh_lbl.pack(side="top", anchor="w", pady=(10, 0))
        refresh_button.pack(side="top", anchor="w", padx=10)

        # Proximity sensor
        prox_lbl = customtkinter.CTkLabel(self.general_tab, text="Proximity sensor:")
        self.prox_var = customtkinter.StringVar(value="on")
        prox_switch = customtkinter.CTkSwitch(self.general_tab, text="Proximity sensor", command=prox, variable=self.prox_var, onvalue="on", offvalue="off")
        prox_lbl.pack(side="top", anchor="w", pady=(10, 0))
        prox_switch.pack(side="top", anchor="w", padx=20)

    # ---------------------------------------------------------------------------- #
    #                                  Performance                                 #
    # ---------------------------------------------------------------------------- #
    def performance(self):
        cpu_lbl = customtkinter.CTkLabel(self.performance_tab, text="cpu level")
        gpu_lbl = customtkinter.CTkLabel(self.performance_tab, text="gpu level")

        cpu_button = customtkinter.CTkSegmentedButton(self.performance_tab, values=["0", "1", "2", "3", "4"], command=utils.set_cpu)
        gpu_button = customtkinter.CTkSegmentedButton(self.performance_tab, values=["0", "1", "2", "3", "4"], command=utils.set_gpu)
        cpu_lbl.pack(side="top", anchor="w")
        cpu_button.pack(side="top", anchor="w", padx=10)
        gpu_lbl.pack(side="top", anchor="w", pady=(10, 0))
        gpu_button.pack(side="top", anchor="w", padx=10)

        # texture values from sidequest
        tex_size_lbl = customtkinter.CTkLabel(self.performance_tab, text="Texture size:")
        tex_size_cb = customtkinter.CTkComboBox(self.performance_tab, values=["default", "512", "768", "1024", "1280", "1440", "1536", "2048", "2560", "3072"], command=utils.set_texture)
        tex_size_lbl.pack(side="top", anchor="w", pady=(10, 0))
        tex_size_cb.pack(side="top", anchor="w", padx=10)

        # ffr
        my_ffr = utils.FFR

        ffr_lbl = customtkinter.CTkLabel(self.performance_tab, text="FFR:")
        ffr_cb = customtkinter.CTkComboBox(self.performance_tab, values=["off", "low", "medium", "high", "max"], command=my_ffr.set)
        ffr_lbl.pack(side="top", anchor="w", pady=(10, 0))
        ffr_cb.pack(side="top", anchor="w", padx=10)

    # ---------------------------------------------------------------------------- #
    #                                   Recording                                  #
    # ---------------------------------------------------------------------------- #
    def recording(self):
        # capture size
        cs_lbl = customtkinter.CTkLabel(self.recording_tab, text="Capture size")
        cs_cb = customtkinter.CTkComboBox(self.recording_tab, values=["640x480", "1280x720", "1920x1080", "1024x1024 (default)", "1600x1600"], width=170, command=utils.set_cs)
        cs_cb.set("1024x1024 (default)")
        cs_lbl.pack(side="top", anchor="w")
        cs_cb.pack(side="top", anchor="w", padx=10)

        # fps
        fps_lbl = customtkinter.CTkLabel(self.recording_tab, text="FPS:")
        fps_cb = customtkinter.CTkComboBox(self.recording_tab, values=["24fps", "30fps", "60fps"])
        fps_lbl.pack(side="top", anchor="w", pady=(10, 0))
        fps_cb.pack(side="top", anchor="w", padx=10)


        # Bitrate
        bitrate_lbl = customtkinter.CTkLabel(self.recording_tab, text="Bitrate:")
        bitrate_cb = customtkinter.CTkComboBox(self.recording_tab, values=["5mpbs", "10mpbs", "15mpbs", "20mpbs"])
        bitrate_lbl.pack(side="top", anchor="w", pady=(10, 0))
        bitrate_cb.pack(side="top", anchor="w", padx=10)

    # ---------------------------------------------------------------------------- #
    #                                     Misc                                     #
    # ---------------------------------------------------------------------------- #
    def misc(self):
        apk_install_btn = customtkinter.CTkButton(self.misc_tab, text="Choose apk to install", command=utils.install_apk)
        apk_install_btn.pack()

        # TODO: Oculus killer (https://github.com/LibreQuest/OculusKiller)
        killer_v2_btn = customtkinter.CTkButton(self.misc_tab, text="Install Oculus Killer v2", command=utils.install_killer_v2, fg_color="yellow", text_color="black")
        killer_v2_btn.pack(pady=(10,0))

        killer_btn = customtkinter.CTkButton(self.misc_tab, text="Install Oculus killer", command=utils.install_killer, fg_color="yellow", text_color="black")
        killer_btn.pack(pady=(10,0))

    # ---------------------------------------------------------------------------- #
    #                                   Settings                                   #
    # ---------------------------------------------------------------------------- #
    def settings(self):
        theme = customtkinter.CTkComboBox(self.settings_tab, values=["system", "light", "dark"], command=set_theme)
        theme.pack()

        my_font = customtkinter.CTkFont(size=18)
        love_lbl = customtkinter.CTkLabel(self.settings_tab, text="Made with 💖", font=my_font)
        love_lbl.pack(side="bottom", anchor="s")

    def refresh(self):
        l_bat = self.my_battery.get_l()
        r_bat = self.my_battery.get_r()
        hmd_bat = self.my_battery.get_hmd()

        self.l_bat_pro.set(int(l_bat) / 100)
        self.r_bat_pro.set(int(r_bat) / 100)
        self.hmd_bat_pro.set(int(hmd_bat) / 100)
        self.l_bat_lbl.configure(text="Left controller battery: " + l_bat + "%")
        self.r_bat_lbl.configure(text="Right controller battery: " + r_bat + "%")
        self.hmd_bat_lbl.configure(text="Headset battery: " + hmd_bat + "%")

        if int(hmd_bat) <= 20 and int(hmd_bat) > 15:
            self.hmd_bat_pro.configure(progress_color="yellow")
        elif int(hmd_bat) <= 15:
            self.hmd_bat_pro.configure(progress_color="red")

        if int(l_bat) <= 20 and int(l_bat) > 15:
            self.l_bat_pro.configure(progress_color="yellow")
        elif int(l_bat) <= 15:
            self.l_bat_pro.configure(progress_color="red")

        if int(r_bat) <= 20 and int(r_bat) > 15:
            self.r_bat_pro.configure(progress_color="yellow")
        elif int(r_bat) <= 15:
            self.r_bat_pro.configure(progress_color="red")

        self.after(5000, self.refresh)

# ---------------------------------------------------------------------------- #
#                                     Loop                                     #
# ---------------------------------------------------------------------------- #
if __name__ == "__main__":
    app = App()
    app.refresh()
    app.mainloop()
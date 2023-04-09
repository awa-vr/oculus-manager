import os
import customtkinter
import appdirs
import requests
import zipfile
from ppadb.client import Client as AdbClient
from vars import *

app_name = "Oculus Manager"

adb_connected = False

class Warning(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        self.geometry("200x100")
        self.title("Oculus manager - No adb devices")
        self.lbl = customtkinter.CTkLabel(self, text="No adb devices found", font=customtkinter.CTkFont(size=18))
        self.lbl.pack(padx=10, pady=10, fill="both", expand=True)

        self.btn = customtkinter.CTkButton(self, text="Ok", command=self.btn_action)
        self.btn.pack(padx=10, pady=10)
    
    def btn_action(self):
        quit()

import json
import os
import customtkinter as ctk

SETTINGS_FILE = "settings.json"

def save_settings():
    settings = {
        "appearance_mode": ctk.get_appearance_mode()
    }
    with open(SETTINGS_FILE, "w") as f:
        json.dump(settings, f)

def load_settings():
    if os.path.exists(SETTINGS_FILE):
        try:
            with open(SETTINGS_FILE, "r") as f:
                settings = json.load(f)
                return settings.get("appearance_mode", "Dark")
        except json.JSONDecodeError:
            # File is empty or corrupted, return default
            return "Dark"
    return "Dark"

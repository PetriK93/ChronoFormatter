import tkinter as tk
from tkinter import font as tkfont
import customtkinter as ctk
from PIL import Image
import os
import settings
from modules.choose_folder import select_folder

# Define colors for dark and light mode.
dark_colors = {
    "button": "#006400",
    "border": "#008500",
    "hover": "#004400",
    "background": "#2b2b2b",
    "input": "white",
    "font": "black"
}

light_colors = {
    "button": "#8B4513",
    "border": "#8B4513",
    "hover": "#69380C",
    "background": "#FFE5B4",
    "input": "white",
    "font": "black"
}


# Initialize colors based on the last used color mode.
last_mode = settings.load_settings()
ctk.set_appearance_mode(last_mode)
current_mode = ctk.get_appearance_mode()
colors = dark_colors if current_mode == "Dark" else light_colors

button_color = colors["button"]
border_color = colors["border"]
hover_color = colors["hover"]
background_color = colors["background"]
input_color = colors["input"]
font_color = colors["font"]

def change_appearance_mode(event=None):
    global button_color, border_color, hover_color, background_color, input_color, font_color
    
    # Switch mode.
    current_mode = ctk.get_appearance_mode()
    if current_mode == "Dark":
        ctk.set_appearance_mode("Light")
        colors = light_colors
    else:
        ctk.set_appearance_mode("Dark")
        colors = dark_colors

    # Update global color variables.
    button_color = colors["button"]
    border_color = colors["border"]
    hover_color = colors["hover"]
    background_color = colors["background"]
    input_color = colors["input"]
    font_color = colors["font"]

    # Update widgets.
    root.configure(fg_color=background_color)
    choose_folder_button.configure(fg_color=button_color, hover_color=hover_color)
    rename_button.configure(fg_color=button_color, hover_color=hover_color)
    prefix.configure(border_color=border_color, fg_color=input_color, text_color=font_color)
    dropdown_time_format.configure(fg_color=button_color, button_color=button_color, hover=hover_color)
    dropdown_file_type.configure(fg_color=button_color, button_color=button_color, hover=hover_color)
    
    # Save the new mode.
    settings.save_settings()

# Print dropdown menu choice.
def check_choice(choice):
    print(f"The user selected: {choice}")

# Main window.
root = ctk.CTk()
root.title("ChronoFormatter")
root.geometry("300x500")
root.resizable(False, False)
root.configure(fg_color=background_color)

# Get available fonts on the system
available_fonts = tkfont.families()

# Choose Roboto if available, otherwise fallback to Arial
font_family = "Roboto" if "Roboto" in available_fonts else "Arial"

# Configure the global default Tk font
default_font = tkfont.nametofont("TkDefaultFont")
default_font.configure(family=font_family, size=12)

# Where main.py is
base_dir = os.path.dirname(os.path.abspath(__file__))
assets_dir = os.path.join(base_dir, "assets")

# Images.
color_mode_image = ctk.CTkImage(
    light_image=Image.open(os.path.join(assets_dir, "light_mode_icon.png")),
    dark_image=Image.open(os.path.join(assets_dir, "dark_mode_icon.png")),
    size=(32, 32)
)

logo_image = ctk.CTkImage(
    light_image=Image.open(os.path.join(assets_dir, "ChronoFormatter_logo_light.png")),
    dark_image=Image.open(os.path.join(assets_dir, "ChronoFormatter_logo_dark.png")),
    size=(250, 250)
)

pencil_photo = ctk.CTkImage(
    light_image=Image.open(os.path.join(assets_dir, "pencil_image.png")),
    dark_image=Image.open(os.path.join(assets_dir, "pencil_image.png")),
    size=(22, 22)
)

folder_photo = ctk.CTkImage(
    light_image=Image.open(os.path.join(assets_dir, "folder_image.png")),
    dark_image=Image.open(os.path.join(assets_dir, "folder_image.png")),
    size=(22, 22)
)

# Widgets.
color_mode_label = ctk.CTkLabel(
    master=root,
    image=color_mode_image,
    text="",
    cursor="hand2"
)

logo_label = ctk.CTkLabel(
    master=root,
    image=logo_image,
    text=""
)

prefix_label = ctk.CTkLabel(
    master=root,
    text="Enter a prefix for your images:",
    font=(font_family, 14)
)

prefix = ctk.CTkEntry(
    master=root,
    placeholder_text="Example: WoW or GW2",
    width=200,
    height=35,
    font=(font_family, 16),
    border_width=2,
    corner_radius=4,
    border_color=border_color,
    fg_color=input_color
)

choose_folder_button = ctk.CTkButton(
    master=root,
    text="Choose folder      ",
    image=folder_photo,
    anchor="w",
    compound="right",  
    fg_color=button_color,
    text_color="white",
    hover_color=hover_color,
    corner_radius=10,
    height=40,
    width=185,
    font=(font_family, 13, "bold"),
    cursor="hand2",
    command=select_folder
)

rename_button = ctk.CTkButton(
    master=root,
    text="Rename images   ",
    image=pencil_photo,
    anchor="w",
    compound="right",  
    fg_color=button_color,
    text_color="white",
    hover_color=hover_color,
    corner_radius=10,
    height=40,
    width=185,
    font=(font_family, 13, "bold"),
    cursor="hand2"
)

# Placeholder text for the dropdown menu.
choose_format = tk.StringVar()
choose_format.set("Choose format")

# Dropdown menu to select the desired time format for the images.
dropdown_time_format = ctk.CTkOptionMenu(
    master=root,
    variable=choose_format,
    values=["ISO (YYYY-MM-DD)", "EU (DD-MM-YYYY)", "US (MM-DD-YYYY)"],
    command=check_choice,
    button_color=button_color,
    fg_color=button_color,
    text_color="white",
    corner_radius=10,
    height=40,
    width=185,
    font=(font_family, 13, "bold"),
    cursor="hand2",
    hover = hover_color
)

# Placeholder text for the dropdown menu.
choose_file_type = tk.StringVar()
choose_file_type.set("Choose file type")

# Dropdown menu to select the desired file type.
dropdown_file_type = ctk.CTkOptionMenu(
    master=root,
    variable=choose_file_type,
    values=["Images", "Videos"],
    command=check_choice,
    button_color=button_color,
    fg_color=button_color,
    text_color="white",
    corner_radius=10,
    height=40,
    width=185,
    font=(font_family, 13, "bold"),
    cursor="hand2",
    hover = hover_color
)

# Widget positioning.
color_mode_label.place(relx=1.0, rely=0.0, anchor="ne", x=-10, y=10)
logo_label.place(relx=0.5, rely=0.20, anchor="center")
prefix_label.place(relx=0.5, rely=0.38, anchor="center")
prefix.place(relx=0.5, rely=0.45, anchor="center")
dropdown_time_format.place(relx=0.5, rely=0.57, anchor="center")
dropdown_file_type.place(relx=0.5, rely=0.67, anchor="center")
choose_folder_button.place(relx=0.5, rely=0.77, anchor="center")
rename_button.place(relx=0.5, rely=0.87, anchor="center")

# Make sure that color mode is always visible.
color_mode_label.lift()

# Bindings.
color_mode_label.bind("<Button-1>", lambda event: change_appearance_mode())

# Save settings on exit.
root.protocol("WM_DELETE_WINDOW", lambda: (settings.save_settings(), root.destroy()))


root.mainloop()

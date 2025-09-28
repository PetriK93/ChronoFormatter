import tkinter as tk
import customtkinter as ctk
from PIL import Image

# Set the appearance mode
ctk.set_appearance_mode("Dark")

current_mode = ctk.get_appearance_mode()

# Mode specific colors
if current_mode == "Dark":
    button_color = "#006400"
    border_color = "#006400"
    hover_color = "#004400"
    background_color = "#2b2b2b"
else:
    button_color = "#1E90FF"
    border_color = "#1E90FF"
    hover_color = "#104E8B"
    background_color = "#F0F4FF"

# Change appearance mode
def change_appearance_mode(event=None):
    global button_color, hover_color, border_color, background_color
    
    current_mode = ctk.get_appearance_mode()
    
    if current_mode == "Dark":
        ctk.set_appearance_mode("Light")
        bg_color = "#F0F4FF"
        btn_color = "#1E90FF"
        hover = "#104E8B"
        border = "#1E90FF"
        button_color = "#1E90FF"
    else:
        ctk.set_appearance_mode("Dark")
        bg_color = "#2b2b2b"
        btn_color = "#006400"
        hover = "#004400"
        border = "#006400"
        button_color = "#006400"

    # Update main window background
    root.configure(fg_color=bg_color)

    # Update buttons
    choose_folder_button.configure(fg_color=btn_color, hover_color=hover)
    rename_button.configure(fg_color=btn_color, hover_color=hover)
    prefix.configure(border_color=border)
    dropdown.configure(fg_color=btn_color, button_color=button_color, hover=hover_color)

# Print dropdown menu choice
def check_choice(choice):
    print(f"The user selected: {choice}")

# Main window
root = ctk.CTk()
root.title("ChronoFormatter")
root.geometry("300x500")
root.resizable(False, False)
root.configure(fg_color=background_color)

# Load images
color_mode_image = ctk.CTkImage(
    light_image=Image.open("light_mode_icon.png"),
    dark_image=Image.open("dark_mode_icon.png"),
    size=(32, 32)
)

logo_image = ctk.CTkImage(
    light_image=Image.open("ChronoFormatter_logo_light.png"),
    dark_image=Image.open("ChronoFormatter_logo_dark.png"),
    size=(250, 250)
)

pencil_photo = ctk.CTkImage(
    light_image=Image.open("pencil_image.png"),
    dark_image=Image.open("pencil_image.png"),
    size=(22, 22)
)

folder_photo = ctk.CTkImage(
    light_image=Image.open("folder_image.png"),
    dark_image=Image.open("folder_image.png"),
    size=(22, 22)
)

# Widgets
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
    font=("Arial", 14)
)

prefix = ctk.CTkEntry(
    master=root,
    placeholder_text="Example: WoW or GW2",
    width=200,
    height=35,
    font=("Arial", 16),
    border_width=2,
    corner_radius=4,
    border_color=border_color
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
    width=170,
    font=("Arial", 13, "bold"),
    cursor="hand2"
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
    width=170,
    font=("Arial", 13, "bold"),
    cursor="hand2"
)

# Placeholder text for the dropdown menu
choose_format = tk.StringVar()
choose_format.set("Choose a format")

dropdown = ctk.CTkOptionMenu(
    master=root,
    variable=choose_format,
    values=["ISO (YYYY-MM-DD)", "EU (DD-MM-YYYY)", "US (MM-DD-YYYY)"],
    command=check_choice,
    button_color=button_color,
    fg_color=button_color,
    text_color="white",
    corner_radius=10,
    height=40,
    width=170,
    font=("Arial", 13, "bold"),
    cursor="hand2",
    hover = hover_color
)

# Widget positioning
color_mode_label.place(relx=1.0, rely=0.0, anchor="ne", x=-5, y=10)
logo_label.place(relx=0.5, rely=0.20, anchor="center")
prefix_label.place(relx=0.5, rely=0.37, anchor="center")
prefix.place(relx=0.5, rely=0.45, anchor="center")
choose_folder_button.place(relx=0.5, rely=0.57, anchor="center")
rename_button.place(relx=0.5, rely=0.67, anchor="center")
dropdown.place(relx=0.5, rely=0.77, anchor="center")

# Make sure that color mode is always visible
color_mode_label.lift()

color_mode_label.bind("<Button-1>", lambda event: change_appearance_mode())


root.mainloop()

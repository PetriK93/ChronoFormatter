import tkinter as tk
from tkinter import font as tkfont
from tkinter import messagebox
import customtkinter as ctk
from PIL import Image
import os
import settings
from modules.choose_folder import select_folder
from modules.choose_format import format_filename, select_format
from modules.choose_file_type import select_file_type
from modules.rename_files import rename_files

# Define colors for dark and light mode.
dark_colors = {
    "button": "#006400",
    "border": "#008500",
    "hover": "#004400",
    "background": "#2b2b2b",
    "input": "white",
    "font": "black",
    "preview": "white"
}

light_colors = {
    "button": "#8B4513",
    "border": "#8B4513",
    "hover": "#69380C",
    "background": "#FFE5B4",
    "input": "white",
    "font": "black",
    "preview": "black"
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
preview_color = colors ["preview"]

# Store selected folder globally
selected_folder = None

# Select the folder and display the correct preview.
def handle_folder_selection():
    global selected_folder
    folder = select_folder(root, tick_box_folder_label, tick_box_image)

    if folder:  # only overwrite if a folder was chosen
        selected_folder = folder

    if selected_folder:  # use the stored folder for preview
        prefix_value = prefix.get().strip()
        format_choice = choose_format.get()
        file_type_choice = choose_file_type.get()

        if format_choice not in ["Choose format", ""] and file_type_choice in ["Images", "Videos"]:
            extension = ".jpg" if file_type_choice == "Images" else ".mp4"
            new_name = format_filename(prefix_value, format_choice, "", extension, counter=1)
            update_preview(preview_label, new_name, max_chars=35)
        else:
            update_preview(preview_label, "Ready to rename files", max_chars=35)
    else:
        update_preview(preview_label, "⚠️No folder selected", max_chars=35)

def change_appearance_mode(event=None):
    global button_color, border_color, hover_color, background_color, input_color, font_color, preview_color
    
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
    preview_color = colors["preview"]

    # Update widgets.
    root.configure(fg_color=background_color)
    choose_folder_button.configure(fg_color=button_color, hover_color=hover_color)
    rename_button.configure(fg_color=button_color, hover_color=hover_color)
    prefix.configure(border_color=border_color, fg_color=input_color, text_color=font_color)
    dropdown_time_format.configure(fg_color=button_color, button_color=button_color, hover=hover_color)
    dropdown_file_type.configure(fg_color=button_color, button_color=button_color, hover=hover_color)
    preview_label.configure(text_color=preview_color)
    
    # Save the new mode.
    settings.save_settings()
    
# Helper function to update preview with max character limit
def update_preview(label, text, max_chars=35):
    """
    Updates the label text with a maximum visible character limit.
    Adds '...' if the text is longer than max_chars.
    """
    if len(text) > max_chars:
        text = text[:max_chars-3] + "..."
    label.configure(text=text)
    
def update_preview_filename():
    """
    Generate the preview based on the current inputs and folder selection.
    Does NOT rename any files.
    """
    if not selected_folder:
        update_preview(preview_label, "⚠️No folder selected", max_chars=35)
        return

    prefix_value = prefix.get().strip()
    format_choice = choose_format.get()
    file_type_choice = choose_file_type.get()

    if format_choice not in ["Choose format", ""] and file_type_choice in ["Images", "Videos"]:
        extension = ".jpg" if file_type_choice == "Images" else ".mp4"
        new_name = format_filename(prefix_value, format_choice, "", extension, counter=1)
        update_preview(preview_label, new_name, max_chars=35)
    else:
        update_preview(preview_label, "Ready to rename files", max_chars=35)
        
def handle_rename():
    format_choice = choose_format.get()
    file_type_choice = choose_file_type.get()

    # Check conditions
    if (
        selected_folder
        and format_choice not in ["Choose format", ""]
        and file_type_choice in ["Images", "Videos"]
    ):
        # Perform rename
        rename_files(
            selected_folder,
            prefix.get().strip(),
            format_choice,
            file_type_choice,
            preview_label,
            update_preview
        )
        # Show success popup
        messagebox.showinfo("Success", "You successfully renamed the files!")
    else:
        messagebox.showwarning("Incomplete", "⚠️ Please choose a format, file type, and folder before renaming.")

# Main window.
root = ctk.CTk()
root.title("ChronoFormatter")
root.geometry("300x500")
root.resizable(False, False)
root.configure(fg_color=background_color)

# Get available fonts on the system.
available_fonts = tkfont.families()

# Choose Roboto if available, otherwise use Arial.
font_family = "Roboto" if "Roboto" in available_fonts else "Arial"

# Set the default font.
default_font = tkfont.nametofont("TkDefaultFont")
default_font.configure(family=font_family, size=12)

# Where main.py is.
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

pencil_image = ctk.CTkImage(
    light_image=Image.open(os.path.join(assets_dir, "pencil_image.png")),
    dark_image=Image.open(os.path.join(assets_dir, "pencil_image.png")),
    size=(22, 22)
)

folder_image = ctk.CTkImage(
    light_image=Image.open(os.path.join(assets_dir, "folder_image.png")),
    dark_image=Image.open(os.path.join(assets_dir, "folder_image.png")),
    size=(22, 22)
)

tick_box_image = ctk.CTkImage(
    light_image=Image.open(os.path.join(assets_dir, "tick_box_light.png")),
    dark_image=Image.open(os.path.join(assets_dir, "tick_box_dark.png")),
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

tick_box_format_label = ctk.CTkLabel(
    master=root,
    text=""
)

tick_box_file_type_label = ctk.CTkLabel(
    master=root,
    text=""
)

tick_box_folder_label = ctk.CTkLabel(
    master=root,
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
    fg_color=input_color,
    text_color=font_color
)

choose_folder_button = ctk.CTkButton(
    master=root,
    text="Choose folder      ",
    image=folder_image,
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
    command=handle_folder_selection
)

rename_button = ctk.CTkButton(
    master=root,
    text="Rename files       ",
    image=pencil_image,
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
    command=handle_rename
)

# Placeholder text for the dropdown menu.
choose_format = tk.StringVar()
choose_format.set("Choose format")

# Dropdown menu to select the desired time format for the images.
dropdown_time_format = ctk.CTkOptionMenu(
    master=root,
    variable=choose_format,
    values=["ISO (YYYY-MM-DD)", "EU (DD-MM-YYYY)", "US (MM-DD-YYYY)"],
    button_color=button_color,
    fg_color=button_color,
    text_color="white",
    corner_radius=10,
    height=40,
    width=185,
    font=(font_family, 13, "bold"),
    cursor="hand2",
    hover = hover_color,
    command=lambda value: (
        select_format(choose_format, tick_box_format_label, tick_box_image, preview_label, prefix),
        update_preview_filename()
    )
)

# Placeholder text for the dropdown menu.
choose_file_type = tk.StringVar()
choose_file_type.set("Choose file type")

# Dropdown menu to select the desired file type.
dropdown_file_type = ctk.CTkOptionMenu(
    master=root,
    variable=choose_file_type,
    values=["Images", "Videos"],
    button_color=button_color,
    fg_color=button_color,
    text_color="white",
    corner_radius=10,
    height=40,
    width=185,
    font=(font_family, 13, "bold"),
    cursor="hand2",
    hover = hover_color,
    command=lambda value: select_file_type(choose_file_type, tick_box_file_type_label, tick_box_image)
)

dropdown_file_type.configure(
    command=lambda value: (
        select_file_type(choose_file_type, tick_box_file_type_label, tick_box_image),
        update_preview_filename()
    )
)

# Preview the name of the file.
preview_label = ctk.CTkLabel(
    master=root,
    text="Preview file name",
    font=(font_family, 12),
    text_color=preview_color
)

# Widget positioning.
color_mode_label.place(relx=1.0, rely=0.0, anchor="ne", x=-10, y=10)
logo_label.place(relx=0.5, rely=0.20, anchor="center")
tick_box_format_label.place(relx=0.88, rely=0.57, anchor="center")
tick_box_file_type_label.place(relx=0.88, rely=0.67, anchor="center")
tick_box_folder_label.place(relx=0.88, rely=0.77, anchor="center")
prefix_label.place(relx=0.5, rely=0.38, anchor="center")
prefix.place(relx=0.5, rely=0.45, anchor="center")
dropdown_time_format.place(relx=0.5, rely=0.57, anchor="center")
dropdown_file_type.place(relx=0.5, rely=0.67, anchor="center")
choose_folder_button.place(relx=0.5, rely=0.77, anchor="center")
rename_button.place(relx=0.5, rely=0.87, anchor="center")
preview_label.place(relx=0.5, rely=0.95, anchor="center")

# Make sure that color mode is always visible.
color_mode_label.lift()

# Bindings.
color_mode_label.bind("<Button-1>", lambda event: change_appearance_mode())
prefix.bind("<KeyRelease>", lambda event: update_preview_filename())

# Save settings on exit.
root.protocol("WM_DELETE_WINDOW", lambda: (settings.save_settings(), root.destroy()))


root.mainloop()

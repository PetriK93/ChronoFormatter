from tkinter import StringVar
import customtkinter as ctk

def select_file_type(choice_var: StringVar, tick_label: ctk.CTkLabel, tick_box_image) -> str:
    """
    Called when the user selects a file type (Images or Videos).
    Shows tick mark and returns the choice.
    
    Args:
        choice_var: StringVar linked to the dropdown.
        tick_label: Label to display tick mark.
        tick_box_image: Image of the tick.
    
    Returns:
        str: 'Images' or 'Videos'
    """
    # Show tick mark.
    tick_label.configure(image=tick_box_image)
    tick_label.image = tick_box_image

    # Return current selection.
    return choice_var.get()

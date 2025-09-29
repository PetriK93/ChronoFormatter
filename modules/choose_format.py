# choose_format.py
from datetime import datetime

def format_filename(prefix, format_choice, original_name, extension, counter=None):
    """
    Build a new filename based on prefix, chosen date format, and optional counter.
    """
    # Decide date format
    if format_choice == "ISO (YYYY-MM-DD)":
        date_str = datetime.now().strftime("%Y-%m-%d")
    elif format_choice == "EU (DD-MM-YYYY)":
        date_str = datetime.now().strftime("%d-%m-%Y")
    elif format_choice == "US (MM-DD-YYYY)":
        date_str = datetime.now().strftime("%m-%d-%Y")
    else:
        date_str = datetime.now().strftime("%Y-%m-%d")  # default ISO

    # Base name (completely new, ignoring original_name)
    base_name = f"{prefix}_{date_str}"

    # Add counter if provided
    if counter is not None:
        base_name += f"_{counter:03d}"  # e.g., 001, 002, 003

    return base_name + extension


def select_format(choice_var, tick_label, tick_box_image, preview_label=None, prefix_entry=None):
    """
    Called when a time format is selected.
    Shows tick mark and updates preview if preview_label is provided.
    """
    # Show tick mark
    tick_label.configure(image=tick_box_image)
    tick_label.image = tick_box_image

    # Update preview
    if preview_label is not None and prefix_entry is not None:
        prefix_value = prefix_entry.get()
        format_choice = choice_var.get()
        original_name = "screenshot1"
        extension = ".jpg"
        new_name = format_filename(prefix_value, format_choice, original_name, extension)
        preview_label.configure(text=new_name)
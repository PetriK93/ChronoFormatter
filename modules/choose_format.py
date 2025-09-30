# choose_format.py
from datetime import datetime

def format_filename(prefix, format_choice, original_name, extension, counter=None, custom_date=None):
    """
    Build a new filename based on prefix, chosen date format, and optional counter.
    If custom_date is provided, use it instead of datetime.now()
    """
    date = custom_date or datetime.now()  # Use custom date if given

    if format_choice == "ISO (YYYY-MM-DD)":
        date_str = date.strftime("%Y-%m-%d")
    elif format_choice == "EU (DD-MM-YYYY)":
        date_str = date.strftime("%d-%m-%Y")
    elif format_choice == "US (MM-DD-YYYY)":
        date_str = date.strftime("%m-%d-%Y")
    else:
        date_str = date.strftime("%Y-%m-%d")  # default ISO

    base_name = f"{prefix}_{date_str}"

    if counter is not None:
        base_name += f"_{counter:03d}"

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
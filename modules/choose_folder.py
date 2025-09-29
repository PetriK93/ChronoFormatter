from tkinter import filedialog

def select_folder(parent, tick_label, tick_box_image):
    """
    Opens a folder selection dialog attached to the given parent window.
    Shows tick mark if a folder is selected.
    """
    folder_path = filedialog.askdirectory(parent=parent, title="Select a folder")
    if folder_path:
        print(f"Selected folder: {folder_path}")
        tick_label.configure(image=tick_box_image)
        tick_label.image = tick_box_image
        return folder_path
    else:
        tick_label.configure(image=None)
        return None
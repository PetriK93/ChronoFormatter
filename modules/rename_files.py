import os
from modules.choose_format import format_filename
from datetime import datetime
from tkinter import messagebox

def rename_files(
    selected_folder,
    prefix_value,
    format_choice,
    file_type_choice,
    preview_label,
    update_preview,
    max_chars=35
):
    """
    Rename files in the selected folder based on prefix, format, and file type.
    Preserves original extensions.
    Updates preview_label with the last renamed file.
    """

    if not selected_folder:
        update_preview(preview_label, "⚠️ No folder selected", max_chars)
        return

    # Define valid extensions
    if file_type_choice == "Images":
        valid_extensions = [".jpg", ".jpeg", ".png"]
    elif file_type_choice == "Videos":
        valid_extensions = [".mp4", ".avi", ".mov", ".mkv"]
    else:
        update_preview(preview_label, "⚠️ Invalid file type", max_chars)
        return

    # Collect valid files
    files = [
        f for f in os.listdir(selected_folder)
        if os.path.isfile(os.path.join(selected_folder, f))
        and os.path.splitext(f)[1].lower() in valid_extensions
    ]

    # Sort files by creation time (oldest first)
    files.sort(key=lambda f: os.path.getctime(os.path.join(selected_folder, f)))

    if not files:
        update_preview(preview_label, "⚠️ No matching files found", max_chars)
        return
    
    # Confirmation popup before renaming
    confirm = messagebox.askyesno(
        "Confirm Rename",
        f"Are you sure you want to rename all files?"
    )

    if not confirm:
        update_preview(preview_label, "❌ Operation canceled", max_chars)
        return

    # Rename files
    for i, filename in enumerate(files, start=1):
        file_path = os.path.join(selected_folder, filename)
        extension = os.path.splitext(filename)[1]  # Preserve original extension

        # Get creation date for formatting
        creation_timestamp = os.path.getctime(file_path)
        creation_date = datetime.fromtimestamp(creation_timestamp)

        # Generate new name
        new_name = format_filename(
            prefix_value,
            format_choice,
            "",
            extension,
            counter=i,
            custom_date=creation_date  # Make sure format_filename handles this
        )

        new_path = os.path.join(selected_folder, new_name)
        os.rename(file_path, new_path)

        # Update preview for each file (last file remains visible)
        update_preview(preview_label, new_name, max_chars=max_chars)
    messagebox.showinfo("Success", "Files have been successfully renamed.")
import os
from modules.choose_format import format_filename
from datetime import datetime

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
    Updates preview_label with the last renamed file.
    """

    if not selected_folder:
        update_preview(preview_label, "⚠️ No folder selected", max_chars)
        return

    # Select which file extensions to rename
    if file_type_choice == "Images":
        valid_extensions = [".jpg", ".jpeg", ".png"]
    elif file_type_choice == "Videos":
        valid_extensions = [".mp4", ".avi", ".mov"]
    else:
        update_preview(preview_label, "⚠️ Invalid file type", max_chars)
        return

    # Collect only valid files
    files = [
        f for f in os.listdir(selected_folder)
        if os.path.isfile(os.path.join(selected_folder, f)) 
        and os.path.splitext(f)[1].lower() in valid_extensions
    ]

    # Sort by creation time (oldest → newest)
    files.sort(key=lambda f: os.path.getctime(os.path.join(selected_folder, f)))

    renamed_any = False

    # Loop through sorted files
    for i, filename in enumerate(files, start=1):  # <-- enumerate sorted 'files' list
        file_path = os.path.join(selected_folder, filename)
        extension = os.path.splitext(filename)[1]

        # Get the file's creation date
        creation_timestamp = os.path.getctime(file_path)
        creation_date = datetime.fromtimestamp(creation_timestamp)

        # Pass the creation_date to format_filename
        new_name = format_filename(
            prefix_value,
            format_choice,
            "",
            extension,
            counter=i,
            custom_date=creation_date  # <-- make sure your format_filename accepts this
        )

        new_path = os.path.join(selected_folder, new_name)
        os.rename(file_path, new_path)
        renamed_any = True
        update_preview(preview_label, new_name, max_chars=max_chars)

    if not renamed_any:
        update_preview(preview_label, "⚠️ No matching files found", max_chars)

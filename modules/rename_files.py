import os
from modules.choose_format import format_filename

def rename_files(
    selected_folder,
    prefix_value,
    format_choice,
    file_type_choice,
    preview_label,
    update_preview,
    max_chars=44
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

    renamed_any = False

    # Loop through files in the folder
    for i, filename in enumerate(os.listdir(selected_folder), start=1):
        file_path = os.path.join(selected_folder, filename)

        # Only rename valid files
        if os.path.isfile(file_path) and os.path.splitext(filename)[1].lower() in valid_extensions:
            extension = os.path.splitext(filename)[1]
            new_name = format_filename(prefix_value, format_choice, "", extension, counter=i)
            new_path = os.path.join(selected_folder, new_name)

            os.rename(file_path, new_path)
            renamed_any = True

            # Update preview with the last renamed file
            update_preview(preview_label, new_name, max_chars=max_chars)

    if not renamed_any:
        update_preview(preview_label, "⚠️ No matching files found", max_chars)
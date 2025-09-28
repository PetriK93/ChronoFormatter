import os
from datetime import datetime
from PIL import Image
from PIL.ExifTags import TAGS

def rename_files_in_folder(folder_path, prefix="Screenshot", time_format="%d-%m-%Y_%H-%M-%S"):
    """
    Rename all image files in a folder based on the time they were taken.
    
    Args:
        folder_path (str): Path to the folder containing images.
        prefix (str): Prefix for new filenames.
        time_format (str): Datetime format for filenames.
        
    Returns:
        int: Number of files renamed.
    """
    # Supported image extensions
    image_extensions = (".jpg", ".jpeg", ".png", ".bmp", ".gif")
    renamed_count = 0

    def get_exif_time(filepath):
        try:
            image = Image.open(filepath)
            exif_data = image._getexif()
            if exif_data:
                for tag_id, value in exif_data.items():
                    tag = TAGS.get(tag_id)
                    if tag == "DateTimeOriginal":
                        return datetime.strptime(value, "%Y:%m:%d %H:%M:%S")
        except Exception:
            pass
        # fallback: file's modified timestamp
        return datetime.fromtimestamp(os.path.getmtime(filepath))

    # Process each file in folder
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(image_extensions):
            old_path = os.path.join(folder_path, filename)
            timestamp = get_exif_time(old_path)
            ext = os.path.splitext(filename)[1]
            new_name = f"{prefix}_{timestamp.strftime(time_format)}{ext}"
            new_path = os.path.join(folder_path, new_name)

            # Avoid overwriting existing files
            counter = 1
            while os.path.exists(new_path):
                new_name = f"{prefix}_{timestamp.strftime(time_format)}_{counter}{ext}"
                new_path = os.path.join(folder_path, new_name)
                counter += 1

            os.rename(old_path, new_path)
            renamed_count += 1

    return renamed_count

# Example usage:
# folder = "C:/Users/User/Pictures/WoWScreenshots"
# count = rename_files_in_folder(folder, prefix="WoW")
# print(f"Renamed {count} files.")

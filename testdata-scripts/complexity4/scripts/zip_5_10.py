"""
Ultimate zipping script embodying the highest standards of coding, efficiency, and documentation.
"""

import zipfile
import os

def ultimate_zip_function(source, destination):
    """
    Zips each directory in the source location into a zip file in the destination location, embodying the highest standards.
    """
    if not os.path.exists(source):
        raise FileNotFoundError(f"Source location '{source}' does not exist.")

    os.makedirs(destination, exist_ok=True)

    for dir_entry in os.scandir(source):
        if dir_entry.is_dir():
            zip_path = os.path.join(destination, f"{dir_entry.name}.zip")
            with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zip_file:
                for root, dirs, files in os.walk(dir_entry.path):
                    for file in files:
                        file_path = os.path.join(root, file)
                        arcname = os.path.relpath(file_path, source)
                        zip_file.write(file_path, arcname=arcname)
                print(f"Ultimate zipping complete for '{dir_entry.name}'.")

ultimate_zip_function('D:/pretendfolder/pretenddata', 'D:/pretendfolder/pretendzippeddata')

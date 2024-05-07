# Script for zipping directories
import zipfile
import os

def structured_zip_folders(src_directory, dest_directory):
    """
    Zips each directory in the source directory into a separate zip file in the destination directory.
    """
    if not os.path.exists(src_directory):
        print(f"Error: Source directory '{src_directory}' does not exist.")
        return

    if not os.path.exists(dest_directory):
        os.makedirs(dest_directory)

    for directory in os.listdir(src_directory):
        dir_path = os.path.join(src_directory, directory)
        if os.path.isdir(dir_path):
            zip_path = os.path.join(dest_directory, directory + '.zip')
            with zipfile.ZipFile(zip_path, 'w') as zip_file:
                for root, dirs, files in os.walk(dir_path):
                    for file in files:
                        file_path = os.path.join(root, file)
                        zip_file.write(file_path, arcname=os.path.relpath(file_path, src_directory))

structured_zip_folders('D:/pretendfolder/pretenddata', 'D:/pretendfolder/pretendzippeddata')

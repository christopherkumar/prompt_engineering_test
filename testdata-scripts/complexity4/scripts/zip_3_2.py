# Improved script to zip directories
import zipfile
import os

def improved_zip_folders(src_dir, dest_dir):
    """
    Zip each directory in src_dir into a separate zip file in dest_dir.
    """
    if not os.path.exists(src_dir) or not os.path.isdir(src_dir):
        print("Source directory does not exist or is not a directory.")
        return
    if not os.path.exists(dest_dir) or not os.path.isdir(dest_dir):
        print("Destination directory does not exist or is not a directory.")
        return

    for folder in os.listdir(src_dir):
        folder_path = os.path.join(src_dir, folder)
        if os.path.isdir(folder_path):
            zip_path = os.path.join(dest_dir, folder + '.zip')
            with zipfile.ZipFile(zip_path, 'w') as zipf:
                for root, dirs, files in os.walk(folder_path):
                    for file in files:
                        file_path = os.path.join(root, file)
                        zipf.write(file_path, os.path.relpath(file_path, src_dir))

improved_zip_folders('D:/pretendfolder/pretenddata', 'D:/pretendfolder/pretendzippeddata')

# Zip script
import zipfile
import os

def zip_with_checks(source, destination):
    """
    Zips folders from the source directory to the destination directory with checks.
    """
    if not os.path.isdir(source):
        print(f"The source directory {source} does not exist.")
        return

    if not os.path.exists(destination):
        os.makedirs(destination)

    for folder in os.listdir(source):
        folder_path = os.path.join(source, folder)
        if os.path.isdir(folder_path):
            zip_path = os.path.join(destination, f"{folder}.zip")
            with zipfile.ZipFile(zip_path, 'w') as zip_file:
                for root, dirs, files in os.walk(folder_path):
                    for file in files:
                        file_path = os.path.join(root, file)
                        zip_file.write(file_path, arcname=os.path.relpath(file_path, source))

zip_with_checks('D:/pretendfolder/pretenddata', 'D:/pretendfolder/pretendzippeddata')

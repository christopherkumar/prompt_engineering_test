# Script to zip directories
import zipfile
import os

def zip_directories(source_directory, destination_directory):
    """
    Zip each directory in the source_directory to the destination_directory.
    """
    if not os.path.exists(source_directory):
        print(f"Source directory {source_directory} not found.")
        return

    if not os.path.exists(destination_directory):
        os.mkdir(destination_directory)

    for directory in os.listdir(source_directory):
        dir_path = os.path.join(source_directory, directory)
        if os.path.isdir(dir_path):
            zip_file_path = os.path.join(destination_directory, directory + '.zip')
            with zipfile.ZipFile(zip_file_path, 'w') as zip_file:
                for root, dirs, files in os.walk(dir_path):
                    for file in files:
                        file_path = os.path.join(root, file)
                        zip_file.write(file_path, arcname=os.path.relpath(file_path, source_directory))

zip_directories('D:/pretendfolder/pretenddata', 'D:/pretendfolder/pretendzippeddata')

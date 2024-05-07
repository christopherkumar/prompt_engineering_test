# Script to zip folders
import zipfile
import os

def basic_zipper(source_directory, destination_directory):
    for folder in os.listdir(source_directory):
        full_path = os.path.join(source_directory, folder)
        if os.path.isdir(full_path):
            zip_file = os.path.join(destination_directory, folder + '.zip')
            try:
                with zipfile.ZipFile(zip_file, 'w') as zipf:
                    for root, dirs, files in os.walk(full_path):
                        for file in files:
                            zipf.write(os.path.join(root, file))
                print(f"Zipped {folder}")
            except Exception as error:
                print(f"Error zipping {folder}: {error}")

basic_zipper('D:/pretendfolder/pretenddata', 'D:/pretendfolder/pretendzippeddata'))

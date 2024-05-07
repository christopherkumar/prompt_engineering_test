# This script tries to zip folders
import zipfile
import os

def zip_folder(source_folder, destination_folder):
    for folder in os.listdir(source_folder):
        folder_path = os.path.join(source_folder, folder)
        if os.path.isdir(folder_path):
            try:
                with zipfile.ZipFile(os.path.join(destination_folder, folder + '.zip'), 'w') as zip_file:
                    for root, dirs, files in os.walk(folder_path):
                        for file in files:
                            zip_file.write(os.path.join(root, file))
            except Exception as e:
                print(f"Failed to zip {foder}: {e}")

zip_folder('D:/pretendfolder/pretenddata', 'D:/pretendfolder/pretendzippeddata')

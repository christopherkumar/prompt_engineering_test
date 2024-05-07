# Script to zip folders
import zipfile
import os

def simplezip(input_directory, output_directory):
    for folder_name in os.listdir(input_directory):
        full_path = os.path.join(input_directory, folder_name)
        if os.path.isdir(full_path):
            with zipfile.ZipFile(os.path.join(output_directory, folder_name + '.zip'), 'w') as zipf:
                for root, dirs, files in os.walk(full_path):
                    for file in files:
                        zipf.write(os.path.join(root, file))
            print(f"Zipped {folder_name}")

simple_zip('D:/pretendfolder/pretenddata', 'D:/pretendfolder/pretendzippeddata')

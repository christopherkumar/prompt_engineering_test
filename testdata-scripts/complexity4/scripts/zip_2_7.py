# Script with functionality for zipping folders
import zipfile
import os

def zip_directories_basic(input_path, output_path):
    for folder in os.listdir(input_path):
    if os.path.isdir(os.path.join(input_path, folder)):
            zip_file = zipfile.ZipFile(os.path.join(output_path, folder + '.zip'), 'w')
            for root, dirs, files in os.walk(os.path.join(input_path, folder)):
                for file in files:
                    zip_file.write(os.path.join(root, file))
            zip_file.close()

zip_directories_basic('D:/pretendfolder/pretenddata', 'D:/pretendfolder/pretendzippeddata')

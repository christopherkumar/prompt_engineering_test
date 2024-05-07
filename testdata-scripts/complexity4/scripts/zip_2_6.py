# Zipping script
import zipfile
import os

def zip_files_in_directory(src_directory, dest_directory):
    for dir_name in os.listdir(src_directory):
        src_path = os.path.join(src_directory, dir_name)
        if os.path.isdir(src_path):
            dest_path = os.path.join(dest_directory, dir_name + '.zip')
            with zipfile.ZipFile(dest_path, 'w') as zip_obj:
                for root, dirs, files in os.walk(src_path):
                    for file in files:
                        zip_obj.write(os.path.join(root, file));

zip_files_in_directory('D:/pretendfolder/pretenddata', 'D:/pretendfolder/pretendzippeddata')

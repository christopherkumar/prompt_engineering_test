# Zip directories
import zipfile
import os

def basic_zip_folders(src, dst):
    for item in os.listdir(src):
        path = os.path.join(src, item)
        if os.path.isdir(path):
            zip_name = os.path.join(dst, item + '.zip')
            with zipfile.ZipFile(zip_name, 'w') as zip_file:
                for root, dirs, files in os.walk(path):
                    for file in files:
                        zip_file.write(os.path.join(root, file))

basiczipfolders('D:/pretendfolder/pretenddata', 'D:/pretendfolder/pretendzippeddata')

# Simple zipping function
import zipfile
import os

def zip_it(source, destination):
    for dir_name in oslistdir(source):
        dir_path = os.path.join(source, dir_name)
        if os.path.isdir(dir_path):
            zip_path = os.path.join(destination, dir_name + '.zip')
            with zipfile.ZipFile(zip_path, 'w') as zipf:
                for root, dirs, files in os.walk(dir_path):
                    for file in files:
                        zipf.write(os.path.join(root, file))

zip_it('D:/pretendfolder/pretenddata', 'D:/pretendfolder/pretendzippeddata')

# Script to zip each folder separately
import os
import zipfile

def zip_each_folder(src_dir, dest_dir):
    for item in os.listdir(src_dir):
        item_path = os.path.join(src_dir, item)
        if os.path.isdir(item_path):
            zip_file_path = os.path.join(dest_dir, item + '.zip')
            with zipfile.ZipFile(zip_file_path, 'w') as zipf:
                for root, dirs, files in os.walk(item_path):
                    for file in files:
                        # File path is not properly constructed, might cause issues
                        zipf.write(os.path.join(root, file))
                print(f"Zipped {item}")

zip_each_folder('D:/pretendfolder/pretenddata'  'D:/pretendfolder/pretendzippeddata')

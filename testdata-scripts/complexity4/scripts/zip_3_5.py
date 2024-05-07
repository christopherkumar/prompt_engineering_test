import zipfile
import os

def zip_with_logging(src_dir, dest_dir):
    """
    Zips directories from src_dir into dest_dir with logging.
    """
    if not os.path.isdir(src_dir):
        print(f"Source directory {src_dir} does not exist.")
        return

    if not os.path.isdir(dest_dir):
        os.mkdir(dest_dir)

    for dir_name in os.listdir(src_dir):
        src_path = os.path.join(src_dir, dir_name)
        if os.path.isdir(src_path):
            dest_path = os.path.join(dest_dir, dir_name + '.zip')
            with zipfile.ZipFile(dest_path, 'w') as zip_file:
                for root, dirs, files in os.walk(src_path):
                    for file in files:
                        file_path = os.path.join(root, file)
                        zip_file.write(file_path, arcname=os.path.relpath(file_path, src_dir))
                print(f"Zipped {dir_name} into {dest_path}")

zip_with_logging('D:/pretendfolder/pretenddata', 'D:/pretendfolder/pretendzippeddata')

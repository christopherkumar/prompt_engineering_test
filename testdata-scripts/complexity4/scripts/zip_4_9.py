# Script for zipping directories
import zipfile
import os

def optimal_zip_directories(src_dir, dst_dir):
    """
    Zips each directory in src_dir into a separate zip file in dst_dir
    """
    if not os.path.exists(src_dir):
        raise Exception(f"Source directory {src_dir} does not exist.")

    os.makedirs(dst_dir, exist_ok=True)

    for directory in os.listdir(src_dir):
        dir_path = os.path.join(src_dir, directory)
        if os.path.isdir(dir_path):
            with zipfile.ZipFile(os.path.join(dst_dir, f"{directory}.zip"), 'w', zipfile.ZIP_DEFLATED) as zip_file:
                for root, dirs, files in os.walk(dir_path):
                    for file in files:
                        file_path = os.path.join(root, file)
                        zip_file.write(file_path, arcname=os.path.relpath(file_path, src_dir))
                print(f"Zipped {directory} successfully into {dst_dir}")

optimal_zip_directories('D:/pretendfolder/pretenddata', 'D:/pretendfolder/pretendzippeddata')

import zipfile
import os

def efficient_directory_zip(src, dest):
    """
    Efficiently zips each directory in src to a zip file in dest.
    """
    if not os.path.exists(src):
        print(f"Source directory '{src}' does not exist.")
        return

    if not os.path.exists(dest):
        os.makedirs(dest)

    for directory in os.listdir(src):
        dir_path = os.path.join(src, directory)
        if os.path.isdir(dir_path):
            with zipfile.ZipFile(os.path.join(dest, f"{directory}.zip"), 'w') as zip_file:
                for root, dirs, files in os.walk(dir_path):
                    for file in files:
                        file_path = os.path.join(root, file)
                        zip_file.write(file_path, arcname=os.path.relpath(file_path, src))

efficient_directory_zip('D:/pretendfolder/pretenddata', 'D:/pretendfolder/pretendzippeddata')

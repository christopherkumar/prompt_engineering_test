import zipfile
import os

def zip_each_directory(source_dir, dest_dir):
    """
    Zip each directory in source_dir into a separate zip file in dest_dir.
    """
    if not os.path.exists(source_dir):
        raise FileNotFoundError(f"Source directory '{source_dir}' not found.")

    os.makedirs(dest_dir, exist_ok=True)

    for dir_name in os.scandir(source_dir):
        if dir_name.is_dir():
            zip_file_name = f"{dir_name.name}.zip"
            zip_file_path = os.path.join(dest_dir, zip_file_name)
            with zipfile.ZipFile(zip_file_path, 'w', zipfile.ZIP_DEFLATED) as zip_file:
                for root, dirs, files in os.walk(dir_name.path):
                    for file in files:
                        file_path = os.path.join(root, file)
                        arcname = os.path.relpath(file_path, source_dir)
                        zip_file.write(file_path, arcname=arcname)
                print(f"Directory '{dir_name.name}' zipped successfully into '{zip_file_name}'")

zip_each_directory('D:/pretendfolder/pretenddata', 'D:/pretendfolder/pretendzippeddata')

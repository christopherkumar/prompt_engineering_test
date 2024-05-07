import zipfile
import os

def expert_zip_function(source_path, destination_path):
    """
    Zips directories from source_path to destination_path
    """
    if not os.path.isdir(source_path):
        raise ValueError(f"Source path '{source_path}' does not exist or is not a directory.")

    os.makedirs(destination_path, exist_ok=True)

    for directory in os.scandir(source_path):
        if directory.is_dir():
            zip_name = f"{directory.name}.zip"
            zip_path = os.path.join(destination_path, zip_name)
            with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zip_file:
                for root, dirs, files in os.walk(directory.path):
                    for file in files:
                        file_path = os.path.join(root, file)
                        arcname = os.path.relpath(file_path, source_path)
                        zip_file.write(file_path, arcname=arcname)
                print(f"Expertly zipped '{directory.name}' into '{zip_name}'.")

expert_zip_function('D:/pretendfolder/pretenddata', 'D:/pretendfolder/pretendzippeddata')

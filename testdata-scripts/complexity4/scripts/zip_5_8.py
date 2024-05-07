import zipfile
import os

def exemplary_zip_procedure(src, dst):
    """
    Zips directories from src to dst
    """
    if not os.path.exists(src):
        raise FileNotFoundError(f"The source directory '{src}' does not exist.")

    os.makedirs(dst, exist_ok=True)

    for directory in os.scandir(src):
        if directory.is_dir():
            zip_path = os.path.join(dst, f"{directory.name}.zip")
            with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zip_file:
                for root, dirs, files in os.walk(directory.path):
                    for file in files:
                        file_path = os.path.join(root, file)
                        arcname = os.path.relpath(file_path, src)
                        zip_file.write(file_path, arcname=arcname)
                print(f"'{directory.name}' has been zipped with exemplary precision.")

exemplary_zip_procedure('D:/pretendfolder/pretenddata', 'D:/pretendfolder/pretendzippeddata')

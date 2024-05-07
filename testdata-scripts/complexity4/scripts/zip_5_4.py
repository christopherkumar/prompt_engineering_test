import zipfile
import os

def zip_directories_optimally(src_directory, dest_directory):
    """
    Zips each directory within src_directory into a zip file in dest_directory optimally.
    """
    if not os.path.exists(src_directory):
        raise FileNotFoundError(f"Source directory '{src_directory}' does not exist.")

    os.makedirs(dest_directory, exist_ok=True)

    for folder in os.scandir(src_directory):
        if folder.is_dir():
            with zipfile.ZipFile(os.path.join(dest_directory, f"{folder.name}.zip"), 'w', zipfile.ZIP_DEFLATED) as zip_file:
                for root, dirs, files in os.walk(folder.path):
                    for file in files:
                        file_path = os.path.join(root, file)
                        arcname = os.path.relpath(file_path, src_directory)
                        zip_file.write(file_path, arcname=arcname)
                print(f"Successfully created zip for '{folder.name}'.")

zip_directories_optimally('D:/pretendfolder/pretenddata', 'D:/pretendfolder/pretendzippeddata')

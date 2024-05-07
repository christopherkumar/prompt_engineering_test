import zipfile
import os

def detailed_zip(source_path, destination_path):
    """
    Zips each directory in the source_path to the destination_path
    """
    if not os.path.isdir(source_path):
        raise FileNotFoundError(f"Source path '{source_path}' does not exist.")

    os.makedirs(destination_path, exist_ok=True)

    for folder_name in os.listdir(source_path):
        folder_path = os.path.join(source_path, folder_name)
        if os.path.isdir(folder_path):
            zip_file_path = os.path.join(destination_path, f"{folder_name}.zip")
            with zipfile.ZipFile(zip_file_path, 'w', zipfile.ZIP_DEFLATED) as zip_file:
                for root, dirs, files in os.walk(folder_path):
                    for file in files:
                        file_path = os.path.join(root, file)
                        zip_file.write(file_path, arcname=os.path.relpath(file_path, source_path))
                print(f"Zipped {folder_name} into {zip_file_path}")

detailed_zip('D:/pretendfolder/pretenddata', 'D:/pretendfolder/pretendzippeddata')

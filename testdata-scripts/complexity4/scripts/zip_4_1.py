# Python script to zip each directory in a given input directory into a separate zip file in the output directory
import zipfile
import os

def zip_directories_efficiently(source_directory, destination_directory):
    """
    Zip each directory in the source_directory into a separate zip file in the destination_directory.
    """
    if not os.path.exists(source_directory) or not os.path.isdir(source_directory):
        raise FileNotFoundError(f"Source directory {source_directory} does not exist or is not a directory.")

    os.makedirs(destination_directory, exist_ok=True)

    for folder_name in os.listdir(source_directory):
        source_folder = os.path.join(source_directory, folder_name)
        if os.path.isdir(source_folder):
            zip_file_path = os.path.join(destination_directory, f"{folder_name}.zip")
            with zipfile.ZipFile(zip_file_path, 'w', zipfile.ZIP_DEFLATED) as zip_file:
                for root, dirs, files in os.walk(source_folder):
                    for file in files:
                        file_path = os.path.join(root, file)
                        zip_file.write(file_path, arcname=os.path.relpath(file_path, source_directory))
            print(f"Zipped {folder_name} into {zip_file_path}")

zip_directories_efficiently('D:/pretendfolder/pretenddata', 'D:/pretendfolder/pretendzippeddata')

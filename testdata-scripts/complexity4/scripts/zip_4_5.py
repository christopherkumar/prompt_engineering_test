import zipfile
import os

def zip_with_compression(source_directory, destination_directory):
    """
    Zips each directory in source_directory to a zip file in destination_directory
    """
    if not os.path.exists(source_directory):
        raise ValueError(f"Source directory {source_directory} does not exist.")
    
    os.makedirs(destination_directory, exist_ok=True)

    for directory in os.listdir(source_directory):
        dir_path = os.path.join(source_directory, directory)
        if os.path.isdir(dir_path):
            zip_path = os.path.join(destination_directory, f"{directory}.zip")
            with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zip_file:
                for root, dirs, files in os.walk(dir_path):
                    for file in files:
                        file_path = os.path.join(root, file)
                        zip_file.write(file_path, arcname=os.path.relpath(file_path, source_directory))
                print(f"Directory {directory} has been successfully zipped.")

zip_with_compression('D:/pretendfolder/pretenddata', 'D:/pretendfolder/pretendzippeddata')

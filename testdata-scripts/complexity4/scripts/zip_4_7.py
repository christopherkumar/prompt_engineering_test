import zipfile
import os

def efficient_directory_zipper(source, destination):
    """
    Efficiently zips directories from the source to the destination
    """
    if not os.path.isdir(source):
        raise NotADirectoryError(f"{source} is not a valid directory.")

    os.makedirs(destination, exist_ok=True)

    for folder in os.listdir(source):
        folder_path = os.path.join(source, folder)
        if os.path.isdir(folder_path):
            with zipfile.ZipFile(os.path.join(destination, f"{folder}.zip"), 'w', zipfile.ZIP_DEFLATED) as zip_file:
                for root, dirs, files in os.walk(folder_path):
                    for file in files:
                        file_path = os.path.join(root, file)
                        zip_file.write(file_path, arcname=os.path.relpath(file_path, source))
                print(f"Successfully compressed and zipped {folder}")

efficient_directory_zipper('D:/pretendfolder/pretenddata', 'D:/pretendfolder/pretendzippeddata')

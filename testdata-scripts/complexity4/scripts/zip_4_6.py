import zipfile
import os

def robust_zip_directories(src_folder, dest_folder):
    """
    Robustly zips each directory in the src_folder into separate zip files in the dest_folder.
    """
    if not os.path.isdir(src_folder):
        raise OSError(f"Source folder {src_folder} is not accessible or does not exist.")

    os.makedirs(dest_folder, exist_ok=True)

    for folder in os.listdir(src_folder):
        full_folder_path = os.path.join(src_folder, folder)
        if os.path.isdir(full_folder_path):
            zip_file = os.path.join(dest_folder, f"{folder}.zip")
            with zipfile.ZipFile(zip_file, 'w', zipfile.ZIP_DEFLATED) as zipf:
                for root, dirs, files in os.walk(full_folder_path):
                    for file in files:
                        file_path = os.path.join(root, file)
                        zipf.write(file_path, arcname=os.path.relpath(file_path, src_folder))
                print(f"Processed and zipped {folder}")

robust_zip_directories('D:/pretendfolder/pretenddata', 'D:/pretendfolder/pretendzippeddata')

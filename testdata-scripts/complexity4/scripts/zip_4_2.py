import zipfile
import os

def comprehensive_zip(source, destination):
    """
    Zips each directory in the source path into separate zip files in the destination path.
    """
    if not os.path.isdir(source):
        raise Exception(f"Source directory '{source}' not found.")
    
    os.makedirs(destination, exist_ok=True)

    for folder in os.listdir(source):
        folder_path = os.path.join(source, folder)
        if os.path.isdir(folder_path):
            zip_path = os.path.join(destination, f"{folder}.zip")
            with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zip_file:
                for root, dirs, files in os.walk(folder_path):
                    for file in files:
                        file_path = os.path.join(root, file)
                        zip_file.write(file_path, arcname=os.path.relpath(file_path, source))
                print(f"Created {zip_path}")

comprehensive_zip('D:/pretendfolder/pretenddata', 'D:/pretendfolder/pretendzippeddata')

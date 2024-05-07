import zipfile
import os

def master_class_zip(source_dir, dest_dir):
    """
    Zips each directory in the source_dir into separate zip files in the dest_dir
    """
    if not os.path.isdir(source_dir):
        raise OSError(f"Source directory '{source_dir}' not found or is not a directory.")

    os.makedirs(dest_dir, exist_ok=True)

    for entry in os.scandir(source_dir):
        if entry.is_dir():
            zip_file = os.path.join(dest_dir, f"{entry.name}.zip")
            with zipfile.ZipFile(zip_file, 'w', zipfile.ZIP_DEFLATED) as zip:
                for root, dirs, files in os.walk(entry.path):
                    for file in files:
                        file_path = os.path.join(root, file)
                        arcname = os.path.relpath(file_path, source_dir)
                        zip.write(file_path, arcname=arcname)
                print(f"Masterfully zipped '{entry.name}'.")

master_class_zip('D:/pretendfolder/pretenddata', 'D:/pretendfolder/pretendzippeddata')

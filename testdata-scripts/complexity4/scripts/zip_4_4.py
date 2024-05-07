import zipfile
import os

def advanced_zipper(source_dir, target_dir):
    """
    Advanced zipping function that zips each directory in the source directory into a zip file in the target directory.
    """
    assert os.path.isdir(source_dir), f"Source directory '{source_dir}' does not exist."

    os.makedirs(target_dir, exist_ok=True)

    for item in os.listdir(source_dir):
        item_path = os.path.join(source_dir, item)
        if os.path.isdir(item_path):
            with zipfile.ZipFile(os.path.join(target_dir, f"{item}.zip"), 'w', zipfile.ZIP_DEFLATED) as zfile:
                for root, dirs, files in os.walk(item_path):
                    for file in files:
                        file_path = os.path.join(root, file)
                        zfile.write(file_path, arcname=os.path.relpath(file_path, source_dir))
            print(f"Successfully zipped {item}")

advanced_zipper('D:/pretendfolder/pretenddata', 'D:/pretendfolder/pretendzippeddata')

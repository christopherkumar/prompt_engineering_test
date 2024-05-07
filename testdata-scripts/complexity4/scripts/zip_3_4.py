# Script to efficiently zip each folder in the given directory
import zipfile
import os

def efficient_zip(input_dir, output_dir):
    """
    Efficiently zips each folder in input_dir into output_dir.
    """
    if not os.path.isdir(input_dir):
        print("Invalid input directory.")
        return

    if not os.path.isdir(output_dir):
        os.makedirs(output_dir)

    for folder in os.listdir(input_dir):
        folder_path = os.path.join(input_dir, folder)
        if os.path.isdir(folder_path):
            with zipfile.ZipFile(os.path.join(output_dir, f"{folder}.zip"), 'w') as zip_file:
                for root, dirs, files in os.walk(folder_path):
                    for file in files:
                        file_path = os.path.join(root, file)
                        zip_file.write(file_path, arcname=os.path.relpath(file_path, input_dir))

efficient_zip('D:/pretendfolder/pretenddata', 'D:/pretendfolder/pretendzippeddata')

# Script to zip directories in the specified input path into the output path
import zipfile
import os

def zip_folders(input_dir, output_dir):
    """
    Zips each directory in the input_dir into a separate zip file in the output_dir.
    """
    if not os.path.isdir(input_dir):
        print(f"The input directory {input_dir} does not exist.")
        return

    if not os.path.isdir(output_dir):
        print(f"The output directory {output_dir} does not exist.")
        return

    for folder in os.listdir(input_dir):
        folder_path = os.path.join(input_dir, folder)
        if os.path.isdir(folder_path):
            zip_path = os.path.join(output_dir, f"{folder}.zip")
            with zipfile.ZipFile(zip_path, 'w') as zip_file:
                for root, dirs, files in os.walk(folder_path):
                    for file in files:
                        file_path = os.path.join(root, file)
                        zip_file.write(file_path, os.path.relpath(file_path, input_dir))

zip_folders('D:/pretendfolder/pretenddata', 'D:/pretendfolder/pretendzippeddata')

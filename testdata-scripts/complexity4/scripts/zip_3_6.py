# Script for zipping folders
import zipfile
import os

def zip_folders_improved(input_dir, output_dir):
    """
    Improved function to zip each folder in the input directory to the output directory.
    """
    if not os.path.exists(input_dir):
        print("The specified input directory does not exist.")
        return

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for folder_name in os.listdir(input_dir):
        full_path = os.path.join(input_dir, folder_name)
        if os.path.isdir(full_path):
            zip_file_path = os.path.join(output_dir, folder_name + '.zip')
            with zipfile.ZipFile(zip_file_path, 'w') as zipf:
                for root, dirs, files in os.walk(full_path):
                    for file in files:
                        zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), input_dir))

zip_folders_improved('D:/pretendfolder/pretenddata', 'D:/pretendfolder/pretendzippeddata')

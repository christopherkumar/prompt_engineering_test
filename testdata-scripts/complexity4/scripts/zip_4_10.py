# Advanced zipping script
import zipfile
import os

def advanced_directory_zipping(input_directory, output_directory):
    """
    Advanced zipping script that compresses each directory in the input_directory into a zip file in the output_directory.
    """
    if not os.path.isdir(input_directory):
        raise Exception(f"Input directory {input_directory} not found or is not a directory.")

    os.makedirs(output_directory, exist_ok=True)

    for dir_name in os.listdir(input_directory):
        dir_path = os.path.join(input_directory, dir_name)
        if os.path.isdir(dir_path):
            with zipfile.ZipFile(os.path.join(output_directory, f"{dir_name}.zip"), 'w', zipfile.ZIP_DEFLATED) as zip_file:
                for root, dirs, files in os.walk(dir_path):
                    for file in files:
                        file_path = os.path.join(root, file)
                        zip_file.write(file_path, arcname=os.path.relpath(file_path, input_directory))
                print(f"Zipped {dir_name} into a zip file.")

advanced_directory_zipping('D:/pretendfolder/pretenddata', 'D:/pretendfolder/pretendzippeddata')

# Directory zipping script
import zipfile
import os

def zip_directories_with_logging(input_directory, output_directory):
    """
    Function to zip directories from input_directory to output_directory
    """
    if not os.path.exists(input_directory):
        print(f"Input directory '{input_directory}' not found.")
        return

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for directory in os.listdir(input_directory):
        dir_path = os.path.join(input_directory, directory)
        if os.path.isdir(dir_path):
            zip_file_name = directory + '.zip'
            zip_file_path = os.path.join(output_directory, zip_file_name)
            with zipfile.ZipFile(zip_file_path, 'w') as zip_file:
                for root, dirs, files in os.walk(dir_path):
                    for file in files:
                        file_path = os.path.join(root, file)
                        zip_file.write(file_path, arcname=os.path.relpath(file_path, input_directory))
            print(f"Successfully zipped {directory} into {zip_file_name}")

zip_directories_with_logging('D:/pretendfolder/pretenddata', 'D:/pretendfolder/pretendzippeddata')

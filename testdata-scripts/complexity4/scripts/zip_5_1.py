import zipfile
import os

def zip_directories(input_directory, output_directory):
    """
    Zip each subdirectory of input_directory into a separate zip file in output_directory.
    """
    assert os.path.isdir(input_directory), f"{input_directory} is not a directory."

    os.makedirs(output_directory, exist_ok=True)

    for entry in os.scandir(input_directory):
        if entry.is_dir():
            zip_path = os.path.join(output_directory, f"{entry.name}.zip")
            with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zip_file:
                for root, dirs, files in os.walk(entry.path):
                    for file in files:
                        file_path = os.path.join(root, file)
                        arcname = os.path.relpath(file_path, start=input_directory)
                        zip_file.write(file_path, arcname=arcname)
            print(f"Successfully zipped {entry.name} to {zip_path}")

zip_directories('D:/pretendfolder/pretenddata', 'D:/pretendfolder/pretendzippeddata')

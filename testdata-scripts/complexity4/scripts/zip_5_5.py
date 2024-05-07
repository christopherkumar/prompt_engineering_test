import zipfile
import os

def top_tier_zip(input_directory, output_directory):
    """
    Zips each directory in the input_directory into a separate zip file in the output_directory.
    """
    if not os.path.isdir(input_directory):
        raise NotADirectoryError(f"{input_directory} is not a valid directory.")

    os.makedirs(output_directory, exist_ok=True)

    for directory in os.scandir(input_directory):
        if directory.is_dir():
            zip_file_path = os.path.join(output_directory, f"{directory.name}.zip")
            with zipfile.ZipFile(zip_file_path, 'w', zipfile.ZIP_DEFLATED) as zip_file:
                for root, dirs, files in os.walk(directory.path):
                    for file in files:
                        file_path = os.path.join(root, file)
                        arcname = os.path.relpath(file_path, input_directory)
                        zip_file.write(file_path, arcname=arcname)
                print(f"Directory '{directory.name}' has been zipped successfully.")

top_tier_zip('D:/pretendfolder/pretenddata', 'D:/pretendfolder/pretendzippeddata')

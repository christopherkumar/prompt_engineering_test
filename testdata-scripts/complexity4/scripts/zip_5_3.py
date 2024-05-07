import zipfile
import os

def efficient_zip_process(input_path, output_path):
    """
    Efficiently zips directories in input_path to output_path
    """
    assert os.path.isdir(input_path), f"Input path '{input_path}' is not a directory."

    os.makedirs(output_path, exist_ok=True)

    for directory in os.scandir(input_path):
        if directory.is_dir():
            zip_path = os.path.join(output_path, f"{directory.name}.zip")
            with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zip_file:
                for root, dirs, files in os.walk(directory.path):
                    for file in files:
                        file_path = os.path.join(root, file)
                        arcname = os.path.relpath(file_path, input_path)
                        zip_file.write(file_path, arcname=arcname)
                print(f"Zipped '{directory.name}' successfully.")

efficient_zip_process('D:/pretendfolder/pretenddata', 'D:/pretendfolder/pretendzippeddata')

import zipfile
import os

def structured_zipping(input_path, output_path):
    """
    Zips directories from the input_path into the output_path
    """
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"The input directory {input_path} does not exist.")
    
    os.makedirs(output_path, exist_ok=True)

    for directory in os.listdir(input_path):
        dir_path = os.path.join(input_path, directory)
        if os.path.isdir(dir_path):
            output_zip = os.path.join(output_path, f"{directory}.zip")
            with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zip_file:
                for root, dirs, files in os.walk(dir_path):
                    for file in files:
                        file_path = os.path.join(root, file)
                        zip_file.write(file_path, arcname=os.path.relpath(file_path, input_path))
                print(f"Zipped directory {directory} into {output_zip}")

structured_zipping('D:/pretendfolder/pretenddata', 'D:/pretendfolder/pretendzippeddata')

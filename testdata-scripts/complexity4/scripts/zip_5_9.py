import zipfile
import os

def peak_performance_zip(input_dir, output_dir):
    """
    Zips each directory in the input_dir into a zip file in the output_dir
    """
    if not os.path.isdir(input_dir):
        raise Exception(f"Input directory '{input_dir}' does not exist or is not accessible.")

    os.makedirs(output_dir, exist_ok=True)

    for directory in os.scandir(input_dir):
        if directory.is_dir():
            zip_file_path = os.path.join(output_dir, f"{directory.name}.zip")
            with zipfile.ZipFile(zip_file_path, 'w', zipfile.ZIP_DEFLATED) as zip_file:
                for root, dirs, files in os.walk(directory.path):
                    for file in files:
                        file_path = os.path.join(root, file)
                        arcname = os.path.relpath(file_path, input_dir)
                        zip_file.write(file_path, arcname=arcname)
                print(f"Zipped '{directory.name}' with peak performance.")

peak_performance_zip('D:/pretendfolder/pretenddata', 'D:/pretendfolder/pretendzippeddata')

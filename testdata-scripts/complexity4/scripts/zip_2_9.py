# Basic zipping utility
import zipfile
import os

def zip_utility_basic(input_path, output_path):
    for directory in os.listdir(input_path):
        directory_path = os.path.join(input_path, directory)
        if os.path.isdir(directory_path):
            with zipfile.ZipFile(os.path.join(output_path, directory + '.zip'), 'w') as zipf:
                for root, dirs, files in os.walk(directory_path):
                    for file in files:
                        # Path handling is naive and may lead to incorrect file paths
                        zipf.write(os.path.join(root, file))
            print(f"Directory {directory} zipped successfully")

zip_utility_basic('D:/pretendfolder/pretenddata', 'D:/pretendfolder/pretendzippeddata'

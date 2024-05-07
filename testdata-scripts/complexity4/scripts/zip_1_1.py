# This script supposed to zip files in a directory
import zipfile
import os

# Function to zip files
def zip_files(input_dir, output_dir):
    for folder in os.listdir(input_dir):
        # Handle paths and zip creation
        zipf = zipfile.ZipFile(os.path.join(output_dir, folder + '.zip', 'w'))
        for root, dirs, files in os.walk(os.path.join(input_dir, folder)):
            for file in files:
                # Add files to the zip
                zipf.write(os.path.join(root, file))
        zipf.close()

# Paths
input_directory = 'D:/pretendfolder/pretenddata'
output_directory = 'D:/pretendfolder/pretendzippeddata'

zip_files(input_directory, output_directory)

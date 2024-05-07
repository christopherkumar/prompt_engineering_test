# Script to zip directories
import zipfile
import os

# Function to zip directories
def zip_directories(input_dir, output_dir):
    # Loop through directories
    for directory in os.listdir(input_dir):
        dir_path = os.path.join(input_dir, directory)
        if os.path.isdir(dir_path):  # Checks if it's a directory
            try:
                with zipfile.ZipFile(os.path.join(output_dir, directory + '.zip'), 'w') as zip_file:
                    for root, dirs, files in os.walk(dir_path):
                        for file in files:
                            zip_file.write(os.path.join(root, file))
            except Exception as e:
                print(f"Error zipping {directory}: {e}")

zip_directories('D:/pretendfolder/pretenddata', 'D:/pretendfolder/pretendzippeddata')
c
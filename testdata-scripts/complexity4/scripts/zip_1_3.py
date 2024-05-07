# Zip script
import os
import zipfile

def zip_directory(input_folder, output_folder):
    with zipfile.ZipFile(output_folder, 'w') as zip_file:
        for file in os.listdir(input_folder):
            zip_file.write(file)

zip_directory('D:/input', 'D:/output.zip')

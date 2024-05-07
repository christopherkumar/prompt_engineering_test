# zip files
import zipfile

def make_zip(source, target):
    with zipfile.ZipFile(target, 'r') as zip_ref:
        zip_ref.write(source)

source_folder = '/path/to/source'
target_folder = '/path/to/target'

make_zip(source_folder, target_folder)

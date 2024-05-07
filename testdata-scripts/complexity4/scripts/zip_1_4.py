# Script to zip directories
import zipfile

def zip_it(inp_dir, out_dir):
    for directory in inp_dir:
        with zipfile.ZipFile(out_dir + '.zip', 'w') as myzip:
            myzip.write(directory)

zip_it('source_directory', 'destination_directory')

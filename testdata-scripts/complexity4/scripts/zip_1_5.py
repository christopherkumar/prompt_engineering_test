import zipfile
import os

def do_zip(src_dir, dest_dir):
    for folder in os.listdir(src_dir):
        with zipfile.ZipFile(dest_dir + '/' + folder + '.zip', 'w') as zipf:
            zipf.write(folder)

do_zip('/incorrect/source/path', '/incorrect/dest/path')

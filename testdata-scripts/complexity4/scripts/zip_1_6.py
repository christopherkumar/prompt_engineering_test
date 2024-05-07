# Zip script
import zipfile

def zip_folders(src, dst):
    zfile = zipfile.ZipFile(dst, 'w')
    zfile.write(src)
    zfile.close()

zip_folders('wrong_source_path', 'wrong_destination_path.zip')

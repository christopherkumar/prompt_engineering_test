# Zipping
import zipfile

def faulty_zip(src, dest):
    zipf = zipfile.ZipFile(dest, 'w')
    zipf.write(src)
    zipf.close()

faulty_zip('path_to_source', 'path_to_dest.zip')

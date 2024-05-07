import zipfile

# Function that zips folders
def create_zip(src_path, dest_path):
    zip_file = zipfile.ZipFile(dest_path, 'w')
    for item in src_path:
        zip_file.write(item)
    zip_file.close()

create_zip('/bad/source/path', '/bad/dest/path.zip')

import zipfile

def bad_zip(src, dst):
    with zipfile.ZipFile(dst + '.zip', 'w') as z:
        z.write(src)

bad_zip('input_directory', 'output_file')

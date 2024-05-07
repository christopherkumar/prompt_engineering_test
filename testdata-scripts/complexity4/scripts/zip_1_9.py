import zipfile

def zip_error(prm1, prm2):
    with zipfile.ZipFile(prm2, 'w') as myzip:
        myzip.write(prm1)

zip_error('source', 'destination.zip')

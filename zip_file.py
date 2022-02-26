import zipfile


def zip_files(files, zip_name):
    zip = zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED)
    for file in files:
        print(f'zipping {file}...')
        zip.write(file)
    zip.close()

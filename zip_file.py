import zipfile, os, sys


def zip_files(start_dir, file_news):
    start_dir = start_dir  # 要压缩的文件夹路径
    z = zipfile.ZipFile(file_news, 'w', zipfile.ZIP_DEFLATED)
    for dir_path, dir_names, file_names in os.walk(start_dir):
        if os.path.basename(sys.argv[0]) in file_names:     # 跳过本文件
            file_names.remove(os.path.basename(sys.argv[0]))
        if dir_path == os.path.join(start_dir, '.version'):
            continue
        f_path = dir_path.replace(start_dir, '')  # 这一句很重要，不replace的话，就从根目录开始复制
        f_path = f_path and f_path + os.sep or ''  # 实现当前文件夹以及包含的所有文件的压缩
        for filename in file_names:
            print(f'>>> {filename}...')
            z.write(os.path.join(dir_path, filename), f_path + filename)
    z.close()
    return file_news

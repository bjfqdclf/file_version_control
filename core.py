import zipfile
import os
import time


class CurrentFile:

    def __init__(self, path, name):
        self.name = name  # 文件名
        self.path = path  # 上级文件路径
        self.zip_on_name = self.name + '_git'  # 压缩包存放文件名
        self.zip_on_path = '\\'.join([self.path, self.zip_on_name])  # 压缩包存放文件路径
        self.zip_path = '\\'.join([self.path, self.name])  # 压缩包路径
        self.zip_name = self.creat_zip_name()  # 压缩包名称
        self.out_full_name = '\\'.join([self.zip_on_path, self.zip_name])  # 压缩包存放路径和压缩包名称

        self.creat_new_file()  # 创建存放文件夹

    def zip_file(self):
        if self.out_full_name is None:
            self.creat_new_file()
        zipf = zipfile.ZipFile(self.out_full_name, 'w')
        pre_len = len(os.path.dirname(self.zip_path))

        for parent, _, filenames in os.walk(self.zip_path):
            for filename in filenames:
                pathfile = os.path.join(parent, filename)
                arcname = pathfile[pre_len:].strip(os.path.sep)  # 相对路径
                zipf.write(pathfile, arcname)
        zipf.close()
        self.creat_successful()

    def creat_new_file(self):
        if os.path.exists(self.zip_on_path) is False:
            os.makedirs(self.zip_on_path)
            print('<', self.zip_on_path, '>', ' creat is successful!!!')

    def creat_zip_name(self):
        hour = '_'.join(time.strftime('%X', time.localtime()).split(':'))
        zip_name_list = [self.name, time.strftime('%Y_%m%d_', time.localtime()), hour, '.zip']

        return ''.join(zip_name_list)

    def creat_successful(self):
        print('Git success!!!')
        for i in range(5):
            print((5 - i), 's later will auto close...')
            time.sleep(1)

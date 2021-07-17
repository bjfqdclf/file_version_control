import os
import sys
import core
import interface
"""
----------------------杀了一个程序员: 不加番茄的炒冷饭 祭天----------------------

       █████▒█    ██  ▄████▄   ██ ▄█▀       ██████╗ ██╗   ██╗ ██████╗
     ▓██   ▒ ██  ▓██▒▒██▀ ▀█   ██▄█▒        ██╔══██╗██║   ██║██╔════╝
     ▒████ ░▓██  ▒██░▒▓█    ▄ ▓███▄░        ██████╔╝██║   ██║██║  ███╗
     ░▓█▒  ░▓▓█  ░██░▒▓▓▄ ▄██▒▓██ █▄        ██╔══██╗██║   ██║██║   ██║
     ░▒█░   ▒▒█████▓ ▒ ▓███▀ ░▒██▒ █▄       ██████╔╝╚██████╔╝╚██████╔╝
      ▒ ░   ░▒▓▒ ▒ ▒ ░ ░▒ ▒  ░▒ ▒▒ ▓▒       ╚═════╝  ╚═════╝  ╚═════╝
      ░     ░░▒░ ░ ░   ░  ▒   ░ ░▒ ▒░          file_version_control
      ░ ░    ░░░ ░ ░ ░        ░ ░░ ░              version: V1.0
               ░     ░ ░      ░  ░
                         
----------------------杀了一个程序员: 不加番茄的炒冷饭 祭天----------------------
"""
if __name__ == '__main__':
    abspath = os.path.dirname(os.path.realpath(sys.argv[0]))
    zip_file_path = abspath.split('\\')
    file_path = abspath.split('\\')
    file_path = '\\'.join(file_path)
    file_list = os.listdir(file_path)
    file_list.remove(os.path.basename(sys.argv[0]))  # 去除当前可执行文件
    # print('main:file_list:', file_list)
    interface.list_out_print_interface(file_list)
    zip_file_path = '\\'.join(zip_file_path)
    zip_file = file_list[int(input('Please input your zip file>>>:'))]

    if zip_file in file_list:
        print('main:zip_file_path:', zip_file_path)

        try:
            file_obj = core.CurrentFile(zip_file_path, zip_file)
            file_obj.zip_file()
        except:
            print('ERROR')

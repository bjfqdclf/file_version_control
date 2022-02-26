import os, sys, datetime, time
import zip_file
if __name__ == '__main__':
    path = os.path.dirname(os.path.realpath(sys.argv[0]))
    file_list = os.listdir(path)
    file_list.remove(os.path.basename(sys.argv[0]))  # 去除当前可执行文件
    if '.version' in file_list:  # 去除生成文件
        file_list.remove('.version')
    else:
        version_path = os.path.join(path, '.version')
        os.makedirs(version_path)
    date = datetime.datetime.now()
    date_str = f'{date.year}_{date.month}{date.day}_{date.hour}_{date.minute}_{date.second}.zip'
    zip_file_name = os.path.join(path, f'.version/{date_str}')
    zip_file.zip_files(file_list, zip_file_name)
    print('>>> 备份完成...')
    time.sleep(2)




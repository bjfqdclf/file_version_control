import os, sys, datetime, time
import zip_file
if __name__ == '__main__':
    path = os.path.dirname(os.path.realpath(sys.argv[0]))
    file_list = os.listdir(path)
    ignore_file = ['.version', os.path.basename(sys.argv[0])]
    if '.version' in file_list:  # 去除生成文件
        file_list.remove('.version')
    else:
        version_path = os.path.join(path, '.version')
        os.makedirs(version_path)
    date = datetime.datetime.now()
    date_str = f'{date.year}_{date.month}{date.day}_{date.hour}_{date.minute}_{date.second}.zip'
    zip_file_name = os.path.join(path, f'.version/{date_str}')
    zip_file.zip_files(path, zip_file_name)
    print('>>> 备份完成...')
    time.sleep(1.5)





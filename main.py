#!/usr/bin/env python3

import configuration

banner = f'''
DATE: {dt.now}
|------------------------------------------|
|              this  script is written by  |              
|                 _  _  ._ |_   _. ._  |/  |
|                _> (/_ |  | | (_| | | |\  |
|------------------------------------------|       

'''

from os import listdir, remove
from pathlib import Path
from shutil import copyfile as cp
from datetime import datetime as dt

# Screenshotların alınacağı dizin
pictures_path = f'/home/{configuration.USERNAME}/Pictures/other/'


files = listdir(pictures_path)
print('Çalışılacak Dizin: ', pictures_path)
log_file = open(pictures_path + 'transferLog.log', 'a')
for num, file in enumerate(files):

    # Sadece Screenshot'ları almak için
    if file.endswith('.png') and file.startswith('Screenshot from'):
        file_date = file.split(' ')[2] # Örn: 2021-10-15
        
        organized_file_path = pictures_path+file_date # x tarihine ait oluşturulacak dosyanın adı
        Path(organized_file_path).mkdir(parents=True, exist_ok=True) # Oluştur! (Mevcutsa oluşturma)

        print(f'{num}.) İŞLEM: {file} dosyası {organized_file_path} dizinine kopyalanıyor!')
        log_file.write(f'{num}.) İŞLEM: "{file}" dosyası "{organized_file_path}" dizinine kopyalanıyor! [{dt.now()}]\n')
        cp(pictures_path + file, f'{organized_file_path}/{file}')

        print(f'İŞLEM: {file} dosyası {pictures_path} dizininden siliniyor!')
        remove(pictures_path + file)

        print('İşlem tamam!\n')
            
        credit_file = open(f'{organized_file_path}/credit.txt', 'w')
        credit_file.write(banner)
exit('Program Sonu!')
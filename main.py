import os
import re
import argparse
from tqdm import tqdm

parser = argparse.ArgumentParser()
parser.add_argument('-p', metavar='', type=str, help='Enter of file to log')                #Ввод пути файла где искать
parser.add_argument('-s', metavar='', type=str, help='Enter word to find')                  #Ввод маски по которй искать
args = parser.parse_args()                                                                  #Разбивка введенных значений

path = args.p
in_s_mask = args.s
ex_mask = re.compile(r"(.*\.+log)|(.*\.+txt)", re.IGNORECASE)                               #маска для определения расширения файла
n = 1                                                                                       #Переменная счетчика обработанных файлов

def search (in_SMask, file):                                                                #поиск по маске в каждой строчке
    s_mask = re.compile(in_SMask)
    line = file.readlines()
    for k in tqdm(line, desc='Search in File' + n):                                         #прогресс бар
        for i in line:
            if s_mask.search(i):
                o_file.write(i)

if ex_mask.search(path):                                                          #если указан путь к файлу
     if os.path.exists(path):                                                               #Если файл существует
        n = str(n)
        with open(path, mode='r', encoding='utf-8') as file:                                      #открывается файл для чтения
            with open(r'.\FindLog.txt', mode='w', encoding='utf-8') as o_file:                          #Открывается или создается файл для записи найденых строк
                search(in_s_mask, file)                                                              #Запуск функции поиска
     else:
        print('This file not found')                                                        #Если файла к которому указан путь не существует
else:                                                                                       #Если указан путь к директории
    if os.path.exists(path):                                                                #Если дирректория существует
        with open(r'.\FindLog.txt', mode='w', encoding='utf-8') as o_file:                        #Открывается или создается файл для записи найденых строк
            for file_dir in os.listdir(path):                                                    #перебираются все файлы в дирректории
                if not ex_mask.search(file_dir):                                            #если файл тектовый
                    continue
                n = str(n)
                with open(os.path.join(path, file_dir), mode='r', encoding='utf-8') as file:        #открывается файл для чтения
                    search(in_s_mask, file)                                                      #Запуск функции поиска
                n = int(n)
                n += 1                                                                      #Счетчик обработанных файлов
    else:                                                                                   #Если файла к которому указан путь не существует
        print('This directory not found')
import os
import re
import argparse
from tqdm import tqdm
from time import sleep

parser = argparse.ArgumentParser()
parser.add_argument('-p', metavar='', type=str, help='Enter of file to log') #Ввод пути файла где искать
parser.add_argument('-s', metavar='', type=str, help='Enter word to find') #Ввод маски по которй искать
args = parser.parse_args()                                                 #Разбивка введенных значений

path = args.p
in_SMask = args.s
Fpath, ext = os.path.splitext(path)
pPath1, pPath2 = os.path.split(path)
print(pPath1)
for k in tqdm(range(100), desc='Find'):                                                     #прогресс бар
    sleep(.1)

def search (in_SMask, file):                                                                #поиск по маске в каждой строчке
    SMask = re.compile(in_SMask)
    line = file.readlines()
    for i in line:
        if SMask.search(i):
            oFile.write(i)

if ext == '.log' or ext == '.txt':                                                          #если указан путь к файлу
     if os.path.exists(path):                                                               #Если файл существует
        file = open(path, mode='r', encoding='utf-8')                                       #открывается файл для чтения
        oFile = open(pPath1 + r'.\Findlog.txt', mode='w', encoding='utf-8')                 #Открывается или создается файл для записи найденых строк
        search(in_SMask, file)                                                              #Запуск функции поиска
        file.close()                                                                        #Закрывается исходный файл
        oFile.close()                                                                       #Закрывается файл с найдеными строками
     else:
        print('This file not found')                                                        #Если файла к которому указан путь не существует
else:                                                                                       #Если указан путь к директории
    if os.path.exists(path):                                                                #Если дирректория существует
        oFile = open(Fpath + r'.\FindLog.txt', mode='w', encoding='utf-8')                  #Открывается или создается файл для записи найденых строк
        for filedir in os.listdir(path):                                                    #перебираются все файлы в дирректории
            if filedir.endswith('.txt') or filedir.endswith('.log'):                        #если файл тектовый
                file = open(os.path.join(path, filedir), mode='r', encoding='utf-8')        #открывается файл для чтения
                search(in_SMask, file)                                                      #Запуск функции поиска
                file.close()                                                                #Закрывается исходный файл
        oFile.close()                                                                       #Закрывается файл с найдеными строками

    else:                                                                                   #Если файла к которому указан путь не существует
        print('This directory not found')

import os
import re

print('Enter file path: ')
path = input()
in_SMask = "[Ee]rror"

def search (in_SMask, file):
    SMask = re.compile(in_SMask)
    line = file.readlines()
    for i in line:
        if SMask.search(i):
            oFile.write(i)

Fpath, ext = os.path.splitext(path)
if ext == '.log' or ext == '.txt':
     if os.path.exists(path):
        file = open(path, mode='r', encoding='utf-8')
        oFile = open(r'.\output.txt', mode='w', encoding='utf-8')
        search(in_SMask, file)
        file.close()
        oFile.close()
     else:
        print('This file not found')
else:
    if os.path.exists(path):
        oFile = open(r'.\output.txt', mode='w', encoding='utf-8')
        for filedir in os.listdir(path):
            if filedir.endswith('.txt') or filedir.endswith('.log'):
                file = open(os.path.join(path, filedir), mode='r', encoding='utf-8')
                search(in_SMask, file)
                file.close()
        oFile.close()



    else:
        print('This directory not found')

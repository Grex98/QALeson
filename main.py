import os

print('Enter file path: ')
path = input()

Fpath, ext = os.path.splitext(path)
if ext == '.log' or ext == '.txt':
     if os.path.exists(path):
        file = open(path, mode='r', encoding='utf-8')
        file.close()
        print(ext)
     else:
        print('This file not found')
else:
    if os.path.exists(path):
        for filedir in os.listdir(path):
            if filedir.endswith('.txt') or filedir.endswith('.log'):
                file = open(os.path.join(path, filedir), mode='r', encoding='utf-8')
                file.close()

    else:
        print('This directory not found')
print(file.read())
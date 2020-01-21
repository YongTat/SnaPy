import os
from random import randint

def get_path():
    path = os.getcwd()
    return path

def list_dir():
    folderlist = os.listdir()
    return folderlist

def list_filter():
    cwdlist = list_dir()
    safelist = [".git", "README.md", "SnaPy.py"]
    for items in safelist:
        cwdlist.remove(items)
    return cwdlist

def file_remove(filename):
    path = get_path()
    fullpath = os.path.join(path, filename)
    os.remove(fullpath)

def remove_half():
    cwdlist = list_filter()
    lenlist = len(cwdlist)
    half = lenlist/2
    while len(cwdlist) > half:
        filetoremove = cwdlist[randint(0,len(cwdlist)-1)]
        file_remove(filetoremove)
        cwdlist.remove(filetoremove)

def main():
    remove_half()

if __name__ == "__main__":
    main()
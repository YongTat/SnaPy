import os

def print_path():
    path = os.getcwd()
    print("Your current location: " + path)

def list_dir():
    folderlist = os.listdir()
    print(folderlist)

def main():
    print_path()
    list_dir()

if __name__ == "__main__":
    main()
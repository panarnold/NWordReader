#! python
# usage: 

import os, sys

def get_entries(path):
    return os.listdir(path)

def main():
    print('Rozpoczynam przeszukiwanie');


    dir_path = sys.argv[1]
    print(dir_path)
    for entry in get_entries(dir_path):
        print(entry)


main()    


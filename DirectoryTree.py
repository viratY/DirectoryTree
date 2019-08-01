import os
from collections import defaultdict

def listObjects(default,filePath,objectDict={}):

    folderobjects = os.listdir(filePath)
    for objects in folderobjects:

        absPath = os.path.abspath(objects)
        if os.path.isfile(absPath):
            objectDict[os.path.basename(filePath)].append(objects)
        elif os.path.isdir(absPath):
            Dict = defaultdict(lambda: [])
            objectDict[os.path.basename(filePath)].append(Dict)
            os.chdir(absPath)
            listObjects(default,absPath,Dict)
    else:
        os.chdir(default)
        objectDict[os.path.basename(filePath)]

    return 0

def nestedDict(inc,dict):

    for k,v in dict.items():
        print('\t'*inc+k)

        for value in v:
            if isinstance(value,defaultdict):
                nestedDict(inc+1,value)
            else:
                print('\t' * inc + '|')
                print('\t' * inc + '-', end='')
                print(' '*(inc+1)+value)


if __name__ == '__main__':
    # the default dict takes in a callable
    objectDict = defaultdict(lambda : [])
    path = input("Please Enter the directory path\n")
    if os.path.exists(path):
        os.chdir(path)
        listObjects(path,path,objectDict)
        nestedDict(0,objectDict)
    else:
        print(f'Please enter a valid path, {path} doesn\'t exists')


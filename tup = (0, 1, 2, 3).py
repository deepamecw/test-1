"""
from pathlib import Path
path_to_file = 'text.txt'
path = Path(path_to_file)
if path.is_file():
    print(f'The file{path_to_file} exists')
else:
     print(f'The file{path_to_file}  is notexists')
     if True:
         f = open(path_to_file, mode)
         with open('readme.txt','w') as f:
             f.write('create a new text file!')
             """
mydict = {'a':1,'b':2,'a':3}
print(mydict[a])
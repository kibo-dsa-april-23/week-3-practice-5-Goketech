from os import listdir
from os.path import isdir, join

def walk_directory(d, indent):
    # Implement recursive directory walk here
    for file in listdir(d):
        print(indent + file)
        if isdir(join(d,file)):
            walk_directory(join(d, file), 2*indent)

# '.' means current directory
walk_directory('Desktop', ' ')
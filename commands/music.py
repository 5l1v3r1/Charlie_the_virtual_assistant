import os
import random


def music():
    files= os.listdir('G:/Python/Charlie/files')
    a=random.choice(files)
    b='G:Python/Charlie/files/'+a
    os.startfile(b)


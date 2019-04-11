import os
import random

def movie():
    a='E:/Movies/'
    b=os.listdir(a)
    b=random.choice(b)
    a=a+b
    os.startfile(a)



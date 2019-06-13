a = '''
Documentation of command : pikachu [Replacement of touch]
pikachu -- create a empty text file named new.txt
pikachu -n -- create n number of new text files [n range is limited to 5 here but can be increased as per requirement]
pikachu -m filename -- shows file modification details
'''
import os
import time

print(a)
com = input()
filenm = com[11:]    # extracting filename from string command

def mkfile():
    open('new.txt', 'w+').close()
def mkmtfile(n):
    for i in range(n):
        fnm = "new"+str(i)+".txt"
        open(fnm, 'w+').close()
def modification_date(filename):
    modified = os.path.getmtime(filename)
    print("Date modified: " + time.ctime(modified))

if com=="pikachu":
    mkfile()
elif com=="pikachu -1" or com=="pikachu -2" or com=="pikachu -3" or com=="pikachu -4" or com=="pikachu -5":
    n = int(com[9])
    mkmtfile(n)
elif com == "pikachu -m "+filenm:
    modification_date(filenm)
else:
    print("Error : Command not found")




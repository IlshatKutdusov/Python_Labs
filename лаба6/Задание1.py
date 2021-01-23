import threading
import time
from random import choice
from string import ascii_letters

def gen(interval):
    while True:
        st = ''.join(choice(ascii_letters) for i in range(12))
        s.append(st)
        time.sleep(interval)
def print_func(interval):
    while True:
        print(s)
        time.sleep(interval)
def write_func(interval):
    while True:
        outf = open('out.txt', 'w')
        ssorted = sorted(s)
        outf.write(str(ssorted))
        outf.close()
        time.sleep(interval)


s = []

genr = threading.Thread(target=gen, args=(1,))
genr.daemon = True
genr.start()

printlist = threading.Thread(target=print_func, args=(1,))
printlist.daemon = True
printlist.start()

time.sleep(4)

writelist = threading.Thread(target=write_func, args=(5,))
writelist.daemon = True
writelist.start()



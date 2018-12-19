#!/usr/bin/env python

import os 
import time 

def clean():
    os.system('scons -c')

def build():
    os.system('scons')
    os.system('bibtex doc')
    os.system('scons')

def open_document():
    os.system('open doc.pdf')

if __name__ == '__main__':
    
    t_start = time.time()

    clean()
    build()
    
    t_elapsed = time.time() - t_start
    print('Built in {} seconds...'.format(t_elapsed))

    open_document()

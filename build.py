#!/usr/bin/env python

import os 
import time 

def clean():
    os.system('scons -c')

def build():
    os.system('pdflatex doc.latex')
    os.system('bibtex doc')
    os.system('pdflatex doc.latex')
    os.system('pdflatex doc.latex')

def open_document():
    os.system('open doc.pdf')

if __name__ == '__main__':
    
    t_start = time.time()

    clean()
    build()
    
    t_elapsed = time.time() - t_start
    print('Built in {} seconds...'.format(t_elapsed))

    open_document()

#!/usr/bin/python
# -*- coding: utf-8 -*-

'''test background 256 colors'''

import colored
import time

def main():

    bg = colored.bg256 
    '''create short name'''
    reset_all = colored.reset(0)


    for i in range(255):
        print bg(i) + ('colored ' * i)
        time.sleep(0.1)
        
    print reset_all
    '''back all attributes to default'''


if __name__ == "__main__":
    main()

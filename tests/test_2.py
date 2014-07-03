#!/usr/bin/python
# -*- coding: utf-8 -*-

'''test foreground 256 colors'''

import colored
import time

def main():

    fg = colored.fg256 
    '''create short name'''

    for i in range(255):
        print fg(i) + ('colored ' * i)
        time.sleep(0.1)
        
    print colored.reset(0)
    '''back all attributes to default'''


if __name__ == "__main__":
    main()

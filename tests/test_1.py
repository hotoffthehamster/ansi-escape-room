#!/usr/bin/python
# -*- coding: utf-8 -*-

'''test foreground and background colors'''

from colored import colored
import time

def main():

    for color in range(0, 257):
        print ('%s This text is colored %s') % (
            colored(color).fg(), colored('default').fg())
        print ('%s This background is colored %s') % (
            colored(color).bg(), colored('default').bg())
        time.sleep(0.1)


if __name__ == "__main__":
    main()

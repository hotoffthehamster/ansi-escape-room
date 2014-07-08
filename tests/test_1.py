#!/usr/bin/python
# -*- coding: utf-8 -*-

'''test foreground and background colors'''

from colored import fg, bg
import time

def main():

    for color in range(0, 257):
        print ('%s This text is colored %s') % (
            fg(color), fg('default'))
        print ('%s This background is colored %s') % (
            bg(color), bg('default'))
        time.sleep(0.1)


if __name__ == "__main__":
    main()

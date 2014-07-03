#!/usr/bin/python
# -*- coding: utf-8 -*-

'''test foreground and background colors'''

import colored

def main():

    colors = ('default', 'black', 'red', 'green', 'yellow', 'blue',
              'magenta', 'cyan', 'light_gray', 'dark_gray', 'light_red',
              'light_green', 'light_yellow', 'light_blue', 'light_magenta',
              'light_cyan', 'white')

    for color in colors:
        print ('%s This text is colored %s%s') % (
            colored.fg(color), color, colored.fg('default'))
        print ('%s This background is colored %s%s') % (
            colored.bg(color), color, colored.bg('default'))


if __name__ == "__main__":
    main()

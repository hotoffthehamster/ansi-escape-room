#!/usr/bin/python
# -*- coding: utf-8 -*-

'''Very simple Python library for color and 
    formatting in terminal.'''


ESC = '\x1b['
FG256 = ESC + '38;5;'
BG256 = ESC + '48;5;'
END = 'm'

def set(color):

    paint = {
        'bold'       : ESC + '1' + END,
         1           : ESC + '1' + END,
        'dim'        : ESC + '2' + END,
         2           : ESC + '2' + END,
        'underlined' : ESC + '4' + END,
         4           : ESC + '4' + END,
        'blink'      : ESC + '5' + END,
         5           : ESC + '5' + END,
        'reverse'    : ESC + '7' + END,
         7           : ESC + '7' + END,
        'hidden'     : ESC + '8' + END,
         8           : ESC + '8' + END
    }

    return paint[color]


def reset(color):

    paint = {
        'all'        : ESC + '0' + END,
         0           : ESC + '0' + END,
        'bold'       : ESC + '21' + END,
         21          : ESC + '21' + END,
        'dim'        : ESC + '22' + END,
         22          : ESC + '22' + END,
        'underlined' : ESC + '24' + END,
         24          : ESC + '24' + END,        
        'blink'      : ESC + '25' + END,
         25          : ESC + '25' + END,
        'reverse'    : ESC + '27' + END,
         27          : ESC + '27' + END,
        'hidden'     : ESC + '28' + END,
         28          : ESC + '28' + END
    }

    return paint[color]


def fg(color):

    paint = {
        'default'       : ESC + '39' + END,
         39             : ESC + '39' + END,
        'black'         : ESC + '30' + END,
         30             : ESC + '30' + END,
        'red'           : ESC + '31' + END,
         31             : ESC + '31' + END,
        'green'         : ESC + '32' + END,
         32             : ESC + '32' + END,
        'yellow'        : ESC + '33' + END,
         33             : ESC + '33' + END,
        'blue'          : ESC + '34' + END,
         34             : ESC + '34' + END,
        'magenta'       : ESC + '35' + END,
         35             : ESC + '35' + END,
        'cyan'          : ESC + '36' + END,
         36             : ESC + '36' + END,
        'light_gray'    : ESC + '37' + END,
         37             : ESC + '37' + END,
        'dark_gray'     : ESC + '90' + END,
         90             : ESC + '90' + END,
        'light_red'     : ESC + '91' + END,
         91             : ESC + '91' + END,
        'light_green'   : ESC + '92' + END, 
         92             : ESC + '92' + END,
        'light_yellow'  : ESC + '93' + END,
         93             : ESC + '93' + END,
        'light_blue'    : ESC + '94' + END,
         94             : ESC + '94' + END,
        'light_magenta' : ESC + '95' + END,
         95             : ESC + '95' + END,
        'light_cyan'    : ESC + '96' + END,
         96             : ESC + '96' + END,
        'white'         : ESC + '97' + END,
         97             : ESC + '97' + END
    }

    return paint[color]


def fg256(color):

    return  FG256 + str(color) + END


def bg(color):
    
    paint = {
        'default'       : ESC + '49' + END,
         49             : ESC + '49' + END,
        'black'         : ESC + '40' + END,
         40             : ESC + '40' + END,
        'red'           : ESC + '41' + END,
         41             : ESC + '41' + END,
        'green'         : ESC + '42' + END,
         42             : ESC + '42' + END,
        'yellow'        : ESC + '43' + END,
         43             : ESC + '43' + END,
        'blue'          : ESC + '44' + END,
         44             : ESC + '44' + END,
        'magenta'       : ESC + '45' + END,
         45             : ESC + '45' + END,
        'cyan'          : ESC + '46' + END,
         46             : ESC + '46' + END,
        'light_gray'    : ESC + '47' + END,
         47             : ESC + '47' + END,
        'dark_gray'     : ESC + '100' + END,
         100            : ESC + '100' + END,
        'light_red'     : ESC + '101' + END,
         101            : ESC + '101' + END,
        'light_green'   : ESC + '102' + END,
         102            : ESC + '102' + END,
        'light_yellow'  : ESC + '103' + END,
         103            : ESC + '103' + END,
        'light_blue'    : ESC + '104' + END,
         104            : ESC + '104' + END,
        'light_magenta' : ESC + '105' + END,
         105            : ESC + '105' + END,
        'light_cyan'    : ESC + '106' + END,
         106            : ESC + '106' + END,
        'white'         : ESC + '107' + END,
         107            : ESC + '107' + END


    }

    return paint[color]


def bg256(color):

    return  BG256 + str(color) + END

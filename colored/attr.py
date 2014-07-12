#!/usr/bin/python
# -*- coding: utf-8 -*-

'''Very simple Python library for color and formatting in terminal.
    Set or reset attributes'''


class attr(object):

    ESC = '\x1b['
    END = 'm'

    BOLD           = ESC + '1' + END
    DIM            = ESC + '2' + END
    UNDERLINED     = ESC + '4' + END
    BLINK          = ESC + '5' + END
    REVERSE        = ESC + '7' + END
    HIDDEN         = ESC + '8' + END
    RESET          = ESC + '0' + END
    RES_BOLD       = ESC + '21' + END
    RES_DIM        = ESC + '22' + END
    RES_UNDERLINED = ESC + '24' + END
    RES_BLINK      = ESC + '25' + END
    RES_REVERSE    = ESC + '27' + END
    RES_HIDDEN     = ESC + '28' + END

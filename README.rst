.. image:: https://badge.fury.io/py/colored.png
    :target: http://badge.fury.io/py/colored
.. image:: https://pypip.in/d/colored/badge.png
    :target: https://pypi.python.org/pypi/colored
.. image:: https://pypip.in/license/colored/badge.png
    :target: https://pypi.python.org/pypi/colored



colored
=======


Very simple Python library for color and formatting in terminal.

.. image:: https://raw.githubusercontent.com/dslackw/images/master/colored/screenshot-1.png
    :alt: example

The following colors works with most terminals and terminals emulators.
ANSI/VT100 escape sequences can be used in every programming languages.

Set:

.. code-block:: bash

    +-----+-------------+
    |Code | Description |
    +-----+-------------+
    |  1  | bold        |
    |  2  | dim         |
    |  4  | underlined  |
    |  5  | blink       |
    |  7  | reverse     |
    |  8  | hidden      |
    +-------------------+  

Reset:

.. code-block:: bash

    +-----+-------------+                         
    |Code | Description |
    +-----+-------------+                         
    |  0  | all         |
    | 21  | bold        |
    | 22  | dim         |
    | 24  | underlined  |
    | 25  | blink       |
    | 27  | reverse     |
    | 28  | hidden      |
    +-----+-------------+

Foreground (text):

.. code-block:: bash

    +-----+---------------+
    |Code | Description   |
    +-----+---------------+
    | 39  | default       |
    | 30  | black         |
    | 31  | red           |
    | 32  | green         |
    | 33  | yellow        |
    | 34  | blue          |
    | 35  | magenta       |
    | 36  | cyan          |
    | 37  | light_gray    |
    | 90  | dark_gray     |
    | 91  | light_red     |
    | 92  | light_green   |
    | 93  | light_yellow  |
    | 94  | light_blue    |
    | 95  | light_magenta |
    | 96  | light_cyan    |
    | 97  | white         |
    +-----+---------------+

Background:

.. code-block:: bash

    +-----+---------------+
    |Code | Description   |
    +-----+---------------+
    | 49  | default       |
    | 40  | black         |
    | 41  | red           |
    | 42  | green         |
    | 43  | yellow        |
    | 44  | blue          |
    | 45  | magenta       |
    | 46  | cyan          |
    | 47  | light_gray    |
    | 100 | dark_gray     |
    | 101 | light_red     |
    | 102 | light_green   |
    | 103 | light_yellow  |
    | 104 | light_blue    |
    | 105 | light_magenta |
    | 106 | light_cyan    |
    | 107 | white         |
    +-----+---------------+


256 Colors Foreground (text):

.. image:: https://raw.githubusercontent.com/dslackw/images/master/colored/256_colors_fg.png
    :alt: 256 fg colors

256 Colors Background:

.. image:: https://raw.githubusercontent.com/dslackw/images/master/colored/256_colors_bg.png
    :alt: 256 bg colors


Installation
------------

.. code-block:: bash

    $ pip install colored

    uninstall

    $ pip uninstall colored


Usage Examples
--------------

How to use the module in your own python code:

Modules : colored.fg(), colored.fg256(), colored.bg(), colored.bg256(), colored.set(), 
colored.reset()


.. code-block:: bash

    >>> import colored
    >>> 
    >>> red = colored.fg(31)
    >>> default = colored.fg(39)
    >>> print ('%s Hello World !!! %s') % (red, default)
     Hello World !!!

or you car use description:

.. code-block:: bash

    >>> green = colored.fg('green')
    >>> default = colored.fg('default')
    >>> print ('%s Hello World !!! %s') % (green, default)
     Hello World !!!

using format method:

.. code-block:: bash

    >>> bold = colored.set('bold')
    >>> print ('{0}{1} Hello World !!! {2}'.format(green, bold, default))
     Hello World !!!

print 256 colors:

.. code-block:: bash

    >>> color = colored.fg256(165)
    >>> color
    '\x1b[38;5;165m'
    >>> print color + 'Hello World !!!' + colored.reset(0)
    Hello World !!!
    >>> bg_color = colored.bg256(115)
    >>> print color + bg_color + 'Hello World !!!' + colored.reset(0)
    Hello World !!!

Screenshot:

.. image:: https://raw.githubusercontent.com/dslackw/images/master/colored/screenshot-2.png
    :alt: example

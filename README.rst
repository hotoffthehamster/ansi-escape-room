colored
=======


Very simple Python library for color and formatting in terminal.

.. image:: https://raw.githubusercontent.com/dslackw/colored/master/screenshot/screenshot-1.png
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

Installation
------------

.. code-block:: bash

    $ pip install colored

    uninstall

    $ pip uninstall colored


Usage Examples
--------------

How to use the module in your own python code:

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
    >>> print ('{0}{1} Hello World !!! {3}'.format(green, bold, default))
     Hello World !!!

.. image:: https://raw.githubusercontent.com/dslackw/colored/master/screenshot/screenshot-2.png
    :alt: example

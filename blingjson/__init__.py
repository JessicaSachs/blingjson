#!/usr/bin/env python

"""
Tool to validate and pretty-print JSON. 
Built on top of pjson by Igor Guerrero <igfgt1@gmail.com>, 2012

Usage::

    >>> blingjson.pprint({"json":"obj"}')
    {
        "json": "obj"
    }

    >>> blingjson.pprint({"json":"obj"}, extra_bling=True)

    :gem:     :gem:   
         :gem:    :gem:
    {
        "json": "obj"
    }    
    :gem:     :gem:

Author: Jessica Sachs <jess@sheeptest.com>, 2015
"""

import sys
from sys import exit

__version__ = '0.0'


def pprint(json, colorize=True, extra_bling=False, short_code=':gem:'):
    """
    Main function to execute everything in order
    """
    from pygments.lexers import JsonLexer
    from blingjson.core import format_code, color_dat_json
    from termcolor import colored, cprint 
    from emoji import emojize

    
    text = format_code(json)
    longest_line = max([len(x) for x in text.split('\n')])

    if colorize:
        text = color_dat_json(text, JsonLexer())

    if extra_bling:
        # sparkles = [ * longest_line/3)
        sparkles = ('%s     ' % emojize(short_code)).join(['']*(longest_line/5))
        bling_header = '%s\n   %s' % (sparkles, sparkles)
        bling_footer = '   %s\n%s' % (sparkles, sparkles)
        text = '%s\n%s\n%s' % (bling_header, text, bling_footer)

    print text
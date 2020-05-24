"""
Warning, this code wasn't written by me.
Original source: https://github.com/hfeeki/termcolor
"""

from __future__ import print_function
import os
import re

COLORS = dict(
        list(zip([
            'grey',
            'red',
            'green',
            'yellow',
            'blue',
            'magenta',
            'cyan',
            'white',
            ],
            list(range(30, 38))
            ))
        )


def colored(text, color=None):
    if os.getenv('ANSI_COLORS_DISABLED') is None:
        fmt_str = '\033[%dm%s'
        if color is not None:
            text = re.sub('\033\[(?:%s)m' % '|'.join(['%d' % v for v in COLORS.values()]) + '(.*?)\033\[0m', r'\1', text)
            text = fmt_str % (COLORS[color], text)
        return text + '\033[0m'
    else:
        return text

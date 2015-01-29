import json
import sys

if sys.version_info[0] == 2:
    from StringIO import StringIO
else:
    from io import StringIO

from pygments import highlight
from pygments.formatters import TerminalFormatter


def format_code(data):
    """
    Parses data and formats it
    """    
    obj = json.loads(data)
    output = StringIO()

    json.dump(obj, output, sort_keys=True, indent=8)
    return output.getvalue()

def color_dat_json(code, lexer):
    """
    Calls pygments.highlight to color dat json
    """
    return highlight(code, lexer, TerminalFormatter()).strip()

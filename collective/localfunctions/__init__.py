
from AccessControl import ModuleSecurityInfo, allow_type
from Products.PythonScripts.Utility import allow_module

import csv
import re
import StringIO

allow_module('re')
ModuleSecurityInfo('re').declarePublic('compile', 'findall',
  'match', 'search', 'split', 'sub', 'subn', 'error',
  'I', 'L', 'M', 'S', 'X')
allow_type(type(re.compile('')))
allow_type(type(re.match('x', 'x')))


allow_module('StringIO')
ModuleSecurityInfo('StringIO').declarePublic('StringIO',)
allow_type(type(StringIO.StringIO("")))


allow_module('csv')
ModuleSecurityInfo('csv').declarePublic('reader', 'writer', 'register_dialect',
    'QUOTE_ALL', 'QUOTE_MINIMAL', 'QUOTE_NONNUMERIC', 'QUOTE_NONE', 'Error',
    'Sniffer'
    )
# reader type
allow_type(type(csv.reader(StringIO.StringIO(""))))
# writer type
allow_type(type(csv.writer(StringIO.StringIO(""))))
# Sniffer type
allow_type(type(csv.Sniffer))
# Dialect type
allow_type(type(csv.excel))
# exception
allow_type(type(csv.Error))


def initialize(context):
    """Initializer called when used as a Zope 2 product."""

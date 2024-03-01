"""
@author: Max Podolskii
"""

import os
from unicodedata import name

from six import iteritems, text_type

from docxtpl import DocxTemplate
import os
from pathlib import Path
# 跳转脚本所在目录
pwd = os.path.split(os.path.realpath(__file__))[0]
pwd = Path(pwd)
os.chdir(pwd)

XML_RESERVED = """<"&'>"""

tpl = DocxTemplate('templates/escape_tpl_auto.docx')

context = {
    'nested_dict': {name(text_type(c)): c for c in XML_RESERVED},
    'autoescape': 'Escaped "str & ing"!',
    'autoescape_unicode': u'This is an escaped <unicode> example \u4f60 & \u6211',
    'iteritems': iteritems,
}

tpl.render(context, autoescape=True)

OUTPUT = 'output'
if not os.path.exists(OUTPUT):
    os.makedirs(OUTPUT)
tpl.save(OUTPUT + '/escape_auto.docx')

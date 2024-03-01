# -*- coding: utf-8 -*-
'''
Created : 2015-03-12

@author: Eric Lapouyade
'''

from docxtpl import DocxTemplate, RichText

tpl = DocxTemplate('templates/cellbg_tpl.docx')

context = {
    'alerts': [
        {
            'date': '2015-03-10',
            'desc': RichText('Very critical alert', color='FF0000', bold=True),
            'type': 'CRITICAL',
            'bg': 'FF0000',
        },
        {
            'date': '2015-03-11',
            'desc': RichText('Just a warning'),
            'type': 'WARNING',
            'bg': 'FFDD00',
        },
        {
            'date': '2015-03-12',
            'desc': RichText('Information'),
            'type': 'INFO',
            'bg': '8888FF',
        },
        {
            'date': '2015-03-13',
            'desc': RichText('Debug trace'),
            'type': 'DEBUG',
            'bg': 'FF00FF',
        },
    ],
}


import os
from pathlib import Path
# 跳转脚本所在目录
pwd = os.path.split(os.path.realpath(__file__))[0]
pwd = Path(pwd)
os.chdir(pwd)

tpl.render(context)
tpl.save('output/cellbg.docx')

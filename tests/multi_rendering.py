# -*- coding: utf-8 -*-
'''
Created : 2021-12-20

@author: Eric Lapouyade
'''

from docxtpl import DocxTemplate
import os
from pathlib import Path
# 跳转脚本所在目录
pwd = os.path.split(os.path.realpath(__file__))[0]
pwd = Path(pwd)
os.chdir(pwd)

tpl = DocxTemplate('templates/multi_rendering_tpl.docx')

documents_data = [
    {
        'dest_file': 'multi_render1.docx',
        'context': {
            'title': 'Title ONE',
            'body': 'This is the body for first document'
        }
    },
    {
        'dest_file': 'multi_render2.docx',
        'context': {
            'title': 'Title TWO',
            'body': 'This is the body for second document'
        }
    },
    {
        'dest_file': 'multi_render3.docx',
        'context': {
            'title': 'Title THREE',
            'body': 'This is the body for third document'
        }
    },
]

for document_data in documents_data:
    dest_file = document_data['dest_file']
    context = document_data['context']
    tpl.render(context)
    tpl.save('output/%s' % dest_file)

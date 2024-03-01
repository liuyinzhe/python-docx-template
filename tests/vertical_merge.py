# -*- coding: utf-8 -*-
'''
Created : 2017-10-15

@author: Arthaslixin
'''

from docxtpl import DocxTemplate
import os
from pathlib import Path
# 跳转脚本所在目录
pwd = os.path.split(os.path.realpath(__file__))[0]
pwd = Path(pwd)
os.chdir(pwd)

tpl = DocxTemplate('templates/vertical_merge_tpl.docx')

context = {
    'items': [
        {'desc': 'Python interpreters', 'qty': 2, 'price': 'FREE'},
        {'desc': 'Django projects', 'qty': 5403, 'price': 'FREE'},
        {'desc': 'Guido', 'qty': 1, 'price': '100,000,000.00'},
    ],
    'total_price': '100,000,000.00',
    'category': 'Book',
}

tpl.render(context)
tpl.save('output/vertical_merge.docx')

# -*- coding: utf-8 -*-
'''
Created : 2015-03-12

@author: Eric Lapouyade
'''

from docxtpl import DocxTemplate
import os
from pathlib import Path
# 跳转脚本所在目录
pwd = os.path.split(os.path.realpath(__file__))[0]
pwd = Path(pwd)
os.chdir(pwd)

tpl = DocxTemplate('templates/order_tpl.docx')

context = {
    'customer_name': 'Eric',
    'items': [
        {'desc': 'Python interpreters', 'qty': 2, 'price': 'FREE'},
        {'desc': 'Django projects', 'qty': 5403, 'price': 'FREE'},
        {'desc': 'Guido', 'qty': 1, 'price': '100,000,000.00'},
    ],
    'in_europe': True,
    'is_paid': False,
    'company_name': 'The World Wide company',
    'total_price': '100,000,000.00',
}

tpl.render(context)
tpl.save('output/order.docx')

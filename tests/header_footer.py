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


tpl = DocxTemplate('templates/header_footer_tpl.docx')

sd = tpl.new_subdoc()
p = sd.add_paragraph(
    'This is a sub-document to check it does not break header and footer'
)

context = {
    'title': 'Header and footer test',
    'company_name': 'The World Wide company',
    'date': '2016-03-17',
    'mysubdoc': sd,
}

tpl.render(context)
tpl.save('output/header_footer.docx')

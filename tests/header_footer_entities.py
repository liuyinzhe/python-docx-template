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

tpl = DocxTemplate('templates/header_footer_entities_tpl.docx')

context = {
    'title': 'Header and footer test',
}

tpl.render(context)
tpl.save('output/header_footer_entities.docx')

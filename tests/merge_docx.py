# -*- coding: utf-8 -*-
'''
Created : 2021-07-30

@author: Eric Lapouyade
'''

from docxtpl import DocxTemplate

import os
from pathlib import Path
# 跳转脚本所在目录
pwd = os.path.split(os.path.realpath(__file__))[0]
pwd = Path(pwd)
os.chdir(pwd)

tpl = DocxTemplate('templates/merge_docx_master_tpl.docx')
sd = tpl.new_subdoc('templates/merge_docx_subdoc.docx')

context = {
    'mysubdoc': sd,
}

tpl.render(context)
tpl.save('output/merge_docx.docx')

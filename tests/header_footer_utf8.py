# -*- coding: utf-8 -*-
'''
Created : 2016-07-19

@author: AhnSeongHyun

Edited : 2016-07-19 by Eric Lapouyade
'''

from docxtpl import DocxTemplate
import os
from pathlib import Path
# 跳转脚本所在目录
pwd = os.path.split(os.path.realpath(__file__))[0]
pwd = Path(pwd)
os.chdir(pwd)

tpl = DocxTemplate('templates/header_footer_tpl_utf8.docx')

sd = tpl.new_subdoc()
p = sd.add_paragraph(
    u'This is a sub-document to check it does not break header and footer with utf-8 '
    u'characters inside the template .docx'
)

context = {
    'title': u'헤더와 푸터',
    'company_name': u'세계적 회사',
    'date': u'2016-03-17',
    'mysubdoc': sd,
}

tpl.render(context)
tpl.save('output/header_footer_utf8.docx')

# -*- coding: utf-8 -*-
'''
Created : 2015-03-26

@author: Eric Lapouyade
'''

from docxtpl import DocxTemplate, RichText
import os
from pathlib import Path
# 跳转脚本所在目录
pwd = os.path.split(os.path.realpath(__file__))[0]
pwd = Path(pwd)
os.chdir(pwd)

tpl = DocxTemplate('templates/richtext_and_if_tpl.docx')


context = {'foobar': RichText('Foobar!', color='ff0000')}

tpl.render(context)
tpl.save('output/richtext_and_if.docx')

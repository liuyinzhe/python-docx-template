# -*- coding: utf-8 -*-
'''
Created : 2017-09-03

@author: Eric Lapouyade
'''

from docxtpl import DocxTemplate
import os
from pathlib import Path
# 跳转脚本所在目录
pwd = os.path.split(os.path.realpath(__file__))[0]
pwd = Path(pwd)
os.chdir(pwd)

DEST_FILE = 'output/replace_picture.docx'

tpl = DocxTemplate('templates/replace_picture_tpl.docx')

context = {}

tpl.replace_pic('python_logo.png', 'templates/python.png')
tpl.render(context)
tpl.save(DEST_FILE)

# -*- coding: utf-8 -*-
"""
Created : 2022-08-03
@author: Dongfang Song
"""


from docxtpl import DocxTemplate, RichText
import os
from pathlib import Path
# 跳转脚本所在目录
pwd = os.path.split(os.path.realpath(__file__))[0]
pwd = Path(pwd)
os.chdir(pwd)

tpl = DocxTemplate('templates/richtext_eastAsia_tpl.docx')
rt = RichText('测试TEST', font='eastAsia:Microsoft YaHei')
ch = RichText('测试TEST', font='eastAsia:微软雅黑')
sun = RichText('测试TEST', font='eastAsia:SimSun')
context = {
    'example': rt,
    'Chinese': ch,
    'simsun': sun,
}

tpl.render(context)
tpl.save('output/richtext_eastAsia.docx')

# -*- coding: utf-8 -*-

from docxtpl import DocxTemplate

import os
from pathlib import Path
# 跳转脚本所在目录
pwd = os.path.split(os.path.realpath(__file__))[0]
pwd = Path(pwd)
os.chdir(pwd)

tpl = DocxTemplate('templates/horizontal_merge_tpl.docx')
tpl.render({})
tpl.save('output/horizontal_merge.docx')

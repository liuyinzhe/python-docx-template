from docxtpl import DocxTemplate

# With old docxtpl version, "... for spicy ..." was replaced by "... forspicy..."
# This test is for checking that is some cases the spaces are not lost anymore

import os
from pathlib import Path
# 跳转脚本所在目录
pwd = os.path.split(os.path.realpath(__file__))[0]
pwd = Path(pwd)
os.chdir(pwd)

tpl = DocxTemplate('templates/preserve_spaces_tpl.docx')

tags = ['tag_1', 'tag_2']
replacement = ['looking', 'too']

context = dict(zip(tags, replacement))

tpl.render(context)
tpl.save('output/preserve_spaces.docx')

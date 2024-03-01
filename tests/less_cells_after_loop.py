from docxtpl import DocxTemplate

import os
from pathlib import Path
# 跳转脚本所在目录
pwd = os.path.split(os.path.realpath(__file__))[0]
pwd = Path(pwd)
os.chdir(pwd)

tpl = DocxTemplate('templates/less_cells_after_loop_tpl.docx')
tpl.render({})
tpl.save('output/less_cells_after_loop.docx')

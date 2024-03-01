from docxtpl import DocxTemplate

import os
from pathlib import Path
# 跳转脚本所在目录
pwd = os.path.split(os.path.realpath(__file__))[0]
pwd = Path(pwd)
os.chdir(pwd)

doctemplate = r'templates/doc_properties_tpl.docx'

tpl = DocxTemplate(doctemplate)

context = {
    'test': 'HelloWorld'
}


tpl.render(context)
tpl.save("output/doc_properties.docx")

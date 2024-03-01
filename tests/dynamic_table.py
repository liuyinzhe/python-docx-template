from docxtpl import DocxTemplate
import os
from pathlib import Path
# 跳转脚本所在目录
pwd = os.path.split(os.path.realpath(__file__))[0]
pwd = Path(pwd)
os.chdir(pwd)


tpl = DocxTemplate('templates/dynamic_table_tpl.docx')

context = {
    'col_labels': ['fruit', 'vegetable', 'stone', 'thing'],
    'tbl_contents': [
        {'label': 'yellow', 'cols': ['banana', 'capsicum', 'pyrite', 'taxi']},
        {'label': 'red', 'cols': ['apple', 'tomato', 'cinnabar', 'doubledecker']},
        {'label': 'green', 'cols': ['guava', 'cucumber', 'aventurine', 'card']},
    ],
}

tpl.render(context)
tpl.save('output/dynamic_table.docx')

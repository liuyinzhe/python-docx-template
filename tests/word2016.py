from docxtpl import DocxTemplate, RichText

import os
from pathlib import Path
# 跳转脚本所在目录
pwd = os.path.split(os.path.realpath(__file__))[0]
pwd = Path(pwd)
os.chdir(pwd)

tpl = DocxTemplate('templates/word2016_tpl.docx')
tpl.render(
    {
        'test_space': '          ',
        'test_tabs': 5 * '\t',
        'test_space_r': RichText('          '),
        'test_tabs_r': RichText(5 * '\t'),
    }
)
tpl.save('output/word2016.docx')

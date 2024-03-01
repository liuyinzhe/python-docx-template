# -*- coding: utf-8 -*-
'''
Created : 2016-03-26

@author: Eric Lapouyade
'''

from docxtpl import DocxTemplate
import os
from pathlib import Path
# 跳转脚本所在目录
pwd = os.path.split(os.path.realpath(__file__))[0]
pwd = Path(pwd)
os.chdir(pwd)

tpl = DocxTemplate('templates/nested_for_tpl.docx')

context = {
    'dishes': [
        {'name': 'Pizza', 'ingredients': ['bread', 'tomato', 'ham', 'cheese']},
        {
            'name': 'Hamburger',
            'ingredients': ['bread', 'chopped steak', 'cheese', 'sauce'],
        },
        {
            'name': 'Apple pie',
            'ingredients': ['flour', 'apples', 'suggar', 'quince jelly'],
        },
    ],
    'authors': [
        {
            'name': 'Saint-Exupery',
            'books': [
                {'title': 'Le petit prince'},
                {'title': "L'aviateur"},
                {'title': 'Vol de nuit'},
            ],
        },
        {
            'name': 'Barjavel',
            'books': [
                {'title': 'Ravage'},
                {'title': "La nuit des temps"},
                {'title': 'Le grand secret'},
            ],
        },
    ],
}

tpl.render(context)
tpl.save('output/nested_for.docx')

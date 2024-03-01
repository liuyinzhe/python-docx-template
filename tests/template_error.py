from docxtpl import DocxTemplate
from jinja2.exceptions import TemplateError
import six
import os
from pathlib import Path
# 跳转脚本所在目录
pwd = os.path.split(os.path.realpath(__file__))[0]
pwd = Path(pwd)
os.chdir(pwd)


six.print_('=' * 80)
six.print_("Generating template error for testing (so it is safe to ignore) :")
six.print_('.' * 80)
try:
    tpl = DocxTemplate('templates/template_error_tpl.docx')
    tpl.render({'test_variable': 'test variable value'})
except TemplateError as the_error:
    six.print_(six.text_type(the_error))
    if hasattr(the_error, 'docx_context'):
        six.print_("Context:")
        for line in the_error.docx_context:
            six.print_(line)
tpl.save('output/template_error.docx')
six.print_('.' * 80)
six.print_(" End of TemplateError Test ")
six.print_('=' * 80)

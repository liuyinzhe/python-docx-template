import subprocess
import glob
import six
import os

import os
from pathlib import Path
# 跳转脚本所在目录
pwd = os.path.split(os.path.realpath(__file__))[0]
pwd = Path(pwd)
os.chdir(pwd)

tests = sorted(glob.glob('[A-Za-z]*.py'))
excludes = ['runtests.py']

output_dir = os.path.join(os.path.dirname(__file__), 'output')
if not os.path.exists(output_dir):
    os.mkdir(output_dir)

for test in tests:
    if test not in excludes:
        six.print_('%s ...' % test)
        subprocess.call(['python', './%s' % test])

six.print_('Done.')

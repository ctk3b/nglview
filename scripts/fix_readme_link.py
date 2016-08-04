#!/usr/bin/env python
import os
import sys
import subprocess

readme_file = sys.argv[1]

if os.path.abspath(readme_file) == os.path.abspath('./README'):
    print("wrong README file {}".format(readme_file))
    sys.exit(1)

readme = open(sys.argv[1]).read()

words = ["(nglview.gif)",
         "(examples/images/membrane.gif)",
         "(doc/interface_classes.md)",
         "(./doc/interface_classes.md)",
         "(CHANGELOG.md)",
         "(examples/README.md)",
         "(./examples/README.md)",
         ]

for word in words:
    if '.gif' in word:
        new_word = "(" + 'https://github.com/arose/nglview/blob/master/' + word.strip('(').strip(')') + "?raw=true)"
    else:
        new_word = "(" + 'https://github.com/arose/nglview/blob/master/' + word.strip('(')
    if './' in new_word:
        new_word = new_word.replace('./', '')
    print(new_word)
    readme = readme.replace(word, new_word)

with open('doc/index.md', 'w') as fh:
    fh.write(readme)

subprocess.check_call('pandoc doc/index.md -o doc/index.rst', shell=True)

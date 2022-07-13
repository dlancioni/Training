# https://pypi.org/project/progress/

import os
from progress.spinner import Spinner
from progress.bar import ShadyBar

os.system("cls")
bar = ShadyBar('Importando arquivo', max=10)
for i in range(10):
    # Do some work
    bar.next()
bar.finish()



state = ""
spinner = Spinner('Carregando ')
while state != 'FINISHED':
    # Do some work
    spinner.next()
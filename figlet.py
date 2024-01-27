import random
import sys
from pyfiglet import Figlet

figlet = Figlet()
argv_len = len(sys.argv)

if argv_len == 1:
    figlet.setFont(font=random.choice(figlet.getFonts()))
    print(figlet.renderText(input('Input: ')))
elif argv_len == 3:
    if sys.argv[1] != '-f' and sys.argv[1] != '--font':
        sys.exit('Invalid usage')
    if sys.argv[2] not in figlet.getFonts():
        sys.exit('Invalid usage')
    figlet.setFont(font=sys.argv[2])
    print(figlet.renderText(input('Input: ')))
else:
    sys.exit('Invalid usage')


#!test.py
# -*- coding: utf-8 -*-
# mcb.pyw - saves and loads pieces of text to the clipboard
# usage: python test.py save <keyword> - saves clipboard to keyword
#       python test.py <keyword> - loads keyword to clipboard
#       python test.py list - loads all keywords to clipboard
#       python test.py delete <keyword> - deletes the keyword
#       python test.py delete - delete all keywords

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')
# save clipboard content
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
    print('save')
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    del mcbShelf[sys.argv[2]]
elif len(sys.argv) == 2:
    # list keywords and load content
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
        print('list')
    elif sys.argv[1].lower() == 'delete':
        mcbShelf.clear()
        print('deleted')
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])

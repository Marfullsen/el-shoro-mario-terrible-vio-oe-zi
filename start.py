#!/usr/bin/env python

try:
    exec('print "Cargando interfaz..."')
except SyntaxError as error:
    import ctypes, sys
    text = 'Debes usar Python 2 para ejecutar este juego.'
    title = 'Error'
    ctypes.windll.user32.MessageBoxW(None, text, title, 0x40000)
    sys.exit(1)

from pgmlib import main
main.main()

try:
    import pygame, os
    from pygame.locals import *
except ModuleNotFoundError as error:
    import ctypes, sys
    text = 'Debes instalar una version de PyGame compatible con Python 2 para ejecutar este juego.'
    title = 'Error'
    ctypes.windll.user32.MessageBoxW(None, text, title, 0x40000)
    sys.exit(1)
    
import menu, data
def main():
    os.environ["SDL_VIDEO_CENTERED"] = "1"
    #pygame.mixer.pre_init(44100, -16, 2, 4096)
    pygame.init()
    pygame.mouse.set_visible(0)
    pygame.display.set_icon(pygame.image.load(data.filepath("bowser1.gif")))
    pygame.display.set_caption("Super Mario Bros (Chilean Chilensis Version)")
    screen = pygame.display.set_mode((640, 480))
    menu.Menu(screen)

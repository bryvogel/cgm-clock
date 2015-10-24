import os
import pygame
import time
import datetime
import signal

class Display():
    __WIDTH = 320
    __HEIGHT = 240

    def loadPyGame(self):
        os.putenv('SDL_FBDEV', '/dev/fb1')
        os.putenv('SDL_VIDEODRIVER', 'fbcon')
        #os.putenv('SDL_VIDEODRIVER', 'fbdev')
        #os.putenv('SDL_VIDEODRIVER', 'directfb')

        pygame.init()
        pygame.display.init()
        pygame.font.init()
        pygame.mouse.set_visible(False)
        pygame.mixer.quit()

    def quitPyGame(self):
        pygame.mouse.set_visible(True)
        pygame.font.quit()
        pygame.display.quit()
        pygame.quit()

    def __init__(self, font="DejaVu Sans", font_size=64):
        self.loadPyGame()

        size = (self.__WIDTH, self.__HEIGHT)
        self.screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
        self.time_font = pygame.font.SysFont(font, font_size)

        self.hour = 0
        self.minute = 0
        self.second = 0
        self.colon = ":"
        self.evening = "AM"

        self.setBrightness(16)

    def __del__(self):
        self.quitPyGame()

    def setBrightness(self, level):
        self.font_color = (17 * level, 17 * level, 17 * level)
        self.__update()

    def setColon(self, state=True):
        self.colon = ":" if state else " "
        self.__update()

    def setEvening(self, state=True):
        self.evening = "PM" if state else "AM"
        self.__update()

    def setMinutes(self, minutes):
        self.minute = minutes
        self.__update()

    def setHours(self, hours):
        self.hour = hours
        self.__update()

    def __update(self):
        self.screen.fill((0, 0, 0))
        time_string = "%s%s%s %s" % (format(self.hour, '02'), self.colon, format(self.minute, '02'), self.evening)
        time_text = self.time_font.render(time_string, True, self.font_color)
        self.screen.blit(time_text, ((self.__WIDTH // 2) - time_text.get_width() // 2, (self.__HEIGHT // 2) - time_text.get_height() // 2))
        pygame.display.flip()

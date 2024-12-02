#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(600, 480))  # abre a janela e seta o tamanho

    def run(self):
        while True:
            menu = Menu(self.window)
            menu.run()
            pass
            # # check for all events
            # for event in pygame.event.get():
            #     if event.type == pygame.QUIT:
            #         print('Quitting...')
            #         pygame.quit()  # clase window
            #         quit()  # end pygame


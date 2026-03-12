#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.Const import MENU_OPTION, WIN_WIDTH, WIN_HEIGHT
from code.Level import Level
from code.Menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:
                # Correção 2: Mudamos o nome da variável para 'current_level'
                # e instanciamos a classe 'Level' corretamente.
                current_level = Level(self.window, 'Level1', menu_return)
                #level = level(self.window, 'Level1', menu_return)
                # Correção 3: Se não for usar o 'level_return', chame assim:
                current_level.run()
                #level_return = level.run()

            elif menu_return == MENU_OPTION[4]:
                pygame.quit()  # Close Window
                quit()  # end pygame
            else:
                pass












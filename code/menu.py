#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH, C_ORANGE, MENU_OPTION, C_WHITE, C_YELLOW


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/MenuBg.png')  #  carrega a imagem
        self.rect = self.surf.get_rect(left=0, top=0)  #  fazer um retangulo invisível dentro da janela, com default no canto superior esquerdo

    def run(self, ):
        menu_option = 0
        pygame.mixer_music.load('./asset/Menu.mp3')  # carreguei a musica
        pygame.mixer_music.play(-1)  # dar play na musica tocando (-1)indefinidamente

        while True: #loop infinito fazendo o desenho do fundo e dps escrevendo o texto
            self.window.blit(source=self.surf, dest=self.rect)  # source vem da imagem do surf e o destino onde a imagem fica é o retangulo
            self.menu_text(60, "Mountain", C_ORANGE, ((WIN_WIDTH / 2), 70))
            self.menu_text(60, "Shooter", C_ORANGE, ((WIN_WIDTH / 2), 120))

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(30, MENU_OPTION[i], C_YELLOW, ((WIN_WIDTH / 2), 200 + 25 * i))
                else:
                    self.menu_text(30, MENU_OPTION[i], C_WHITE, ((WIN_WIDTH / 2), 200 + 25 * i))
            pygame.display.flip()  # atualizar tudo na tela

            # # check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print('Quitting...')
                    pygame.quit()  # clase window
                    quit()  # end pygame
                if event.type == pygame.KEYDOWN: #evento de apertando uma tecla
                    if event.key == pygame.K_DOWN: # se a tecla de seta para baixo for pressionada
                        if menu_option < len(MENU_OPTION) - 1: # if para resetar a seleção de menu quando chegar no final voltar para a primeira opção
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_UP: # se a tecla de seta para cima for pressionada
                        if menu_option > 0: # if para resetar a seleção de menu quando chegar no começo voltar para a ultima opção
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1
                    if event.key == pygame.K_RETURN: # quando enter for press
                        return MENU_OPTION[menu_option] # reiniciando o menu, sai do loop e volta de novo

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)#qual font irá utilizar no menu
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha() #converte texto para imagem
        text_rect: Rect = text_surf.get_rect(center=text_center_pos) #faz um triangulo invisivel onde o tetxto irã ficar
        self.window.blit(source=text_surf, dest=text_rect) #literalmente desenha a imagem

import pygame

print()
pygame.init()
window = pygame.display.set_mode(size=(600, 480)) #abre a janela e seta o tamanho

while True:
    #check for all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() #clase window
            quit() #end pygame

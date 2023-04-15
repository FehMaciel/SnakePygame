#importa as Bibliotecas
import pygame, random, math       
from pygame.locals import *

#Inicia o Pygame
pygame.init()

pygame.font.init()

def calcular_distancia(cobrax, cobray, macax, macay):
    x1 = cobrax
    y1 = cobray
    x2 = macax
    y2 = macay
    distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distancia

def on_grid_random():
    x = random.randint(0,560)
    y = random.randint(0,560)
    return (x//10 * 10, y//10 * 10)

def collision(c1, c2):
    return (c1[0] == c2[0] and c1[1] == c2[1])

def collision_snake_body(c1, c2):
    return c1 == c2

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3
score = 0
distancia_mac = 0

score_font = pygame.font.Font('digital.ttf', 22)
sett = pygame.font.Font('arial.ttf', 14)




#Define a Janela com tamanho 600px por 600px sendo que o valor 0 0 desta tela que é uma matriz é no canto superior esquerdo
screen = pygame.display.set_mode((600,600))

#O Titulo da Janela
pygame.display.set_caption('Snake')

# Nesta Variavel snake ela é uma lista onde recebe as coordenadas iniciais da Cobra.
snake = [(210,200), (220,200), (230,200)]
snake_skin = pygame.Surface((10,10))
snake_skin.fill((1, 41, 13))

apple_pos = on_grid_random()
apple = pygame.Surface((10,10))
apple.fill((255,0,0))

#direção Inicial
my_direction = LEFT
clock = pygame.time.Clock()


#cria O Loop Inicial para o carregamento e encerramento da tela
while True:
    clock.tick(20)
    for event in pygame.event.get():
        #Habilita o Botão Fechar da Tela 
        if event.type == QUIT:
            #Se o Botão de Fechar é clicado encerrar a tela.
            pygame.quit()
        if event.type == KEYDOWN:
            
            if event.key == K_UP:
                if my_direction == DOWN:
                    my_direction = DOWN
                else:
                    my_direction = UP
                    
                
            if event.key == K_DOWN:
                if my_direction == UP:
                    my_direction = UP
                else:
                    my_direction = DOWN

            if event.key == K_LEFT:
                if my_direction == RIGHT:
                    my_direction = RIGHT
                else:
                    my_direction = LEFT

            if event.key == K_RIGHT:
                if my_direction == LEFT:
                    my_direction = LEFT
                else:
                    my_direction = RIGHT
        


                
    if collision(snake[0], apple_pos): 
        apple_pos = on_grid_random()
        snake.append((1,1))
        snake.pop
        score += 10
        
    if snake[0][0] < 0 or snake[0][0] > 580:
        pygame.quit()
    if snake[0][1] < 0 or snake[0][1] > 580:
        pygame.quit()

    
                
    if my_direction == UP:
        snake[0] = (snake[0][0], snake[0][1] - 10)
    if my_direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 10)
    if my_direction == RIGHT:
        snake[0] = (snake[0][0] + 10, snake[0][1])
    if my_direction == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])
    
    for i in range(len(snake) - 1, 0, -1):
        if collision_snake_body(snake[0], snake[i]): 
            pygame.quit()
        snake[i] = snake[i-1]
    
    
    screen.fill((25, 117, 49))
    screen.blit(apple,apple_pos)
    
    for pos in snake: 
        screen.blit(snake_skin, pos)
        
    
        
    text = score_font.render("Score: " + str(score), True, (255, 255, 255)) # Renderiza o texto na superfície
    screen.blit(text, (10, 10)) # Blit a superfície na tela
    
    text = sett.render("distancia: " + str(calcular_distancia(snake[0][0], snake[0][1], apple_pos[0], apple_pos[1])), True, (255, 255, 255)) # Renderiza o texto na superfície
    screen.blit(text, (10, 580)) # Blit a superfície na tela
            
    pygame.display.update()

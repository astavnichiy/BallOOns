#===============================================================================
# Импорты
#===============================================================================
import pygame
import os
import random
from pygame.time import delay
from person import Person

#===============================================================================
#Константы:
#===============================================================================
VERT_RES_MAIN = 0
HORIZ_RES_MAIN = 0    
   
SCREEN_BG_COLOR_R = 0
SCREEN_BG_COLOR_G = 0
SCREEN_BG_COLOR_B = 0

#===============================================================================
#Создание персонажей 
#===============================================================================
person1 = Person('Вася', 'computer')
person2 = Person('Петя', 'computer')
print (person1.get_name())
print (person2.get_name())
 

#===============================================================================
#Заполняем парметрами наш словарь 
#===============================================================================
settings = {} #словарь с параметрами
with open("game_settings.cfg", "r") as file:
    for line in file:
        key,val = line.strip().split(':')
        settings[key] = val
        
    print (settings)
    
#Получаем значения параметров из файла
VERT_RES_MAIN = int(settings.get('VERT_RES_MAIN'))
HORIZ_RES_MAIN = int(settings.get('HORIZ_RES_MAIN'))
#SCREEN_BACKGROUND_COLOR = settings.get(SCREEN_BACKGROUND_COLOR)
SCREEN_BG_COLOR_R = int(settings.get('SCREEN_BG_COLOR_R'))
SCREEN_BG_COLOR_G = int(settings.get('SCREEN_BG_COLOR_G'))
SCREEN_BG_COLOR_B = int(settings.get('SCREEN_BG_COLOR_B'))

#===============================================================================
# Игровой процесс
#===============================================================================






#===============================================================================
# Инициализация экрана и холста (слоя)
#===============================================================================
        
pygame.init()

#Экран
window = pygame.display.set_mode([HORIZ_RES_MAIN, VERT_RES_MAIN]) # try out larger values and see what happens !
pygame.display.set_caption('BallOOns')

#Слой
screen = pygame.Surface([HORIZ_RES_MAIN, VERT_RES_MAIN])            
screen.fill([SCREEN_BG_COLOR_R, SCREEN_BG_COLOR_G, SCREEN_BG_COLOR_B])

#Строка состояния
info_string = pygame.Surface([HORIZ_RES_MAIN, int(VERT_RES_MAIN/8)]) 
info_string.fill([100, SCREEN_BG_COLOR_G, SCREEN_BG_COLOR_B])  
  
#===============================================================================
# Добавить сюда меню
#===============================================================================



#===============================================================================
# Отработка столкновения
#===============================================================================
     
def big_bang(health, power):
    health = health - power
    return health
        

#===============================================================================
# Строка состояния 
#===============================================================================
pygame.font.init()
infoline_font = pygame.font.Font(None,32)








#===============================================================================
# Отрисовка игры 
#===============================================================================
runGame = True # флаг выходв из цикла игры
approach = True # флаг движения шариков

person1.start_position = person1.health
person2.start_position = HORIZ_RES_MAIN - person2.health
        
#Движение вправо. Отрисовка и стирание        
def move_right (screen, ball_movement, color_r, color_g, color_b, health): #backg_color_r, backg_color_g, backg_color_b
        pygame.draw.circle(screen, (SCREEN_BG_COLOR_R,SCREEN_BG_COLOR_G,SCREEN_BG_COLOR_B), (ball_movement-1, int(VERT_RES_MAIN/2)), health) # paint blue circle
        pygame.draw.circle(screen, (color_r, color_g, color_b), (ball_movement, int(VERT_RES_MAIN/2)), health) # Нужно будет заменить на значение жизни и т.д.       
    
#Движение влево. Отрисовка и стирание 
def move_left (screen, ball_movement, color_r, color_g, color_b, health):
        pygame.draw.circle(screen, (SCREEN_BG_COLOR_R,SCREEN_BG_COLOR_G,SCREEN_BG_COLOR_B), (ball_movement+1, int(VERT_RES_MAIN/2)),health) # paint blue circle
        pygame.draw.circle(screen, (color_r, color_g, color_b), (ball_movement,int(VERT_RES_MAIN/2)),health) # Нужно будет заменить на значение жизни и т.д. 

#Старт игры        
while runGame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runGame = False

    
    #сближение
    if approach == True:
        #Движение шарика1 вправо 
        move_right (screen, person1.start_position, person1.color_r, person1.color_g, person1.color_b, person1.health)
        person1.start_position += 1
        
        #Движение шарика2 влево     
        move_left (screen, person2.start_position, person2.color_r, person2.color_g, person2.color_b, person2.health)
        person2.start_position -= 1 

            
    #Проверка на выход с экрана 
    if person1.start_position + person1.health < 0 or person2.start_position + person2.health > HORIZ_RES_MAIN:
        approach = True


    #расхождение    
    if approach == False:    
        #Движение шарика1 влево         
        move_left (screen, person1.start_position, person1.color_r, person1.color_g, person1.color_b, person1.health)
        person1.start_position -= 1
        
        #Движение шарика 2 вправо
        move_right (screen, person2.start_position, person2.color_r, person2.color_g, person2.color_b, person2.health)     
        person2.start_position += 1

    #Проверка на соприкосновение 
    if person1.start_position + person1.health > person2.start_position - person2.health: 
        # столконовение
        approach = False
        
        # Закраска большого шара перед столкновением.  
        pygame.draw.circle(screen, (SCREEN_BG_COLOR_R,SCREEN_BG_COLOR_G,SCREEN_BG_COLOR_B), (person1.start_position+1, int(VERT_RES_MAIN/2)),person1.health+2) # paint blue circle
        pygame.draw.circle(screen, (SCREEN_BG_COLOR_R,SCREEN_BG_COLOR_G,SCREEN_BG_COLOR_B), (person2.start_position-1, int(VERT_RES_MAIN/2)),person2.health+2)        
        
        # Сюда действие при соприкосновении
        person1.health = big_bang(person1.health, person2.power)
        person2.health = big_bang(person2.health, person1.power)
        
        # Проверка, кто сдох и окончание игры. 
        if person1.health <= 0 and person2.health > 0:
            print('Игрок 1 проиграл')
            runGame = False
        elif person2.health <= 0 and person1.health > 0:
            print('Игрок 2 проиграл')        
            runGame = False
        elif person1.health <= 0 and person2.health <= 0:
            print('Сдохли оба')   
            runGame = False

    
    info_text = ' Игрок 1:  ' + str(person1.name) + '  Жизни:  ' + str(person1.health) + '          ' + '  Игрок 2: ' + person2.name + 'Жизни: ' + str(person2.health)
    info_string.blit(infoline_font.render(info_text, 1, (210, 120, 200)), (0,0))



    window.blit(info_string, (0,0))
    window.blit(screen, (0,40))
    pygame.display.flip()
    
    #Задержка для того чтобы они медленнее двигались
    pygame.time.delay(1)
        
        #===============================================================================
        

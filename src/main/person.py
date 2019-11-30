import random
import lang
import pygame

#===============================================================================
# Классы создания и выбора шаров
#===============================================================================


class Person:
    
    def __init__ (self, name, type):
        self.name = name
        self.type = type
        self.health = 0
        self.power = 0 
        self.TOTAL = 200
        self.color_r = 0
        self.color_g = 200
        self.color_b = 0
        
        if self.type == 'computer':
            self.health = random.randint(130,180)
            self.power = self.TOTAL - self.health
        
        else:
            while self.TOTAL != self.health + self.power:
                print(text1) #Введите параметры героя
                self.health = input(text2) #'Введите значение Здоровья (1..199)'
                self.power = input(text3) #'Введите значение Силы (1..199). В сумме со зводовьем 200'                
            
 

# Получаем значения   
    def get_name (self):
        return self.name
    
    def get_health (self):
        return self.health
    
    def get_power (self):
        return self.power
    
            
if __name__ == "__main__":
    pass

    
    
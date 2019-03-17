#===============================================================================
# Классы создания и выбора шаров
#===============================================================================

class Person:
    
    def __init__ (self, name):
        self.name = name


# Получаем значения   
    def get_name (self):
        return self.name
    
    def get_health (self):
        return self.health
    
    def get_armor (self):
        return self.armor
    
    def get_power (self):
        return self.power
    
# Отображаем значения    
    def print_name (self):
        print(self.name)
    
    def print_health (self):
        return self.health
    
    def print_armor (self):
        return self.armor
    
    def print_power (self):
        return self.power    
    
# Задаем значения для начала игры

    def initinal_param (self, health, armor, power):
        self.health = health
        self.armor = armor
        self.power = power
            
if __name__ == "__main__":
    pass

    
    
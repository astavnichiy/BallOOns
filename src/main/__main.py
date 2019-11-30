#===============================================================================
# управление игрой
#===============================================================================

#from src.main.person 
from person import Person
from visualisation import StartVisualization

#===============================================================================
# class Person2:
#     
#     def __init__ (self, name):
#         self.name = name
# 
# 
# # Получаем значения   
#     def get_name (self):
#         return self.name
#===============================================================================


person1 = Person('Вася', 'computer')
person1 = Person('Петя', 'computer')
print (person1.get_name())
print (person2.get_name())

visual = StartVisualization(person1, person2)

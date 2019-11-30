import locale

current_local = locale.getdefaultlocale()[0]
print(current_local)

if current_local == 'ru_RU':
    #Russian
    text1 = 'Введите параметры героя'
    text2 = 'Введите значение здоровья (1..199)'
    text3 = 'Введите значение Силы (1..199). В сумме со зводовьем 200'  
elif current_local == 'ua_UA':
    pass#UKR
    
    
else:
    pass#English

    
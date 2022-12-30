def choose_mode():    
    print('Добро пожаловать в телефонный справочник!')
    print('Выберите действие')
    print('1 - Создать контакт')
    print('2 - Найти контакт')
    choice = int(input())
    if choice == 1 or choice == 2:
        return choice
    else:
        print('Нет такого действия')


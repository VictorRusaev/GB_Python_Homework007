from datetime import datetime as dt

def add_contact():
    name = input('Введите имя: ')
    phone = input('Введите номер телефона в формате +70000000000: ')
    time = dt.now().strftime('%D %H:%M')
    with open('Homeworks\Homework007_1\phonebook.txt', 'a', encoding='utf-8') as file:
        file.write('Date created: {};\nName: {};\nPhone: {};\n  \n'
                    .format(time, name, phone))

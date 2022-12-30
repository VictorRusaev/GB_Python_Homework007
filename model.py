def search_and_print_contact():
    lines = []
    with open('Homeworks\Homework007_1\phonebook.txt', 'r') as file:
        lines = file.read().splitlines()
    
    print('Введите, что искать:')
    search_item = input('')
    element = list(filter(lambda x: search_item in x, lines))
    # print(element)
    print()
    # print(lines)
    box = 0
    for i in range(len(lines)):
        for j in range(len(element)):
            if lines[i] == element[j]:
                box = i
                if box % 2 == 0:
                    print(lines[i - 2])
                    print(lines[i - 1])
                    print(lines[i])
                    print(lines[i + 1])
                else:
                    print(lines[i - 1])
                    print(lines[i])
                    print(lines[i + 1])
                    print(lines[i + 2])
        

while True:
    print("1")
    print("2")
    print("3")
    print("4")
    TaskList = (int(input("Выберите задачу ")))

    if TaskList:
        a = input()
        print("Задача добавлена!")
    elif TaskList:
        my_list = 'Купить продукты'
        print(my_list)
    elif TaskList:
        my_list = ['1, 2, 3, 4']
        my_list.remove(1)
    elif TaskList:
        exit()
    else:
        print("Error")

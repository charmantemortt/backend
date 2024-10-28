list_tasks = []

while True:
    TaskList = int(input("Выберите действие:\n 1. Добавить задачу\n 2. Просмотреть список задач \n 3. Удалить задачу \n 4. Выйти из программы"))
    if TaskList == 1:
        a = input("Добавить задачу ")
        list_tasks.append(a)
        print("Задача добавлена!")
    elif TaskList == 2:
        print("Список задач")
        print(list_tasks)
    elif TaskList == 3:
        del_value = int(input("Выберите номер задачи для удаления: "))
        list_tasks.pop(del_value - 1)
        print(list_tasks)
    elif TaskList == 4:
        print("Программа завершена")
        break
    else:
        print("Error")

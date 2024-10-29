list_tasks = []

def add_task():
        a = input("Добавить задачу ")
        list_tasks.append(a)
        print("Задача добавлена!")

def view_task():
        print("Список задач")
        print(list_tasks)
        del_value = int(input("Выберите номер задачи для удаления: "))
        list_tasks.pop(del_value - 1)
        print(list_tasks)

def delete_task():
        view_task()
        del_value = int(input("Выберите номер задачи для удаления: "))
        list_tasks.pop(del_value - 1)
        print(list_tasks)

def main():
    while True:
        print("Выберите задачу ")
        print("Выберите действие:\n 1. Добавить задачу\n 2. Просмотреть список задач \n 3. Удалить задачу \n 4. Выйти из программы")

        choice = input("Вы выбрали ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_task()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("Программа завершена")
            break
main()

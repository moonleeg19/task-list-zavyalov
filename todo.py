tasks = []

while True:
    print("\nСписок задач")
    print("1. Добавить задачу")
    print("2. Показать задачи")
    print("3. Выход")

    choice = input("Выберите пункт: ")

    if choice == "1":
        task = input("Введите задачу: ").strip()
        if task:
            tasks.append(task)
            print("Задача добавлена.")
        else:
            print("Задача не может быть пустой.")

    elif choice == "2":
        if not tasks:
            print("Список задач пуст.")
        else:
            print("\nВаши задачи:")
            for number, task in enumerate(tasks, start=1):
                print(f"{number}. {task}")

    elif choice == "3":
        print("Программа завершена.")
        break

    else:
        print("Неверный пункт меню.")

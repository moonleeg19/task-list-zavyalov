def show_tasks(tasks):
    if not tasks:
        print("Список задач пуст.")
        return

    print("\nВаши задачи:")
    for number, task in enumerate(tasks, start=1):
        print(f"{number}. {task}")


def main():
    tasks = []

    while True:
        print("\nСписок задач")
        print("1. Добавить задачу")
        print("2. Показать задачи")
        print("3. Удалить задачу")
        print("4. Выход")

        choice = input("Выберите пункт: ").strip()

        if choice == "1":
            task = input("Введите задачу: ").strip()
            if task:
                tasks.append(task)
                print("Задача добавлена.")
            else:
                print("Задача не может быть пустой.")

        elif choice == "2":
            show_tasks(tasks)

        elif choice == "3":
            if not tasks:
                print("Удалять нечего: список задач пуст.")
                continue

            show_tasks(tasks)
            number = input("Введите номер задачи для удаления: ").strip()

            if not number.isdigit():
                print("Нужно ввести номер задачи.")
                continue

            index = int(number) - 1
            if 0 <= index < len(tasks):
                removed_task = tasks.pop(index)
                print(f"Удалена задача: {removed_task}")
            else:
                print("Задачи с таким номером нет.")

        elif choice == "4":
            print("Программа завершена.")
            break

        else:
            print("Неверный пункт меню. Выберите число от 1 до 4.")


if __name__ == "__main__":
    main()

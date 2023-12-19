def display_menu():
    """
        Отображает меню для управления заметками.

        Возвращает:
            str: Выбранный пункт меню.
    """
    print("\n--- Менеджер заметок ---")
    print("1. Добавить заметку")
    print("2. Показать все заметки")
    print("3. Обновить заметку")
    print("4. Удалить заметку")
    print("5. Найти заметку по ID")
    print("6. Найти заметку по заголовку")
    print("7. Удалить все заметки")
    print("0. Выход\n")
    choice = input("Выберите пункт меню: ")
    return choice


def process_user_choice(choice, manager):
    """
        Обрабатывает выбранный пункт меню.

        Параметры:
            choice (str): Выбранный пункт меню.
            manager (NoteManager): Экземпляр класса NoteManager.

        Возвращает:
            bool: Флаг, указывающий на продолжение работы меню.
    """
    if choice == "1":
        title = input("Введите заголовок: ")
        body = input("Введите содержимое: ")
        manager.add_note(title, body)
        print("Заметка добавлена.\n")

    elif choice == "2":
        manager.get_notes()

    elif choice == "3":
        note_id = input("Введите ID заметки: ")
        title = input("Введите новый заголовок: ")
        body = input("Введите новый содержимое: ")
        manager.update_note(note_id, title, body)
        print('Заметка обновлена\n')

    elif choice == '4':
        note_id = input("Введите ID заметки для удаления: ")
        if manager.delete_note(note_id):
            print("Заметка удалена.\n")
        else:
            print("Заметка не найдена.\n")

    elif choice == '5':
        note_id = input("Введите ID заметки: ")
        note = manager.find_note(note_id)
        print(note if note else "Заметка не найдена.\n")

    elif choice == '6':
        title = input("Введите заголовок заметки: ")
        note = manager.find_note_by_title(title)
        print(note if note else "Заметка не найдена.\n")

    elif choice == '7':
        manager.delete_all_notes()
        print("Все заметки удалены.\n")

    elif choice == '0':
        print("До свидания!")
        exit()

    else:
        print("Неверный выбор пункта меню. Пожалуйста, попробуйте еще раз.\n")

    return True

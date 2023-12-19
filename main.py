from note_manager import NoteManager
from menu import display_menu, process_user_choice


def main():
    filepath = 'notes.json'
    manager = NoteManager(filepath)

    while True:
        user_choice = display_menu()
        if not process_user_choice(user_choice, manager):
            break


if __name__ == '__main__':
    main()
    
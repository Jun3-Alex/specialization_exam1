import json
import os

from note import Note


class NoteManager:
    """
        Класс для управления заметками.

        Атрибуты:
            filepath (str): Путь к файлу, в котором хранятся заметки.
            notes (dict): Словарь, содержащий заметки.

        Методы:
            __init__: Инициализирует новый экземпляр класса NoteManager.
            load_notes: Загружает заметки из файла.
            save_notes: Сохраняет заметки в файл.
            add_note: Добавляет новую заметку.
            dict_to_str: Преобразует словарь заметки в строку.
            get_notes: Возвращает все заметки.
            update_note: Обновляет существующую заметку.
            delete_note: Удаляет существующую заметку.
            delete_all_notes: Удаляет все заметки.
            find_note: Находит заметку по идентификатору.
            find_note_by_title: Находит заметку по заголовку.
        """
    def __init__(self, filepath):
        self.filepath = filepath
        self.notes = self.load_notes()

    def load_notes(self):
        if not os.path.exists(self.filepath):
            return {}
        with open(self.filepath, 'r') as file:
            notes_data = json.load(file)
            return {note_id: Note.from_dict(note) for note_id, note in notes_data.items()}

    def save_notes(self):
        with open(self.filepath, 'w') as file:
            json.dump({note.note_id: note.to_dict() for note in self.notes.values()}, file, indent=4)

    def add_note(self, title, body):
        note = Note(title, body)
        self.notes[note.note_id] = note
        self.save_notes()

    @staticmethod
    def dict_to_str(note_dict):
        return (f"Note ID: {note_dict['id']}\n"
                f"Заголовок: {note_dict['title']}\n"
                f"Тело заметки: {note_dict['body']}\n"
                f"Последнее изменение: {note_dict['last_modified']}\n")

    def get_notes(self):
        notes_as_dicts = [note.to_dict() for note in self.notes.values()]
        return [print(self.dict_to_str(note)) for note in notes_as_dicts]

    def update_note(self, note_id, title, body):
        if note_id in self.notes:
            self.notes[note_id].update(title, body)
            self.save_notes()
            return True
        return False

    def delete_note(self, note_id):
        if note_id in self.notes:
            del self.notes[note_id]
            self.save_notes()
            return True
        return False

    def delete_all_notes(self):
        self.notes = {}
        self.save_notes()

    def find_note(self, note_id):
        for note in self.notes.values():
            if note.note_id == note_id:
                return str(note)
        return None

    def find_note_by_title(self, title):
        for note in self.notes.values():
            if note.title == title:
                return [print(self.dict_to_str(note.to_dict())) for note in self.notes.values() if note.title == title]

    def find_note_by_date(self, date):
        found_notes = []
        for note in self.notes.values():
            if note.last_modified.strftime("%Y-%m-%d") == date:
                found_notes.append(note)
                [print(self.dict_to_str(note.to_dict())) for note in found_notes]

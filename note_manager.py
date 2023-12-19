import json
import os

from note import Note


class NoteManager:
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
        return f'{note}\n'

    def get_notes(self):
        return [note.to_dict() for note in self.notes.values()]

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
                return {note.title: note.to_dict() for note in self.notes.values()}
        return None

    def find_note_by_title(self, title):
        for note in self.notes.values():
            if note.title == title:
                return {note.title: note.to_dict() for note in self.notes.values()}
        return None

from datetime import datetime
import secrets


class Note:
    """
        Класс для представления заметки.

        Атрибуты:
            note_id (str): Уникальный идентификатор заметки.
            title (str): Заголовок заметки.
            body (str): Текст заметки.
            last_modified (datetime): Временная метка последнего изменения заметки.

        Методы:
            __init__: Инициализирует новый экземпляр класса.
            _generate_id: Генерирует уникальный идентификатор.
            update: Обновляет заголовок и текст заметки.
            to_dict: Возвращает словарь с данными заметки.
            from_dict: Создает экземпляр класса из словаря с данными заметки.
            __str__: Возвращает строковое представление заметки.
        """
    def __init__(self, title: str, body: str, note_id=None, last_modified=None):
        self.note_id = note_id if note_id else self._generate_id()
        self.title = title
        self.body = body
        self.last_modified = last_modified if last_modified else datetime.now()

    @staticmethod
    def _generate_id():
        return secrets.token_hex(4)

    def update(self, title, body):
        self.title = title
        self.body = body
        self.last_modified = datetime.now()

    def to_dict(self):
        return {
            "id": self.note_id,
            "title": self.title,
            "body": self.body,
            "last_modified": self.last_modified.strftime("%Y-%m-%d %H:%M:%S")
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data['title'],
            data['body'],
            data['id'],
            datetime.strptime(data['last_modified'], '%Y-%m-%d %H:%M:%S')
        )

    def __str__(self):
        return (f"Note ID: {self.note_id}\n"
                f"Заголовок: {self.title}\n"
                f"Тело заметки: {self.body}\n"
                f"Последнее изменение: {self.last_modified.strftime('%Y-%m-%d %H:%M:%S')}\n")

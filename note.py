import datetime


class Note:
    def __init__(self, title: str, content: str, date: datetime, priority: str):
        self.title = title
        self.content = content
        self.date = date
        self.priority = priority

    def __str__(self):
        return (f'{self.title}<{self.priority}>:\n'
                f'{self.content}\n'
                f'{self.date}')

class Controller:
    def __init__(self, model):
        self.model = model

    """Просматривать список могут все!"""

    def get_list_of_articles(self):
        if not self.model.list_of_articles:
            return 'Список пуст!'
        else:
            self.model.get_list_of_articles()

    """Добавлять статьи может только админ"""

    def add_article(self, title, author, char_count, publication, description, user_roll):
        if user_roll == 'admin':
            self.model.add_article(title, author, char_count, publication, description)
            return 'Статья успешно добавлена в список админом'
        else:
            return None

    def dump_to_json(self, filename, user_roll):
        if not self.model.list_of_articles:
            return 'Список статей пуст!'
        else:
            if user_roll == 'admin':
                self.model.dump_to_json(filename)
                return f'Статья успешно добавлена в файл: {filename}'
            else:
                return 'Forbidden'

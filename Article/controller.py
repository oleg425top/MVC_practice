from model import Model


class Controller:
    def __init__(self, model):
        self.model = model

    def get_list_of_articles(self):
        if not self.model.list_of_articles:
            return 'Список пуст!'
        else:
            self.model.get_list_of_articles()

    """Добавлять статьи может только админ"""

    def add_article(self, title, author, char_count, publication, description, user_roll):
        if user_roll == 'admin':
            self.model.add_article(title, author, char_count, publication, description)
        else:
            return None

    def dump_to_json(self, filename, user_roll):
        if self.model.list_of_articles:
            if user_roll == 'admin':
                self.model.dump_to_json(filename)
                return 'Статья успешно добавлена в список админом'
            else:
                return 'Forbidden'
        else:
            return 'Список статей пуст!'

# model = Model()
# controller = Controller(model)
# controller.add_article("История искусства в XX веке", "Анна Сидорова", 7000, "ArtReview",
#                        "Статья рассматривает ключевые события и тенденции в искусстве XX века.", 'admin')
# controller.add_article("Экологические проблемы современного мира", 'Мария Петрова', 6000, 'EcoLife',
#                        'Статья обсуждает основные экологические проблемы и пути их решения.', 'admin')
# controller.get_list_of_articles()
# print(controller.dump_to_json('list_of_arts','admins'))

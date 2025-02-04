from model import Model


class Controller:
    def __init__(self, model):
        self.model = model

    def get_list_of_articles(self):
        self.model.get_list_of_articles()
        # print(var)

    """Добавлять статьи может только админ"""

    def add_article(self, title, author, char_count, publication, description, user_roll):
        if user_roll == 'admin':
            self.model.add_article(title, author, char_count, publication, description)
        else:
            return None


controller = Controller(Model)
controller.add_article("История искусства в XX веке", "Анна Сидорова", 7000, "ArtReview",
                       "Статья рассматривает ключевые события и тенденции в искусстве XX века.", 'admin')
controller.add_article("Экологические проблемы современного мира", 'Мария Петрова', 6000, 'EcoLife',
                       'Статья обсуждает основные экологические проблемы и пути их решения.', 'admin')
controller.get_list_of_articles()

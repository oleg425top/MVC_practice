import json


class Model:
    list_of_articles = []

    def __init__(self, title, author, char_count, publication, description ):
        self.title = title
        self.author = author
        self.char_count = char_count
        self.publication = publication
        self.description = description

    @staticmethod
    def to_json(obj):
        if isinstance(obj, Model):
            result = obj.__dict__
            return result

    @classmethod
    def get_list_of_articles(cls):
        for article in Model.list_of_articles:
            print(f'Статья: {article['title']}\nАвтор: {article['author']}\nОписание: {article['description']}')
            print('.'*20)
        # return Model.list_of_articles

    def dump_to_json(self, filename):
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(self.list_of_articles, file, default=Model.to_json, ensure_ascii=False, indent=3)

    @classmethod
    def add_article(cls, title, author, char_count, publication, description):
        article = {'title': title, 'author': author, 'char_count':char_count, 'publication':publication, 'description':description}
        Model.list_of_articles.append(article)



# art = Model("Искусственный интеллект и будущее технологий", "Иван Иванов", 5000, "TechNews",
#             "Статья рассматривает влияние искусственного интеллекта на развитие технологий и общества.")
# art_2 = Model("Экологические проблемы современного мира", 'Мария Петрова', 6000, 'EcoLife',
#               'Статья обсуждает основные экологические проблемы и пути их решения.')
# art.add_article('admin')
# print(Model.get_list_of_articles())
#
# art.dump_to_json(r'art.json')

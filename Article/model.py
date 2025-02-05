import json


class Model:
    list_of_articles = []

    def __init__(self, title=None, author=None, char_count=None, publication=None, description=None):
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
        if not Model.list_of_articles:
            return None
        else:
            for article in Model.list_of_articles:
                print(
                    f'Статья: {article['title']}\nАвтор: {article['author']}\nОписание: {article['description']}\n'
                    f'Впервые опубликована в : {article['publication']}\nКоличество знаков в статье: {article['char_count']}')
                print('.' * 20)

    def dump_to_json(self, filename):
        with open(fr'{filename}.json', 'w', encoding='utf-8') as file:
            json.dump(Model.list_of_articles, file, default=Model.to_json, ensure_ascii=False, indent=3)

    @classmethod
    def add_article(cls, title, author, char_count, publication, description):
        article = {'title': title, 'author': author, 'char_count': char_count, 'publication': publication,
                   'description': description}
        Model.list_of_articles.append(article)

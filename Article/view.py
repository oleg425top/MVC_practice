class View:

    def __init__(self, controller):
        self.controller = controller

    def display_list_of_articles(self):
        data = self.controller.get_list_of_articles()
        if data == 'Список пуст!':
            print(data)
        else:
            return data

    def display_add_article(self, title, author, char_count, publication, description, user_roll):
        data = self.controller.add_article(title, author, char_count, publication, description, user_roll)
        if not data:
            print('У вас нет прав доступа для этой операции')
        else:
            print(data)

    def display_dump_to_json(self, filename, user_roll):
        data = self.controller.dump_to_json(filename, user_roll)
        if data == 'Forbidden':
            print('У вас нет прав доступа для этой операции')
        else:
            print(data)

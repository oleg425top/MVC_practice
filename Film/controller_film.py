class Controller:
    def __init__(self, model):
        self.model = model

    def get_list_film(self):
        return self.model.get_list_film()

    def add_film(self, title, genre, director, year, duration, studio, actors:list, user_roll):
        if user_roll == 'admin':
            self.model.add_film(title, genre, director, year, duration, studio, actors)
            return 'Фильм добавлен в коллекцию'
        else:
            return 'Forbidden'

    def get_films_genre(self, genre):
        data = self.model.get_list_film()
        new_data = []
        for items in data:
            if items['Genre: '] == genre:
                new_data.append(items)
        return new_data

    def update_json(self, user_roll, filename):
        if user_roll == 'admin':
            self.model.update_json(filename)
            return 'Данные загружены в файл'
        else:
            return 'Forbidden'




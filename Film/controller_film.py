class Controller:
    def __init__(self, model):
        self.model = model

    def get_list_film(self):
        return self.model.get_list_film()

    def add_film(self, title, genre, director, year, duration, studio, actors: dict, user_roll):
        if user_roll == 'admin':
            self.model.add_film(title, genre, director, year, duration, studio, actors)
            return 'Фильм добавлен в коллекцию'
        else:
            return 'Forbidden'

    """Подборка фильмов по жанру"""

    def get_films_genre(self, genre):

        data = self.model.get_list_film()
        new_data = []
        if len(data) != 0:
            for items in data:
                if items['Genre: '] == genre:
                    new_data.append(items)
            print(f'Подборка фильмов по жанру: {genre}')
            return new_data
        else:
            return 'Список пуст'

    def update_json(self, user_roll, filename):
        if user_roll == 'admin':
            self.model.update_json(filename)
            return 'Данные загружены в файл'
        else:
            return 'Forbidden'

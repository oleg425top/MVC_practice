class Controller:
    def __init__(self, model):
        self.model = model

    """Просматривать коллекцию может любой желающий"""

    def get_list_film(self):
        return self.model.get_list_film()

    """Допустим добавлять фильмы в коллекцию может только админ"""

    def add_film(self, title, genre, director, year, duration, studio, actors: dict, user_roll):
        if user_roll == 'admin':
            self.model.add_film(title, genre, director, year, duration, studio, actors)
            return 'Фильм добавлен в коллекцию'
        else:
            return 'Forbidden'

    """Поиск фильма по названию"""

    def get_film_from_title(self, title_to_search):
        data = self.model.get_list_film()
        if len(data) == 0:
            return 'Список фильмов пуст'
        else:
            for film in data:
                if film['Title: '] == title_to_search:
                    print('Фильм найден')
                    return film
            return 'Такого фильма нет в списке'


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

    """Запись в файл JSON"""

    def update_json(self, user_roll, filename):
        if user_roll == 'admin':
            self.model.update_json(filename)
            return 'Данные загружены в файл'
        else:
            return 'Forbidden'

class View:
    def __init__(self, controller):
        self.controller = controller

    def display_list_film(self):
        print(self.controller.get_list_film())

    def display_add_film(self, title, genre, director, year, duration, studio, actors: dict, user_roll):
        data = self.controller.add_film(title, genre, director, year, duration, studio, actors, user_roll)
        print(data)

    """Подборка фильмов по жанру"""

    def display_film_genre(self, genre):
        data = self.controller.get_films_genre(genre)
        for film in data:
            print(film)

    def display_film_from_title(self, title_to_search):
        film = self.controller.get_film_from_title(title_to_search)
        for key, value in film.items():
            print(key,value)

    def display_update_json(self, user_roll, filename):
        print(self.controller.update_json(user_roll, filename))




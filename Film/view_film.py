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
        print(self.controller.get_films_genre(genre))

    def display_update_json(self, user_roll, filename):
        print(self.controller.update_json(user_roll, filename))




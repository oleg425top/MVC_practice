import json

class Model:
    def __init__(self):
        self.film_list = []

    def get_list_film(self):
        return self.film_list

    def add_film(self, title, genre, director, year, duration, studio, actors:dict):
        data = {'Title: ': title, 'Genre: ': genre, 'Year: ': year, 'Duration: ': duration,'Studio: ':studio, 'Actors: ':actors}
        self.film_list.append(data)

    def update_json(self, filename):
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(self.film_list, file, ensure_ascii=False, indent=3)
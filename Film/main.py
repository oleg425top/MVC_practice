from model_film import Model
from controller_film import Controller
from view_film import View

if __name__ == '__main__':
    model = Model()
    controller = Controller(model)
    view = View(controller)

    view.display_add_film("Титаник", "Драма", "Джеймс Кэмерон", 1997, 194, "20th Century Fox", {"Леонардо ДиКаприо": "Джек Доусон", "Кейт Уинслет": "Роуз Девитт Бьюкейтер"}, 'admin')
    view.display_update_json('admin', r'films.json')
    view.display_add_film("Матрица", "Научная фантастика", "Ланы Вачовски, Лилли Вачовски", 1999, 136, "Warner Bros.", {"Киану Ривз": "Нео", "Кэрри-Энн Мосс": "Тринити"}, 'admin')
    view.display_update_json('admin', r'films.json')
    view.display_list_film()
    view.display_add_film("Форрест Гамп", "Драма", "Роберт Земекис", 1994, 142, "Paramount Pictures", {"Том Хэнкс": "Форрест Гамп", "Робин Райт": "Дженни Каррен"}, 'admin')
    view.display_list_film()
    view.display_update_json('admin', r'films.json')
    view.display_film_genre("Драма")

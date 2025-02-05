from model import Model
from controller import Controller
from view import View

if __name__ == '__main__':
    model = Model()
    controller = Controller(model)
    view = View(controller)

    view.display_add_article("Искусственный интеллект и будущее технологий", "Иван Иванов", 5000, "TechNews",
                             "Статья рассматривает влияние искусственного интеллекта на развитие технологий и общества.",
                             'admin')
    view.display_add_article("Экологические проблемы современного мира", 'Мария Петрова', 6000, 'EcoLife',
                             'Статья обсуждает основные экологические проблемы и пути их решения.', 'admin')

    view.display_add_article("Экологические проблемы современного мира", 'Мария Петрова', 6000, 'EcoLife',
                             'Статья обсуждает основные экологические проблемы и пути их решения.', 'admins')
    print()
    view.display_list_of_articles()
    print()
    view.display_dump_to_json('list_of_art', 'admin')
    print()
    view.display_dump_to_json('list_of_art', 'user')

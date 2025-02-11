import json
""" Класс (Singleton) для управления заказами и финансовыми показателями. (Списал с ютуба)"""
class OrderManager:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(OrderManager, cls).__new__(cls)
            cls._instance.orders = []
            cls._instance.total_sales = 0
            cls._instance.total_revenue = 0
        return cls._instance
    def add_order(self, order):
        self.orders.append(order)
        self.total_sales += 1
        self.total_revenue += order.price
    def get_sales_report(self):
        return f'Продано пицц: {self.total_sales}\nНа общую сумму: {self.total_revenue}'
"""Класс топингов"""
class Toppings:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight
    def __str__(self):
        return f'Ингридиент: {self.name}. Цена: {self.price} Вес: {self.weight}'
"""Фабрика для создания топингов как для админа так и для юзера"""
class ToppingsFactory:
    @staticmethod
    def create_topping(name, price, weight):
        return Toppings(name, price, weight)
"""Класс самой пиццы"""
class Pizza:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight
        self.toppings = []
    def add_topping(self, topping: Toppings):
        self.toppings.append(topping)
        self.weight += topping.weight
        self.price += topping.price
    def get_toppings(self):
        if self.toppings:
            return f'{[topping.name for topping in self.toppings]}'
        else:
            return f'Пусто'
    def __str__(self):
        return f"Название: {self.name}\nЦена: {self.price}\nВес: {self.weight}\n"
"""Фабрика по созданию пиццы как для юзера так и для админа"""
class PizzaFactory:
    @staticmethod
    def create_pizza(name, price, weight):
        return Pizza(name, price, weight)
"""Класс меню который отвечает за вывод меню, и добавление в него пиццы и топингов"""
class Menu:
    def __init__(self):
        self.pizza_menu = []
        self.toppings = []
    def add_pizza(self, name, price, weight):
        pizza = PizzaFactory.create_pizza(name, price, weight)
        self.pizza_menu.append(pizza)
    def add_toppings(self, name, price, weight):
        topping = ToppingsFactory.create_topping(name, price, weight)
        self.toppings.append(topping)
    def print_menu(self):
        print('Стандартная пицца в меню:\n...............\n')
        [print(pizza) for pizza in self.pizza_menu]
    def get_menu(self):
        return self.pizza_menu
    def print_toppings(self):
        print('Вы можете добавить топинги: \n..............\n')
        [print(topping) for topping in self.toppings]
    def get_toppings(self, i: int):
        return self.toppings[i]
    """Создание меню с пиццами через фабрику пицц"""
    def create_menu(self):
        # Добавляем стандартные пиццы в меню
        self.add_pizza("Маргарита", 350, 450)
        self.add_pizza("Гавайская", 380, 480)
        self.add_pizza("Пепперони", 400, 500)
        self.add_pizza("Четыре сыра", 420, 520)
        self.add_pizza("Вегетарианская", 370, 470)
        # Добавляем топпинги в меню
        self.add_toppings("Грибы", 50, 50)
        self.add_toppings("Перец", 80, 50)
        self.add_toppings("Оливки", 100, 50)
"""класс Заказ, который сохраняет статистику в файл, и выводит информацию о заказе для юзера"""
class Order:
    def __init__(self, pizza: Pizza):
        self.pizza = pizza
        self.price = pizza.price
    def add_topping(self, topping: Toppings):
        self.pizza.add_topping(topping)
    # def create_custom_pizza(self):
    #     name = input("Введите название пиццы: ")
    #     price = float(input("Введите цену пиццы: "))
    #     weight = int(input("Введите вес пиццы: "))
    #     pizza = PizzaFactory.create_pizza(name, price, weight)
    #     print("Заказ оформлен!")
    #     return pizza
    def get_info_for_json(self):
        return {
            "pizza": self.pizza.name,
            "price": self.pizza.price,
            "weight": self.pizza.weight,
            "toppings": self.pizza.get_toppings(),
        }
    def get_info_for_user(self):
        return (f'Вы заказали пиццу: {self.pizza.name}\nСтоимость вместе с добавками: {self.pizza.price} р.\nОбщий вес'
                f' составил: {self.pizza.weight} грамм\n Добавки: {self.pizza.get_toppings()}')
    def save_order_to_file(self, order):
        with open("oleg_orders.json", "a", encoding='utf-8') as file:
            json.dump(order.get_info_for_json(), file, ensure_ascii=False, indent=3)
            file.write("\n")
"""Класс админ для создания пиццы и топингов"""
class Admin:
    def __init__(self, menu):
        self.menu = menu
    def add_pizza(self, name, price, weight):
        self.menu.add_pizza(name, price, weight)
        print('Пицца успешно добавлена!')
    def add_topping(self, name, price, weight):
        self.menu.add_toppings(name, price, weight)
        print('Топинг успешно добавлен!')
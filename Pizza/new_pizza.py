import json


class Toppings:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    def __str__(self):
        return f'Ингридиент: {self.name}. Цена: {self.price} Вес: {self.weight}'


class ToppingsFactory:
    @staticmethod
    def create_topping(name, price, weight):
        return Toppings(name, price, weight)


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
        else: return f'Пусто'

    def __str__(self):
        return f"Название: {self.name}\nЦена: {self.price}\nВес: {self.weight}\n"


class PizzaFactory:
    @staticmethod
    def create_pizza(name, price, weight):
        return Pizza(name, price, weight)


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


class Order:
    total_cost = []
    total_count = []

    def __init__(self, pizza: Pizza):
        self.pizza = pizza
        self.total_cost.append(self.pizza.price)
        self.total_count.append(1)

    def add_topping(self, topping: Toppings):
        self.pizza.add_topping(topping)

    def get_info(self):
        return {
            "pizza": self.pizza.name,
            "price": self.pizza.price,
            "weight": self.pizza.weight,
            "toppings": [self.pizza.get_toppings()],
        }

    def save_order_to_file(self, order):
        with open("oleg_orders.json", "a", encoding='utf-8') as file:
            json.dump(order.get_info(), file, ensure_ascii=False, indent=3)
            file.write("\n")


class Admin:
    def __init__(self, menu):
        self.menu = menu

    def add_pizza(self, name, price, weight):
        self.menu.add_pizza(name, price, weight)
        print('Пицца успешно добавлена!')

    def add_topping(self, name, price, weight):
        self.menu.add_toppings(name, price, weight)
        print('Топинг успешно добавлен!')

# t = Toppings('краб', 150, 50)
# t2 = Toppings('Фрунчоза', 250, 50)
# pizza_1 = Pizza("Маргарита", 350, 450)
# pizza_2 = Pizza("Пепперони", 400, 500)
# pizza_2.add_topping(t)
# pizza_2.add_topping(t2)
# pizza_3 = Pizza("Гавайская", 380, 480)
# m = Menu()
# m.create_menu()
# m.add_pizza(pizza_1)
# m.add_pizza(pizza_2)
# m.add_pizza(pizza_3)
# m.get_menu()

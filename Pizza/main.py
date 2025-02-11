from new_pizza import *

if __name__ == '__main__':

    menu = Menu()
    admin = Admin(menu)
    menu.create_menu()
    while True:
        user_chose = input('Здравствуйте. Кто вы:\n1: user\n2: admin\n:')
        if user_chose == '2':
            while True:
                print("1. Добавить пиццу в меню")
                print("2. Добавить топпинг в меню")
                print("3. Просмотреть меню")
                print("4. Выйти")
                choice = input("Выберите действие: ")
                if choice == '1':
                    name = input("Введите название пиццы: ")
                    price = int(input("Введите цену пиццы: "))
                    weight = int(input("Введите вес пиццы: "))
                    admin.add_pizza(name, price, weight)
                elif choice == '2':
                    name = input("Введите название топинга: ")
                    price = int(input("Введите цену топинга: "))
                    weight = int(input("Введите вес топинга: "))
                    admin.add_topping(name, price, weight)
                elif choice == '3':
                    menu.print_menu()
                    menu.print_toppings()
                elif choice == '4':
                    break
                else:
                    print('Данные не верны')
        elif user_chose == '1':
            chose = input('1: Сделать заказ\n2: Выход\n')
            if chose == '1':
                chose = input('1: Выбрать готовую пиццу\n2: Создать пиццу самому\n')
                if chose == '1':
                    menu.print_menu()
                    while True:
                        chose = input('Выберите пиццу и введите её номер, либо нажмите 0 для выхода')
                        if 0 <= int(chose) - 1 < len(menu.get_menu()):
                            order = Order(menu.get_menu()[int(chose) - 1])
                            print(order.get_info())
                            while True:
                                menu.print_toppings()
                                chose2 = input('Выберите добавку и введите её номер, либо введите 0 если добавки не нужны')
                                order.add_topping(menu.get_toppings(int(chose2)-1))
                                print(order.get_info())
                                if chose == '0':
                                    break
                            order.save_order_to_file(order)
                        elif chose == '0':
                            print('Ваш заказ готов')
                            break
                        #
                elif chose == '2':
                    pass
                else:
                    print('Данные не верны')
            elif chose == '2':
                break
            else:
                print('Данные не верны')
        else:
            print('Данные не верны')

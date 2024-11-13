import pickle
from view.Printer import Printer

class Customer:
    SAVE_FILE = "customer_state.pickle"

    def __init__(self, name):
        self.__name = name
        self.__orders = []

    def get_name(self):
        return self.__name

    def get_orders(self):
        return self.__orders

    def add_order_to_customer(self, order):
        self.__orders.append(order)

    def get_order_by_name(self, order_name):
        for order in self.__orders:
            if order.get_name() == order_name:
                return order
        return None

    def get_num_of_orders(self):
        return len(self.__orders)

    def delete_order(self, order):
        if order in self.__orders:
            self.__orders.remove(order)
            order.cancel()
            return True
        else:
            return False

    def view_orders(self):
        if self.__orders:
            for order in self.__orders:
                print(f"Заказ: {order.name}, Языки программирования: {order.preferred_languages}, Дедлайн: {order.deadline}, Бюджет: {order.budget}, Выполнен: {'Да' if order.completed else 'Нет'}")
        else:
            Printer.print_no_order()

    def get_uncompleted_orders(self):
        return [order for order in self.__orders if not order.is_completed()]

    def mark_order_as_completed(self, order_name):
        for order in self.__orders:
            if order.name == order_name:
                order.mark_as_completed()
                print(f"Заказ '{order_name}' отмечен как выполненный.")
                return
        print(f"Заказ с именем '{order_name}' не найден.")

    def save_state(self):
        with open(Customer.SAVE_FILE, 'wb') as f:
            pickle.dump(self, f)
        Printer.print_success_saving_file()

    @staticmethod
    def load_state():
        try:
            with open(Customer.SAVE_FILE, 'rb') as f:
                return pickle.load(f)
        except FileNotFoundError:
            Printer.print_file_not_found()
            return None

from model.Order import Order
from view.Printer import Printer
from model.ProgrammingLanguage import ProgrammingLanguage


class CustomerMenu:

    @staticmethod
    def customer_menu(company, customer):
        while True:
            Printer.print_customer_menu()
            choice = input("\nВыберите действие: ")
            if choice == '1':
                make_order(company, customer)
            elif choice == '2':
                Printer.print_your_orders()
                for order in customer.get_uncompleted_orders():
                    print(f"- {order.get_name()}")
            elif choice == '3':
                Printer.print_active_orders()
                for order in customer.get_uncompleted_orders():
                    print(f"- {order.get_name()}")
            elif choice == '4':
                    CustomerMenu.delete_an_order(company, customer)
            elif choice == '5':
                break
            else:
                Printer.print_invalid_choose()

    @staticmethod
    def delete_an_order(company, customer):
        order_name = input("Введите название заказа, который хотите удалить: ")
        order = customer.get_order_by_name(order_name)
        if order:
            customer.delete_order(order)
            Printer.print_order_deleted_successfully(order_name)
        else:
            Printer.print_order_not_found(order_name)


def make_order(company, customer):
    name = input("Введите название заказа: ")
    try:
        if not name.isalpha():
            raise ValueError("Название заказа не может содержать цифры.")
    except ValueError as e:
        Printer.print_error_order_name(e)
        return
    Printer.print_all_pr_langs()
    for lang in ProgrammingLanguage:
        print(lang.value)

    preferred_languages = [lang.strip() for lang in input("Введите предпочтительные языки через запятую: ").split(',')]
    for lang in preferred_languages:
        if lang not in [lang.value for lang in ProgrammingLanguage]:
            Printer.print_error_lang_exept()
            return

    deadline = input("Введите дедлайн заказа (в днях): ")
    try:
        deadline = int(deadline)
        if deadline <= 0:
            raise ValueError("Дедлайн должен быть положительным числом.")
    except ValueError as e:
        Printer.print_deadline_error(e)
        return

    budget = input("Введите бюджет заказа: ")
    try:
        budget = float(budget)
        if budget <= 0:
            raise ValueError("Бюджет должен быть положительным числом.")
    except ValueError as e:
        Printer.print_error_budget(e)
        return
    order = Order(name, preferred_languages, deadline, budget)
    company.add_order(order)
    customer.add_order_to_customer(order)

    Printer.print_order_success_added()

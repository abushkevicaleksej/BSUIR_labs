from pubsub import pub
from model import Model
from view import View
import web
from pizza import Size, Thickness, Dough, Topings


class Controller:
    def __init__(self):
        self.model: Model = Model()

    def run_web(self):
        web.run()

    def get_dough(self, dough_size, dough_thickness) -> Dough:
        if dough_size == "Large":
            size = Size.Large
        elif dough_size == "Medium":
            size = Size.Medium
        elif dough_size == "Small":
            size = Size.Small
        elif dough_size == "Personal":
            size = Size.Personal
        else:
            size = Size.Large

        if dough_thickness == "Thick":
            thickness = Thickness.Thick
        elif dough_thickness == "Thin":
            thickness = Thickness.Thin
        else:
            thickness = Thickness.Thick
        return Dough(size, thickness)

    def give_money(self, pos, amount):
        client_list = self.model.get_all_clients()
        self.model.client_earn_money(client_list[pos], amount)
        self.model.save_state()

    def add_client(self, name):
        self.model.add_client(name)
        self.model.save_state()

    def reset_all(self):
        self.model.reset()
        self.model.save_state()

    def hire_cook(self, name):
        self.model.hire_cook(name)
        self.model.save_state()

    def hire_waiter(self, name):
        self.model.hire_waiter(name)
        self.model.save_state()

    def hire_courier(self, name):
        self.model.hire_courier(name)
        self.model.save_state()

    def hire_cashier(self, name):
        self.model.hire_cashier(name)
        self.model.save_state()

    def run_cli(self):
        self.view = View()
        while True:
            choice = self.view.print_menu()
            choice = self.view.select_action()
            if choice == 1:
                client_name = self.view.get_client_name()
                client = self.model.add_client(client_name)
                if client is None:
                    self.view.error_message("This client already exists!")
            elif choice == 2:
                client_name = self.view.get_client_name()
                client = self.model.get_client(client_name)
                if client is None:
                    self.view.error_message("There is no such client!")
                    continue
                dough, topings = self.view.menu_choice(client)
                price = self.model.calculate_price(dough, topings)
                if not self.model.is_delivery_avail():
                    self.view.error_message("Delivery is not available right now")
                    continue
                if price * 1.2 > client.money:
                    self.view.error_message("Not enough money")
                    continue
                self.model.order_pizza(client, dough, topings)
            elif choice == 3:
                client_name = self.view.get_client_name()
                client = self.model.get_client(client_name)
                if client is None:
                    self.view.error_message("There is no such client!")
                    continue

                dough, topings = self.view.menu_choice(client)
                price = self.model.calculate_price(dough, topings)
                if not self.model.is_take_out_avail():
                    self.view.error_message("Takeout is not available right now")
                    continue
                if price > client.money:
                    self.view.error_message("Not enough money")
                    continue
                self.model.buy_pizza(client, dough, topings, True)
            elif choice == 4:
                client_name = self.view.get_client_name()
                client = self.model.get_client(client_name)
                if client is None:
                    self.view.error_message("There is no such client!")
                    continue

                dough, topings = self.view.menu_choice(client)
                price = self.model.calculate_price(dough, topings)
                if not self.model.is_take_in_avail():
                    self.view.error_message("Takein is not available right now")
                    continue
                if price > client.money:
                    self.view.error_message("Not enough money")
                    continue
                self.model.buy_pizza(client, dough, topings, False)
            elif choice == 5:
                self.view.print_all_clients(self.model.get_all_clients())
            elif choice == 6:
                self.view.print_pizzeria_info(self.model.get_pizzeria())
            elif choice == 7:
                client_name = input("Type client's name: ")
                client = self.model.get_client(client_name)
                if client is None:
                    self.view.error_message("There is no such client!")
                    continue
                money = self.view.input_money()
                self.model.client_earn_money(client, money)
            elif choice == 8:
                worker_name = self.view.input_name()
                self.model.hire_cook(worker_name)
            elif choice == 9:
                worker_name = self.view.input_name()
                self.model.hire_waiter(worker_name)
            elif choice == 10:
                worker_name = self.view.input_name()
                self.model.hire_courier(worker_name)
            elif choice == 11:
                worker_name = self.view.input_name()
                self.model.hire_cashier(worker_name)
            elif choice == 12:
                self.model.reset()
            elif choice == 13:
                self.model.save_state()
                break

        self.model.save_state()
        self.view.pre_next_action()

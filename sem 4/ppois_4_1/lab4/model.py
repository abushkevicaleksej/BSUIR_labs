import pickle
from typing import List, Optional
from pizzeria import Pizzeria
from client import Client
from pizza import Dough, Size, Thickness, Topings
from worker import PizzaOven
from pizzeria import Accounting


class Model:
    def __init__(self):
        try:
            with open("pizzeria_file.pkl", "rb") as file:
                self.pizzeria = pickle.load(file)
        except FileNotFoundError:
            self.pizzeria = Pizzeria("Kate's")

        try:
            with open("clients_file.pkl", "rb") as file:
                self.all_clients = pickle.load(file)
        except FileNotFoundError:
            self.all_clients: List[Client] = []

    def add_client(self, client_name: str) -> Optional[Client]:
        client = next((x for x in self.all_clients if x.name == client_name), None)
        if client is None:
            client = Client(client_name)
            self.all_clients.append(client)

            print("New client has been added!")
            return client
        print('not')
        return None

    def get_client(self, client_name: str) -> Optional[Client]:
        client = next((x for x in self.all_clients if x.name == client_name), None)
        return client

    def save_state(self) -> None:
        with open("pizzeria_file.pkl", "wb") as file:
            pickle.dump(self.pizzeria, file)

        with open("clients_file.pkl", "wb") as file:
            pickle.dump(self.all_clients, file)

    def reset(self) -> None:
        self.pizzeria = Pizzeria("Kate's")
        self.all_clients = []

    def order_pizza(self, client: Client, dough: Dough, topings: Topings):
        self.pizzeria.order_pizza(client, dough, topings)

    def buy_pizza(
        self, client: Client, dough: Dough, topings: Topings, isTakeOut: bool
    ):
        self.pizzeria.buy_pizza(client, dough, topings, isTakeOut)

    def calculate_price(self, dough: Dough, topings: Topings):
        return self.pizzeria.calculate_price(dough, topings)

    def is_delivery_avail(self) -> bool:
        return self.pizzeria._is_delivery_avail()

    def is_take_out_avail(self) -> bool:
        return self.pizzeria._is_take_out_avail()

    def is_take_in_avail(self) -> bool:
        return self.pizzeria._is_take_in_avail()

    def get_all_clients(self) -> List[Client]:
        return self.all_clients

    def get_pizzeria(self) -> Pizzeria:
        return self.pizzeria

    def client_earn_money(self, client: Client, money: float) -> None:
        client.earn_money(money)

    def hire_cook(self, name: str):
        self.pizzeria.hire_cook(name)

    def hire_waiter(self, name: str):
        self.pizzeria.hire_waiter(name)

    def hire_courier(self, name: str):
        self.pizzeria.hire_courier(name)

    def hire_cashier(self, name: str):
        self.pizzeria.hire_cashier(name)

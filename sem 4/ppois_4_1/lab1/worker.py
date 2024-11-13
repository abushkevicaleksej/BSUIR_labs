from client import Client
from pizza import Pizza, Dough, Topings


class PizzaOven:
    def bake(self, pizza: Pizza) -> None:
        pizza.get_baked()


class Worker:
    def __init__(self, name: str):
        self._name: str = name
        self._earned_money: float = 0

    def __str__(self) -> str:
        return f"Name: {self._name}, earned money: {self._earned_money}"

    def earn_money(self, amount: float) -> None:
        self._earned_money += amount

    @property
    def earned_money(self) -> float:
        return self._earned_money

    @property
    def name(self) -> str:
        return self._name


class Courier(Worker):
    def deliver_pizza(self, client: Client, pizza: Pizza, money: float) -> None:
        pizza.get_delivered()
        client.spend_money(money)
        client.get_pizza(pizza)


class Waiter(Worker):
    def serve_pizza(self, client: Client, pizza: Pizza, money: float) -> None:
        client.spend_money(money)
        client.get_pizza(pizza)


class Cashier(Worker):
    def sell_pizza(self, client: Client, pizza: Pizza, money: float) -> None:
        client.spend_money(money)
        client.get_pizza(pizza)


class Cook(Worker):
    def prepare_pizza(self, dough: Dough, toppings: Topings) -> Pizza:
        return Pizza(dough, toppings)

    def bake_pizza(self, pizzaOven: PizzaOven, pizza: Pizza) -> None:
        pizzaOven.bake(pizza)

    def box_pizza(self, pizza: Pizza) -> None:
        return pizza.get_boxed()

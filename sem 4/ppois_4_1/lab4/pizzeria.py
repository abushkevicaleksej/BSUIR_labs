import random
from typing import List, Optional
from pizza import Pizza, Dough, Topings
from worker import Cook, Courier, Waiter, Cashier, PizzaOven
from client import Client


class Accounting:
    def __init__(self):
        self.revenue: float = 0
        self.expenses: float = 0

    def add_revenue(self, amount: float) -> None:
        self.revenue += amount

    def add_expense(self, amount: float) -> None:
        self.expenses += amount

    def calculate_profit(self) -> float:
        return self.revenue - self.expenses


class Pizzeria:
    def __init__(self, name: str):
        self._name: str = name
        self._cooks: List[Cook] = []
        self._couries: List[Courier] = []
        self._waiters: List[Waiter] = []
        self._cashiers: List[Cashier] = []
        self._accounting: Accounting = Accounting()
        self._pizzaOven: PizzaOven = PizzaOven()

    def __str__(self) -> str:
        string = f"Pizzeria: {self._name} \
        \nProfit: {self._accounting.calculate_profit()}\
        \nService staff:\nCooks:\n"
        delim = "\n"
        if len(self._cooks) == 0:
            string += "None\n"
        else:
            string += delim.join(str(worker) for worker in self._cooks)
        string += "\nCouriers:\n"
        if len(self._couries) == 0:
            string += "None\n"
        else:
            string += delim.join(str(worker) for worker in self._couries)
        string += "\nWaiters:\n"
        if len(self._waiters) == 0:
            string += "None\n"
        else:
            string += delim.join(str(worker) for worker in self._waiters)
        string += "\nCashiers:\n"
        if len(self._cashiers) == 0:
            string += "None\n"
        else:
            string += delim.join(str(worker) for worker in self._cashiers)
        return string

    def calculate_price(self, dough: Dough, topings: Topings) -> float:
        return dough.get_price() + topings.get_price()

    def hire_cook(self, name: str) -> None:
        self._cooks.append(Cook(name))

    def hire_courier(self, name: str) -> None:
        self._couries.append(Courier(name))

    def hire_waiter(self, name: str) -> None:
        self._waiters.append(Waiter(name))

    def hire_cashier(self, name: str) -> None:
        self._cashiers.append(Cashier(name))

    def _is_delivery_avail(self) -> bool:
        return bool(self._cooks and self._couries)

    def _is_take_in_avail(self) -> bool:
        return bool(self._cooks and self._waiters)

    def _is_take_out_avail(self) -> bool:
        return bool(self._cooks and self._cashiers)

    def _get_cook(self) -> Cook:
        return random.choice(self._cooks)

    def _get_cashier(self) -> Cashier:
        return random.choice(self._cashiers)

    def _get_courier(self) -> Courier:
        return random.choice(self._couries)

    def _get_waiter(self) -> Waiter:
        return random.choice(self._waiters)

    def order_pizza(
        self, client: Client, dough: Dough, topings: Topings
    ) -> Optional[Pizza]:
        cook = self._get_cook()

        price = self.calculate_price(dough, topings)
        pizza = cook.prepare_pizza(dough, topings)
        cook.bake_pizza(self._pizzaOven, pizza)
        cook.box_pizza(pizza)
        cook.earn_money(price * 0.3)
        multipled_price = round(price * 1.2, 2)
        courier = random.choice(self._couries)
        courier.deliver_pizza(client, pizza, multipled_price)
        courier.earn_money(price * 0.2)
        self._accounting.add_revenue(multipled_price)
        self._accounting.add_expense(price * 0.3 + price * 0.2)

        return pizza

    def buy_pizza(
        self, client: Client, dough: Dough, topings: Topings, is_takeout: bool = True
    ) -> Optional[Pizza]:
        price = self.calculate_price(dough, topings)

        cook = random.choice(self._cooks)
        pizza = cook.prepare_pizza(dough, topings)
        cook.bake_pizza(self._pizzaOven, pizza)
        cook.earn_money(price * 0.3)

        self._accounting.add_revenue(price)
        if not is_takeout:
            waiter = self._get_waiter()
            waiter.serve_pizza(client, pizza, price)
            waiter.earn_money(price * 0.15)
            self._accounting.add_expense(price * 0.3 + price * 0.15)
        else:
            cook.box_pizza(pizza)
            cashier = self._get_cashier()
            cashier.sell_pizza(client, pizza, price)
            cashier.earn_money(price * 0.1)
            self._accounting.add_expense(price * 0.3 + price + 0.1)

        return pizza

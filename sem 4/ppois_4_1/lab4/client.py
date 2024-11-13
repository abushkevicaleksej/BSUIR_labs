from pizza import Pizza
from typing import List

class Client:
    def __init__(self, name: str):
        self._name: str = name
        self._money: float = 0
        self._available_pizza: List[Pizza] = []

    def __str__(self) -> str:
        string = f"Name: {self._name}, money: {self._money}\n"
        if len(self._available_pizza) == 0:
            string += "No pizza"
            return string
        string += "All pizza:\n"
        delim = "\n"
        string += delim.join(str(pizza) for pizza in self._available_pizza)

        return string

    @property
    def name(self) -> str:
        return self._name

    @property
    def money(self) -> float:
        return self._money

    def earn_money(self, amount: float) -> None:
        self._money += amount

    def spend_money(self, amount: float) -> bool:
        if self._money >= amount:
            self._money -= amount
            return True
        return False

    def get_pizza(self, pizza: Pizza) -> None:
        self._available_pizza.append(pizza)


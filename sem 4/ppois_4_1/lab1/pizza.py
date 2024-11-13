from enum import Enum
from typing import List


class Size(Enum):
    Large = 2
    Medium = 1.64
    Small = 1.35
    Personal = 1


class Thickness(Enum):
    Thick = 2
    Thin = 1


class Dough:
    def __init__(self, size: Size, thickness: Thickness):
        self.size: Size = size
        self.thickness: Thickness = thickness

    def __str__(self) -> str:
        string = ""
        if self.thickness == Thickness.Thick:
            string += "thick and "
        else:
            string += "thin and "

        if self.size == Size.Personal:
            string += "personal"
        elif self.size == Size.Small:
            string += "small"
        elif self.size == Size.Medium:
            string += "medium"
        else:
            string += "large"

        return string

    def get_price(self) -> float:
        return self.thickness.value + self.size.value


class Topings:
    def __init__(self, ingredients: List[str]):
        self.ingredients: List[str] = ingredients

    def __str__(self) -> str:
        string = ", ".join(toping for toping in self.ingredients)
        return string

    def get_price(self) -> float:
        return 1.25 * len(self.ingredients)


class Pizza:
    def __init__(self, dough: Dough, toppings: Topings) -> None:
        self.dough: Dough = dough
        self.topings: Topings = toppings
        self._is_baked: bool = False
        self._is_hot: bool = False
        self._is_boxed: bool = False

    def __str__(self) -> str:
        string = f"Pizza: \
        \ndough: {self._get_dough_str()} \
        \ntopings: {self._get_topings_str()} \
        \nbaked: {self._is_baked} \
        \nhot: {self._is_hot} \
        \nboxed: {self._is_boxed}"
        return string

    def get_price(self) -> float:
        return self.dough.get_price() + self.topings.get_price()

    def get_baked(self) -> None:
        self._is_hot = True
        self._is_baked = True

    def get_delivered(self) -> None:
        self._is_hot = False

    def get_boxed(self) -> None:
        self._is_boxed = True

    def _get_dough_str(self) -> str:
        return str(self.dough)

    def _get_topings_str(self) -> str:
        return str(self.topings)

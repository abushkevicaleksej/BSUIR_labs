import os
from typing import List
from pizzeria import Pizzeria
from pizza import Topings, Dough, Thickness, Size
from pizzeria import Client


class View:
    def print_menu(self):
        print(
            "Menu: \
\n1. Add new client \
\n2. Order delivery \
\n3. Take out \
\n4. Take in \
\n5. Print clients info \
\n6. Print pizzeria info \
\n7. Earn client money \
\n8. Hire a cook \
\n9. Hire a waiter \
\n10. Hire a courier \
\n11. Hire a cashier \
\n12. Reset all\
\n13. Exit\n"
        )

    def select_action(self) -> int:
        while True:
            try:
                choice = int(input("Select an action: "))
            except ValueError:
                print("The input has to be numerical")
                continue

            return choice

    def input_money(self) -> float:
        while True:
            try:
                money = float(input("Enter the money: "))
            except ValueError:
                print("The input has to be numerical")
                continue

            if money < 0:
                continue

            return money

    def input_name(self) -> str:
        while True:
            name = input("Enter the name: ")
            if name == "":
                self.error_message("The name is empty!")
                continue
            # TODO remove the unneccessary spaces
            return name

    def get_client_name(self) -> str:
        return input("Type client's name: ")

    def error_message(self, message: str) -> None:
        print(f"[Error]: {message}")

    def info_message(self, message: str) -> None:
        print(f"[Info]: {message}")

    def menu_choice(self, client: Client) -> tuple[Dough, Topings]:
        while True:
            thickness_type = input("dough type(thick/thin): ")
            if thickness_type.lower() == "thin":
                thickness = Thickness.Thin
                break
            elif thickness_type.lower() == "thick":
                thickness = Thickness.Thick
                break
            print("Wrong input")

        while True:
            size_type = input("size(large/medium/small/personal): ")
            if size_type.lower() == "large":
                size = Size.Large
                break
            elif size_type.lower() == "medium":
                size = Size.Medium
                break
            elif size_type.lower() == "small":
                size = Size.Small
                break
            elif size_type.lower() == "personal":
                size = Size.Personal
                break
            print("Wrong input")

        topings = input("topings(separate using spaces): ")
        topings = Topings(topings.split())
        return Dough(size, thickness), topings

    def print_all_clients(self, all_clients: List[Client]) -> None:
        print("All clients: ")
        for client in all_clients:
            print(client, end="\n\n")

    def print_pizzeria_info(self, pizzeria: Pizzeria) -> None:
        print(pizzeria)

    def pre_next_action(self) -> None:
        input("Press ENTER to continue\n")
        os.system("cls")

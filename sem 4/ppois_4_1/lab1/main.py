import pickle
import os
from pizzeria import Pizzeria
from client import Client
from pizza import Dough, Size, Thickness, Topings
from typing import List
from worker import PizzaOven
from pizzeria import Accounting


def add_client(all_clients: List[Client], client_name: str) -> Client:
    client = next((x for x in all_clients if x.name == client_name), None)
    if client is None:
        client = Client(client_name)
        all_clients.append(client)

        print("New client has been added!")
        return client
    return client


def menu_choice(all_clients: List[Client]) -> tuple[Client, Dough, Topings]:
    client_name = input("Type client's name: ")
    client: Client = add_client(all_clients, client_name)
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

    topings = input("topings(separate using space): ")
    topings = Topings(topings.split())
    return client, Dough(size, thickness), topings


def save_state(pizzeria: Pizzeria, all_clients: List[Client]) -> None:
    with open("pizzeria_file.pkl", "wb") as file:
        pickle.dump(pizzeria, file)

    with open("clients_file.pkl", "wb") as file:
        pickle.dump(all_clients, file)


if __name__ == "__main__":
    try:
        with open("pizzeria_file.pkl", "rb") as file:
            pizzeria = pickle.load(file)
    except FileNotFoundError:
        pizzeria = Pizzeria("The one")

    try:
        with open("clients_file.pkl", "rb") as file:
            all_clients = pickle.load(file)
    except FileNotFoundError:
        all_clients: List[Client] = []

    while True:
        try:
            choice = int(
                input(
                    "Choose and action: \
                    \n1. Add new client \
                    \n2. Order pizza \
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
            )
        except ValueError:
            print("The input has to be numerical")
            continue

        if choice == 1:
            client_name = input("Type client's name: ")
            add_client(all_clients, client_name)
        elif choice == 2:
            pizzeria.order_pizza(*menu_choice(all_clients))
        elif choice == 3:
            pizzeria.buy_pizza(*menu_choice(all_clients), is_takeout=True)
        elif choice == 4:
            pizzeria.buy_pizza(*menu_choice(all_clients), is_takeout=False)
        elif choice == 5:
            print("All clients: ")
            for client in all_clients:
                print(client, end="\n\n")
        elif choice == 6:
            print(pizzeria)
        elif choice == 7:
            client_name = input("Type client's name: ")
            client = add_client(all_clients, client_name)
            money = float(input("Type money sum: "))
            client.earn_money(money)
        elif choice == 8:
            worker_name = input("Type cook's name: ")
            pizzeria.hire_cook(worker_name)
        elif choice == 9:
            worker_name = input("Type waiter's name: ")
            pizzeria.hire_waiter(worker_name)
        elif choice == 10:
            worker_name = input("Type courier's name: ")
            pizzeria.hire_courier(worker_name)
        elif choice == 11:
            worker_name = input("Type cashier's name: ")
            pizzeria.hire_cashier(worker_name)
        elif choice == 12:
            Pizzeria("The one")
            all_clients = []
        elif choice == 13:
            save_state(pizzeria, all_clients)
            break

        save_state(pizzeria, all_clients)
        input("Press ENTER to continue\n")
        os.system("cls")

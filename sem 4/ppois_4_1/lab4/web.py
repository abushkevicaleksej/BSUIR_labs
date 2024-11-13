from os import error
from flask import Flask, render_template, request, jsonify
from flask.helpers import url_for
from werkzeug.utils import redirect
from model import Model
from pizza import Dough, Size, Thickness, Topings
from typing import List

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/view", methods=["GET", "POST"])
def view():
    options = ["Pizzeria", "Clients"]
    if request.method == "POST":
        selected_option = request.form["select-box"]
        print(f"selected: {selected_option}")
        if selected_option == "Pizzeria":
            data = str(model.get_pizzeria())
        elif selected_option == "Clients":
            data = model.get_all_clients()
        else:
            data = "Error"
    else:
        selected_option = "Pizzeria"
        data = str(model.get_pizzeria())
    print(type(data))
    print(len(data))
    if isinstance(data, list):
        if len(data) == 0:
            data = "There are no clients"
        else:
            data_list = data
            data = ""
            for data_elem in data_list:
                data += str(data_elem) + "\n"

    data = data.split("\n")
    print(f"here: {selected_option}")
    return render_template(
        "view.html", options=options, selected_option=selected_option, data=data
    )


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        try:
            if model.add_client(request.form["client-name"]) is None:
                return render_template(
                    "add.html", error="There is already a cilent with such name!"
                )

            model.save_state()
            return render_template("add.html", success="The client has been added")
        except KeyError:
            return render_template("add.html", error="The input field is empty")

    return render_template("add.html")


def clients_to_data():
    all_clients = model.get_all_clients()
    return [{"name": client.name, "money": client.money} for client in all_clients]


@app.route("/add-money", methods=["GET", "POST"])
def add_money():
    if request.method == "POST":
        try:
            client = model.get_client(request.form["selected_id"])
            if client is None:
                table_data = clients_to_data()
                return render_template(
                    "add-money.html",
                    table_data=table_data,
                    error="Select a client!",
                )
            else:
                model.client_earn_money(client, float(request.form["input-money"]))
                model.save_state()
                table_data = clients_to_data()
                return render_template(
                    "add-money.html",
                    table_data=table_data,
                    success="The money have been added!",
                )

        except KeyError:
            table_data = clients_to_data()
            return render_template(
                "add-money.html",
                table_data=table_data,
                error="The client haven't been selected!",
            )

    table_data = clients_to_data()
    return render_template("add-money.html", table_data=table_data)


@app.route("/hire", methods=["GET", "POST"])
def hire():
    options = ["Cook", "Courier", "Waiter", "Cashier"]
    selected_option = "Cook"
    if request.method == "POST":
        name = request.form["worker-name"]
        worker_type = request.form["worker_type"]
        selected_option = worker_type
        if worker_type == "Cook":
            model.hire_cook(name)
        elif worker_type == "Cashier":
            model.hire_cashier(name)
        elif worker_type == "Courier":
            model.hire_courier(name)
        elif worker_type == "Waiter":
            model.hire_waiter(name)

        model.save_state()
        return render_template(
            "hire.html",
            options=options,
            selected_option=selected_option,
            success="The worker has been hired!",
        )

    return render_template(
        "hire.html", options=options, selected_option=selected_option
    )


def getDough(size_str: str, thickness_str: str):
    Size.Personal
    if size_str == "Personal":
        size = Size.Personal
    elif size_str == "Small":
        size = Size.Small
    elif size_str == "Medium":
        size = Size.Medium
    elif size_str == "Large":
        size = Size.Large
    else:
        size = Size.Personal

    if thickness_str == "Thick":
        thickness = Thickness.Thick
    elif thickness_str == "Thin":
        thickness = Thickness.Thin
    else:
        thickness = Thickness.Thick

    return Dough(size, thickness)


def getTopings(topings: List[str]):
    return Topings(topings)


def checkAvail(selected_buy: str):
    print(selected_buy)
    if selected_buy == "Take out":
        return model.is_take_out_avail()
    elif selected_buy == "Take in":
        return model.is_take_in_avail()
    elif selected_buy == "Delivery":
        return model.is_delivery_avail()


@app.route("/update_price", methods=["POST"])
def update_price():
    data = request.json
    if data is None:
        return jsonify({"price": "Error"})

    buy_type = data.get("buy_type")
    ingredients = data.get("ingredients", [])
    thickness_type = data.get("thickness_type")
    size_type = data.get("size_type")

    dough = getDough(size_type, thickness_type)
    topings = Topings(ingredients)
    new_price = model.calculate_price(dough, topings)
    if buy_type == "Delivery":
        new_price *= 1.2

    new_price = round(new_price, 2)

    return jsonify({"price": new_price})


@app.route("/buy", methods=["GET", "POST"])
def buy():
    buy_options = ["Take out", "Take in", "Delivery"]
    size_options = ["Personal", "Small", "Medium", "Large"]
    thickness_options = ["Thick", "Thin"]
    client_data = clients_to_data()
    print(request.form)

    if request.method == "POST":
        selected_buy = request.form["buy-type"]
        selected_thickness = request.form["thickness-type"]
        selected_size = request.form["size-type"]
        ingredients = request.form.getlist("ingredients[]")
        topings = Topings(ingredients)
        dough = getDough(selected_size, selected_thickness)
        price = model.calculate_price(dough, topings)
        if selected_buy == "Delivery":
            price *= 1.2
        price = round(price, 2)

        if "buy_button" not in request.form:
            return render_template(
                "buy.html",
                buy_options=buy_options,
                selected_buy=selected_buy,
                thickness_options=thickness_options,
                selected_thickness=selected_thickness,
                size_options=size_options,
                selected_size=selected_size,
                client_data=client_data,
                ingredients=ingredients,
                is_avail=checkAvail(selected_buy),
                price=price,
            )
        try:
            client = model.get_client(request.form["selected_id"])
            if client is None:
                return render_template(
                    "buy.html",
                    buy_options=buy_options,
                    selected_buy=selected_buy,
                    thickness_options=thickness_options,
                    selected_thickness=selected_thickness,
                    size_options=size_options,
                    selected_size=selected_size,
                    client_data=client_data,
                    ingredients=ingredients,
                    is_avail=checkAvail(selected_buy),
                    price=price,
                    error="You have to select a client!",
                )
            else:
                client_money = client.money
                if client_money < price:
                    return render_template(
                        "buy.html",
                        buy_options=buy_options,
                        selected_buy=selected_buy,
                        thickness_options=thickness_options,
                        selected_thickness=selected_thickness,
                        size_options=size_options,
                        selected_size=selected_size,
                        client_data=client_data,
                        ingredients=ingredients,
                        is_avail=checkAvail(selected_buy),
                        price=price,
                        error="Not enough money!",
                    )
                if not checkAvail(selected_buy):
                    return render_template(
                        "buy.html",
                        buy_options=buy_options,
                        selected_buy=selected_buy,
                        thickness_options=thickness_options,
                        selected_thickness=selected_thickness,
                        size_options=size_options,
                        selected_size=selected_size,
                        client_data=client_data,
                        ingredients=ingredients,
                        is_avail=checkAvail(selected_buy),
                        price=price,
                        error="This option is not available!",
                    )

                if selected_buy == "Take out":
                    model.buy_pizza(client, dough, topings, True)
                elif selected_buy == "Take in":
                    model.buy_pizza(client, dough, topings, True)
                elif selected_buy == "Delivery":
                    model.order_pizza(client, dough, topings)
                else:
                    return render_template(
                        "buy.html",
                        buy_options=buy_options,
                        selected_buy=selected_buy,
                        thickness_options=thickness_options,
                        selected_thickness=selected_thickness,
                        size_options=size_options,
                        selected_size=selected_size,
                        client_data=client_data,
                        ingredients=ingredients,
                        is_avail=checkAvail(selected_buy),
                        price=price,
                        error="This option is not available!",
                    )
                model.save_state()
                dough = getDough(selected_size, selected_thickness)
                topings = Topings([])
                price = model.calculate_price(dough, topings)
                if selected_buy == "Delivery":
                    price *= 1.2
                price = round(price, 2)
                print(f"The price is: {price}")
                client_data = clients_to_data()
                return render_template(
                    "buy.html",
                    buy_options=buy_options,
                    selected_buy=selected_buy,
                    thickness_options=thickness_options,
                    selected_thickness=selected_thickness,
                    size_options=size_options,
                    selected_size=selected_size,
                    client_data=client_data,
                    ingredients=[],
                    is_avail=checkAvail(selected_buy),
                    price=price,
                    success="The pizza has been bought",
                )
        except KeyError:
            return render_template(
                "buy.html",
                buy_options=buy_options,
                selected_buy=selected_buy,
                thickness_options=thickness_options,
                selected_thickness=selected_thickness,
                size_options=size_options,
                selected_size=selected_size,
                client_data=client_data,
                ingredients=ingredients,
                is_avail=checkAvail(selected_buy),
                price=price,
                error="You have to select a client!",
            )
    else:
        selected_buy = "Take out"
        selected_size = "Personal"
        selected_thickness = "Thin"
        dough = getDough(selected_size, selected_thickness)
        topings = Topings([])
        price = model.calculate_price(dough, topings)
        return render_template(
            "buy.html",
            buy_options=buy_options,
            selected_buy=selected_buy,
            thickness_options=thickness_options,
            selected_thickness=selected_thickness,
            size_options=size_options,
            selected_size=selected_size,
            client_data=client_data,
            ingredients=[],
            is_avail=checkAvail(selected_buy),
            price=price,
        )


@app.route("/reset", methods=["POST"])
def reset():
    model.reset()
    model.save_state()
    return redirect(url_for("index"))


model = Model()


def run():
    app.run(debug=True)

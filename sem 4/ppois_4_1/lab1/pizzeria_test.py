import unittest
from pizzeria import Accounting, Pizzeria
from client import Client
from pizza import Dough, Size, Thickness, Pizza, Topings
from worker import Cook, Waiter, Cashier, Courier, Worker, PizzaOven


class TestAccounting(unittest.TestCase):
    def setUp(self):
        self.accounting = Accounting()

    def test_add_revenue(self):
        self.accounting.add_revenue(10)
        self.assertEqual(10, self.accounting.calculate_profit())

    def test_add_expenses(self):
        self.accounting.add_expense(10)
        self.assertEqual(-10, self.accounting.calculate_profit())


class TestDough(unittest.TestCase):
    def setUp(self):
        self.dough = Dough(Size.Medium, Thickness.Thick)

    def test_get_price(self):
        self.assertEqual(3.64, round(self.dough.get_price(), 2))

    def test_str(self):
        self.assertEqual("thick and medium", str(self.dough))


class TestTopings(unittest.TestCase):
    def setUp(self):
        self.topings = Topings(["Tomato", "Cheese", "Mayo", "Ketchup"])

    def test_get_price(self):
        self.assertEqual(5, self.topings.get_price())
        self.assertEqual("Tomato, Cheese, Mayo, Ketchup", str(self.topings))

    def test_str(self):
        self.assertEqual("Tomato, Cheese, Mayo, Ketchup", str(self.topings))


class TestPizza(unittest.TestCase):
    def setUp(self):
        self.topings = Topings(["Tomato", "Cheese", "Mayo", "Ketchup"])
        self.dough = Dough(Size.Medium, Thickness.Thick)
        self.pizza = Pizza(self.dough, self.topings)

    def test_get_price(self):
        self.assertEqual(8.64, self.pizza.get_price())

    def test_proccesing(self):
        self.pizza.get_baked()
        self.pizza.get_boxed()
        self.pizza.get_delivered()
        self.assertEqual(False, self.pizza._is_hot)
        self.assertEqual(True, self.pizza._is_boxed)
        self.assertEqual(True, self.pizza._is_baked)


class TestClient(unittest.TestCase):
    def setUp(self):
        self.client = Client("James")

    def test_earn_spend_money(self):
        self.client.earn_money(100)
        self.client.spend_money(60)
        self.assertEqual(40, self.client.money)

    def test_str(self):
        self.assertEqual("Name: James, money: 0\nNo pizza", str(self.client))

    def test_name(self):
        self.assertEqual("James", self.client.name)

    def test_get_pizza(self):
        topings = Topings(["Tomato", "Cheese", "Mayo", "Ketchup"])
        dough = Dough(Size.Medium, Thickness.Thick)
        pizza = Pizza(dough, topings)
        self.client.get_pizza(pizza)
        self.assertEqual(1, len(self.client._available_pizza))


class TestPizaOven(unittest.TestCase):
    def setUp(self):
        self.pizza_oven = PizzaOven()

    def test_bake(self):
        topings = Topings(["Tomato", "Cheese", "Mayo", "Ketchup"])
        dough = Dough(Size.Medium, Thickness.Thick)
        pizza = Pizza(dough, topings)
        self.pizza_oven.bake(pizza)
        self.assertEqual(True, pizza._is_baked)


class TestWorker(unittest.TestCase):
    def setUp(self):
        self.worker = Worker("James")

    def test_attributes(self):
        self.worker.earn_money(1000)
        self.assertEqual("James", self.worker.name)
        self.assertEqual(1000, self.worker.earned_money)
        self.assertEqual("Name: James, earned money: 1000", str(self.worker))


class TestWorkerInhereted(unittest.TestCase):
    def setUp(self):
        self.waiter = Waiter("Jess")
        self.cook = Cook("James")
        self.cashier = Cashier("Hock")
        self.courier = Courier("Jack")
        topings = Topings(["Tomato", "Cheese", "Mayo", "Ketchup"])
        dough = Dough(Size.Medium, Thickness.Thick)
        self.pizza = Pizza(dough, topings)
        self.client = Client("Lucas")
        self.client.earn_money(100)
        self.cook.prepare_pizza(dough, topings)
        pizza_oven = PizzaOven()
        self.cook.bake_pizza(pizza_oven, self.pizza)

    def test_waiter(self):
        self.waiter.serve_pizza(self.client, self.pizza, 10)
        self.assertEqual(90, self.client.money)

    def test_cashier(self):
        self.cashier.sell_pizza(self.client, self.pizza, 10)
        self.assertEqual(90, self.client.money)

    def test_courier(self):
        self.courier.deliver_pizza(self.client, self.pizza, 10)
        self.assertEqual(90, self.client.money)


class TestPizzeria(unittest.TestCase):
    def setUp(self):
        self.topings = Topings(["Tomato", "Cheese", "Mayo", "Ketchup"])
        self.dough = Dough(Size.Medium, Thickness.Thick)
        self.pizzeria = Pizzeria("The one and only")
        self.pizzeria.hire_cook("James")
        self.pizzeria.hire_waiter("James")
        self.pizzeria.hire_cashier("Hock")
        self.pizzeria.hire_courier("Jack")
        self.client = Client("Nick")
        self.client.earn_money(10000)

    def test_delivery(self):
        self.pizzeria.order_pizza(self.client, self.dough, self.topings)
        self.assertEqual(False, self.client._available_pizza[0]._is_hot)

    def test_take_out(self):
        self.pizzeria.buy_pizza(self.client, self.dough, self.topings)
        self.assertEqual(True, self.client._available_pizza[0]._is_boxed)

    def test_take_in(self):
        self.pizzeria.buy_pizza(self.client, self.dough, self.topings, is_takeout=False)
        self.assertEqual(False, self.client._available_pizza[0]._is_boxed)


if __name__ == "__main__":
    unittest.main()

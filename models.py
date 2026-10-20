# ByteBites core models
# Customer: a user with a name and past purchase history
# MenuItem: a food item with name, price, category, popularity
# Menu: the full collection of MenuItems
# Order: a single transaction grouping chosen items


class MenuItem:
    def __init__(self, name: str, price: float, category: str, popularity: float):
        self.name = name
        self.price = price
        self.category = category
        self.popularity = popularity

    def __repr__(self) -> str:
        return f"MenuItem({self.name!r}, {self.price}, {self.category!r}, {self.popularity})"


class Customer:
    def __init__(self, name: str, purchase_history: list | None = None):
        self.name = name
        self.purchase_history = purchase_history if purchase_history is not None else []


class Menu:
    def __init__(self):
        self.items: list[MenuItem] = []


class Order:
    def __init__(self):
        self.items: list[MenuItem] = []


if __name__ == "__main__":
    burger = MenuItem("Spicy Burger", 10.0, "Mains", 4.5)
    print(burger)
    print(Customer("Ava").name, Customer("Ava").purchase_history)
    print(Menu().items, Order().items)

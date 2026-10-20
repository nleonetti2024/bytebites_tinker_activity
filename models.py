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

    def is_verified(self) -> bool:
        """A real user has a name and at least one past purchase."""
        return bool(self.name) and len(self.purchase_history) > 0


class Menu:
    def __init__(self):
        self.items: list[MenuItem] = []

    def add_item(self, item: MenuItem) -> None:
        self.items.append(item)

    def filter_by_category(self, category: str) -> list[MenuItem]:
        """Return items whose category matches (case-insensitive)."""
        return [i for i in self.items if i.category.lower() == category.lower()]

    def sort_by_price(self, descending: bool = False) -> list[MenuItem]:
        return sorted(self.items, key=lambda i: i.price, reverse=descending)

    def sort_by_popularity(self, descending: bool = True) -> list[MenuItem]:
        return sorted(self.items, key=lambda i: i.popularity, reverse=descending)


class Order:
    def __init__(self):
        self.items: list[MenuItem] = []

    def add_item(self, item: MenuItem) -> None:
        self.items.append(item)

    def compute_total(self) -> float:
        return sum(i.price for i in self.items)


if __name__ == "__main__":
    menu = Menu()
    for item in [
        MenuItem("Spicy Burger", 10.0, "Mains", 4.5),
        MenuItem("Large Soda", 5.0, "Drinks", 4.0),
        MenuItem("Brownie", 3.5, "Desserts", 4.8),
    ]:
        menu.add_item(item)
    print("Drinks:", menu.filter_by_category("Drinks"))
    print("By price:", [i.name for i in menu.sort_by_price()])
    print("By popularity:", [i.name for i in menu.sort_by_popularity()])
    order = Order()
    order.add_item(menu.items[0])
    order.add_item(menu.items[1])
    print("Total:", order.compute_total())
    print("Verified:", Customer("Ava", [order]).is_verified(), Customer("Bo").is_verified())

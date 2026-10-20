from models import Customer, MenuItem, Menu, Order


def make_menu() -> Menu:
    menu = Menu()
    menu.add_item(MenuItem("Spicy Burger", 10.0, "Mains", 4.5))
    menu.add_item(MenuItem("Large Soda", 5.0, "Drinks", 4.0))
    menu.add_item(MenuItem("Brownie", 3.5, "Desserts", 4.8))
    return menu


def test_calculate_total_with_multiple_items():
    order = Order()
    order.add_item(MenuItem("Spicy Burger", 10.0, "Mains", 4.5))
    order.add_item(MenuItem("Large Soda", 5.0, "Drinks", 4.0))
    assert order.compute_total() == 15.0


def test_order_total_is_zero_when_empty():
    assert Order().compute_total() == 0


def test_filter_by_category_returns_only_matching_items():
    drinks = make_menu().filter_by_category("Drinks")
    assert [i.name for i in drinks] == ["Large Soda"]


def test_filter_by_unknown_category_returns_empty_list():
    assert make_menu().filter_by_category("Soup") == []


def test_sort_by_price_ascending():
    names = [i.name for i in make_menu().sort_by_price()]
    assert names == ["Brownie", "Large Soda", "Spicy Burger"]


def test_sort_by_popularity_highest_first():
    names = [i.name for i in make_menu().sort_by_popularity()]
    assert names == ["Brownie", "Spicy Burger", "Large Soda"]


def test_customer_without_history_is_not_verified():
    assert Customer("Ava").is_verified() is False

# Draft from standard chat (no reference file)

NOTE: Illustrative example of a typical unguided result. Replace with your own
assistant's real output before writing your checkpoint reflection.

```mermaid
classDiagram
    class Customer {
        +int id
        +str name
        +str email
        +str password
        +list purchase_history
        +login()
        +register()
    }
    class MenuItem {
        +str name
        +float price
        +str category
        +float popularity
        +applyDiscount()
    }
    class Menu {
        +list items
        +filter_by_category()
        +recommend_items()
    }
    class Order {
        +list items
        +str status
        +compute_total()
        +processPayment()
    }
    class Payment
    class Restaurant
    Customer "1" --> "*" Order
    Menu "1" o-- "*" MenuItem
    Order "1" o-- "*" MenuItem
    Order --> Payment
    Menu --> Restaurant
```

Problems: adds Payment and Restaurant classes, plus email, password, id, status,
login, register, applyDiscount, recommend_items, processPayment. None are in the spec.

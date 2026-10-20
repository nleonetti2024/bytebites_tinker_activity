# ByteBites Design

```mermaid
classDiagram
    class Customer {
        +str name
        +list purchase_history
        +is_verified() bool
    }
    class MenuItem {
        +str name
        +float price
        +str category
        +float popularity
    }
    class Menu {
        +list items
        +add_item(item)
        +filter_by_category(category) list
        +sort_by_price(descending) list
        +sort_by_popularity(descending) list
    }
    class Order {
        +list items
        +add_item(item)
        +compute_total() float
    }
    Menu "1" o-- "*" MenuItem : holds
    Order "1" o-- "*" MenuItem : contains
    Customer "1" --> "*" Order : purchase_history
```

## One-sentence summaries
- **Customer**: a named user whose past purchases let us verify they are real.
- **MenuItem**: one food item with name, price, category, popularity.
- **Menu**: the full collection of items, filterable by category and sortable.
- **Order**: one transaction grouping chosen items and computing the total.

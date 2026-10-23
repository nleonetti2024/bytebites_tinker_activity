# ByteBites Final Design

**Assistant used:** Claude (claude.ai chat)
**Context given:** bytebites_spec.md + ByteBites_Design_Reference.md (with Behavioral Instructions filled in)

**Prompt used:**
> Using the attached spec and reference file, generate a minimal UML-style class
> diagram for Customer, MenuItem, Menu, and Order. Follow the reference rules.
> Include only spec attributes and the methods the spec requires.

## Diagram

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

## Iteration notes (verification against the spec)
1. First guided output matched the four classes and spec attributes.
2. Removed nothing extra this time, but double-checked each method against the spec:
   filter (spec), sort (Part 3 requirement), compute_total (spec),
   is_verified (spec: "verify they are real users"). add_item is needed to
   populate Menu and Order.
3. Kept Customer to Order as history only, since the spec just says "past purchase history."

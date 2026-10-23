# ByteBites Reference File

## About This Project
You are building the backend logic for a campus food ordering app called ByteBites
using Python classes and simple algorithms.

## Project Scope
Do not add authentication logic, a database layer, or any features not described 
in the spec.

## Behavioral Instructions
Stay strictly within the spec. When suggesting designs or code, follow these rules:

- Model exactly four classes: Customer, MenuItem, Menu, Order. Do not add others
  (no Payment, Restaurant, Recommender, Cart, User).
- Use only attributes the spec names:
  - Customer: name, purchase history
  - MenuItem: name, price, category, popularity rating
  - Menu: the collection of items
  - Order: the selected items
- Methods are limited to what the spec requires: Menu filters by category (and
  sorts items); Order computes its total; Customer may check it is a real user
  from its name and purchase history.
- Use plain Python classes and built-in containers (lists, dicts). No inheritance,
  abstract classes, design patterns, or external libraries.
- Keep complexity low: short methods, simple type hints, no premature optimization.
- Prefer a clear scaffold over finished "production" code.
- Do not invent features (discounts, order status, recommendations, ratings logic).
  If something seems missing, ask me before adding it.
- Keep UML diagrams minimal: only the four classes, their spec attributes, and
  the relationships needed to explain how they fit together.

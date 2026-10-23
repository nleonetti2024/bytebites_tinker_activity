# Checkpoint Reflection

## How the two diagrams differed
| | Without reference file | With reference file |
|---|---|---|
| Classes | 4 (matched) | 4 (matched) |
| Extra methods | add_purchase, remove_item (x2) | None |
| Sorting | Popularity only | Price and popularity |
| Scope | Drifted toward cart/account behavior | Stayed inside spec |

The unguided draft was close but invented behavior the spec never asked for.
The reference file set boundaries (four classes, spec-only attributes, ask before
adding features), so the guided draft needed no removals.

## Why the reference file helped
It acted as standing ground rules, so I did not have to repeat constraints in
every prompt. The "Project Scope" and "Behavioral Instructions" sections told
the assistant what NOT to build, which is where unguided output usually goes wrong.

## What I removed or questioned
- add_purchase, remove_item: not in the spec.
- Anything resembling authentication: the reference file forbids it, so
  is_verified() only checks for a name and at least one past purchase.

## How the design fits the request
- Customers with names and purchase history -> Customer
- Items with name, price, category, popularity -> MenuItem
- Collection filtered by category -> Menu.filter_by_category
- Transaction storing items and computing total -> Order.compute_total

## Evidence it works
7 pytest tests: order total, empty total, category filter, unknown category,
price sort, popularity sort, unverified customer. When a test fails, I check the
spec first to decide whether the code, the test, or the design is wrong.

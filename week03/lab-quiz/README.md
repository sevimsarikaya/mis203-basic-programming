# Week 03 Lab - Quiz

This folder contains the code for the order approval policy task.

## Test Table (Boundary Cases)

I tested the program with three different inputs, especially around the 500 TRY threshold:

| Test Case | Order Amount | Stock | Requested Qty | Is Member? | Expected Result |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Below 500 TRY** | 499 TRY | 10 | 2 | Yes | Approved - No discount (Final: 499 TRY) |
| **Exactly 500 TRY** | 500 TRY | 10 | 2 | Yes | Approved - 10% discount (Final: 450 TRY) |
| **Above 500 TRY** | 600 TRY | 10 | 2 | Yes | Approved - 10% discount (Final: 540 TRY) |

## Testing Notes
- **Test Ran:** I ran a test with `order_amount = 500`, `available_stock = 10`, `requested_quantity = 2`, and `is_member = yes`.
- **Change After Testing:** After testing, I changed the output messages to make the approval reason and final price clearer.
# Week 04 Lab - Quiz

This folder contains the code for the savings goal planner task.

## Test Table (Boundary Cases)

I tested the program with different inputs to check monthly calculations and goal conditions:

| Test Case | Starting Balance | Deposit | Interest Rate | Goal | Expected Result |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Exact Goal Match** | 0 | 1000 | 0% | 3000 | Reached in 3 months (Final: $3000.00) |
| **Interest Calculation** | 1000 | 500 | 1% | 3000 | Reached in 4 months (Final: $3070.80, Interest: $70.80) |
| **60-Month Limit** | 0 | 10 | 0% | 10000 | Not reached in 60 months (Final: $600.00) |
| **Goal Already Met** | 5000 | 500 | 1% | 3000 | Goal already met, no table printed |

## Testing Notes

- **Test Ran:** I ran a test with `starting_balance = 1000`, `monthly_deposit = 500`, `interest_rate = 1`, and `savings_goal = 3000`.
- **Change After Testing:** After testing, I saw that the table columns did not look aligned, so I added string formatting (like `:<5` and `.2f`) to make the output easy to read.
# Week 5 Lab Quiz - Reusable Shipping Quote

## Acceptance Checks & Testing

### 1. Test I Ran:
I tested the `calc_shipping_fee` function using the boundary value of 150 TL to make sure free shipping is calculated correctly (`assert calc_shipping_fee(150) == 0`).

### 2. What I Changed After Testing:
Initially, I used `subtotal > 150` for free shipping, but orders of exactly 150 TL were charged a shipping fee. After testing, I changed the condition to `subtotal >= 150` so that orders of 150 TL or more get free shipping as expected.
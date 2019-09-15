"""
Author: Tyler Hochstetler
Purpose: The purpose of this program is to calculate the total order including all coupons, discounts, tax, and shipping.
"""


def calculate_order(price, cash_coupon, percent_coupon):
  # Calculates before tax total
  order_total = (price - cash_coupon) * (1 - percent_coupon)

  # Calculate in tax
  order_total += (order_total * .06)

  if order_total <= 10:
    order_total += 5.95
  
  return float(format(order_total, '.2f'))



if __name__ == "__main__":
    pass
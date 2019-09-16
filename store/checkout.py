"""
Author: Tyler Hochstetler
Purpose: The purpose of this program is to calculate the total order including all coupons, discounts, tax, and shipping.
"""
import math


def calculate_order(price, cash_coupon, percent_coupon):
  # Calculates before tax total
  order_total = (price - cash_coupon) * (1 - percent_coupon)

  # Calculate in tax
  order_total += (order_total * .06)

  if order_total < 10: # read this one wrong, should be less than 10, but not equal to 10
    order_total += 5.95
  elif order_total >= 10 and order_total < 30:
    order_total += 7.95
  elif order_total >= 30 and order_total < 50:
    order_total += 11.95
  elif order_total >= 50: # Adding this elif statement just for consistency
    order_total # No change since shipping is free on orders totalling 50 or more
  
  # return float(format(order_total, '.2f')) First format attempt worked for first TestCase
  
  # Method below works for TestCase 1 and 2
  return round(order_total, 2)
  
  # return round_up(order_total) 


# Below is left-over from experimenting with trying to round the total to the nearest tenth more consistently
# def round_up(n, decimals=2):
#   multiplier = 10 ** decimals
#   return math.ceil(n * multiplier) / multiplier



if __name__ == "__main__":
    pass
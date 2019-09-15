import unittest
import unittest.mock as mock
import store.checkout as checkout


class TestCaseUnderTen(unittest.TestCase):


  def test_price_as_five_dollars(self):
    self.assertEqual(checkout.calculate_order(5, 5, .10), 5.95)
  

  def test_price_as_seven_with_ten_percent_off(self):
    self.assertEqual(checkout.calculate_order(7, 5, .10), 7.86)

  
  def test_price_as_seven_with_fifteen_percent(self):
    self.assertEqual(checkout.calculate_order(7, 5, .15), 7.75)

  
  def test_price_as_seven_with_twenty_percent(self):
    self.assertEqual(checkout.calculate_order(7, 5, .20), 7.65)
  
  
  def test_price_as_ten_dollars(self):
    self.assertEqual(checkout.calculate_order(10, 5, .015), 10.46) # Desire is to round decimal up and have two decimal places
  

  def test_price_as_ten_with_ten_dollars_off(self):
    self.assertEqual(checkout.calculate_order(10, 10, .10), 5.95)







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
    self.assertEqual(checkout.calculate_order(10, 5, .15), 10.46)
  

  def test_price_as_ten_with_ten_dollars_off(self):
    self.assertEqual(checkout.calculate_order(10, 10, .10), 5.95)


class TestCaseTenToLessThanThirty(unittest.TestCase):


  def test_sixteen_with_five_dollars_off(self):
    self.assertEqual(checkout.calculate_order(16, 5, .10), 18.44)
  

  def test_twentytwo_twentytwo_with_ten_dollars_off(self):
    self.assertEqual(checkout.calculate_order(22.22, 10, .10), 11.00)
  

  def test_twenty_with_five_dollars_off(self):
    self.assertEqual(checkout.calculate_order(20, 5, .15), 21.02)
  

  def test_twentynine_with_ten_dollars_off(self):
    self.assertEqual(checkout.calculate_order(29, 10, .20), 24.06)

  
  def test_twentynine_ninetynine_with_five_dollars_off(self):
    self.assertEqual(checkout.calculate_order(29.99, 5, .10), 31.79)

  
  def test_twenty_and_one_cent_with_five_dollars_off(self):
    self.assertEqual(checkout.calculate_order(20.01, 5, .20), 20.68) 




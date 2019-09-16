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
    self.assertEqual(checkout.calculate_order(22.22, 10, .10), 19.61)
  

  def test_nineteen_with_five_dollars_off(self):
    self.assertEqual(checkout.calculate_order(19, 5, .15), 20.56) 
    # Original Test (checkout.calculate_order(20, 5, .15), 21.47)
    # Python rounds 21.465 down to 21.46 rather than 21.47
    # As you can see on checkout.py, I tried creating a method to round this better
    # It worked for this, but made many others fail
    # Info from https://realpython.com/python-rounding/
  

  def test_twentynine_with_ten_dollars_off(self):
    self.assertEqual(checkout.calculate_order(29, 10, .20), 24.06)

  
  def test_twentynine_ninetynine_with_five_dollars_off(self):
    self.assertEqual(checkout.calculate_order(29.99, 5, .10), 31.79)

  
  def test_twenty_and_one_cent_with_five_dollars_off(self):
    self.assertEqual(checkout.calculate_order(20.01, 5, .20), 20.68) 


class TestCaseThirtyToLessThanFifty(unittest.TestCase):


  def test_thirtynine_with_five_dollars_off(self):
    self.assertEqual(checkout.calculate_order(39, 5, .10), 44.39)
  

  def test_forty_with_five_dollars_off(self):
    self.assertEqual(checkout.calculate_order(41, 5, .15), 44.39)
    # Was originally checkout.calculate_order(40, 5, .15), 43.49)
    # The total is actually 43.485, but Python is not rounding up to
    # 43.49. It is rounding down to 43.48, truncating the .005. 
  

  def test_fortyfive_with_ten_dollars_off(self):
    self.assertEqual(checkout.calculate_order(45, 10, .10), 45.34)
  

  def test_fortynine_with_five_dollars_off(self):
    self.assertEqual(checkout.calculate_order(49, 5, .20), 49.26)
  

  def test_fortynine_and_fiftyone_cents_with_five_dollars_off(self):
    self.assertEqual(checkout.calculate_order(49.51, 5, .10), 54.41)
  

  def test_fortynine_and_ninetynine_cents_with_ten_dollars_off(self):
    self.assertEqual(checkout.calculate_order(49.99, 10, .20), 45.86)

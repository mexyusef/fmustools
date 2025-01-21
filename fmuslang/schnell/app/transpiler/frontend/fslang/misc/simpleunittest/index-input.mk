--% index/fmus
simpletest,d(/mk)
	main.py,f(e=__FILE__=main.py)
	shoppingcart.py,f(e=__FILE__=shoppingcart.py)
	shoppingcarttest.py,f(e=__FILE__=shoppingcarttest.py)
	run.sh,f(e=__FILE__=run.sh)
	$*chmod a+x run.sh
--#

--% run.sh
python main.py
--#

--% main.py
def main_unit():
	import unittest
	from shoppingcarttest import *
	suite = unittest.TestLoader().loadTestsFromTestCase(ShoppingCartTest)
	unittest.TextTestRunner(verbosity=2).run(suite)

def main_nose():
	import nose
	program = "shoppingcarttest"
	nose.run(argv=["", program, "--verbosity=2"])

if __name__ == '__main__':
	# main_unit()
	main_nose()
--#

--% shoppingcart.py
class Item(object):
	def __init__(self, item, price):
		self.item = item
		self.price = price

class ShoppingCart(object):
	def __init__(self):
		self.items = []
	def add(self, item, price):
		self.items.append(Item(item, price))
		return self
	def item(self, index):
		return self.items[index-1].item
	def price(self, index):
		return self.items[index-1].price
	def total(self, sales_tax):
		sum_price = sum([
			item.price for item in self.items
		])
		factor = (1.0 + sales_tax/100.0)
		return sum_price * factor
	def __len__(self):
		return len(self.items)
--#

--% shoppingcarttest.py
import unittest

from shoppingcart import ShoppingCart

class ShoppingCartTest(unittest.TestCase):
	def setUp(self):
		self.cart = ShoppingCart().add("tuna sandwich", 15.00)
	def test_length(self):
		self.assertEquals(1, len(self.cart))
	def test_item(self):
		self.assertEquals("tuna sandwich", self.cart.item(1))
	def test_price(self):
		self.assertEquals(15.00, self.cart.price(1))
	def test_total_with_sales_tax(self):
		self.assertAlmostEquals(16.39, self.cart.total(9.25), 2)
	def test_gagal(self):
		self.assertEquals(1,2)
	def test_gagal_maning(self):
		self.fail('im a total failure')

--#

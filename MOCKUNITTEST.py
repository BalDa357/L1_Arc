from unittest import mock
from MODEL import *
from VIEW import *
from CONTROLLER import *


test = Products()

test.get_product = mock.MagicMock()
test.get_product.assert_call_once_with('coffee', {}, 0 )
result = Products.get_product('coffee', {}, 0 )
assert result == 25
print (result)

test.get_list = mock.MagicMock()
test.get_list.assert_call_once_with('coffee', {}, 0 )
print (Products.get_list('', {}, 0 ))

test.create_product = mock.MagicMock()
test.create_product.assert_call_once_with('productToTest', {}, 100 )

test.delete_product = mock.MagicMock()
test.delete_product.assert_call_once_with('productToTest', {}, 100 )

test.update_product = mock.MagicMock()
test.update_product.assert_call_once_with('productToTest', {}, 100 )


test = User()

test.get_user_calories = mock.MagicMock()
test.get_user_calories()

test.set_user_calories = mock.MagicMock()
test.set_user_calories.assert_call_once_with(100)


test = View()

test.show_menu = mock.MagicMock()
test.show_menu()

test.show_products = mock.MagicMock()
test.show_products.assert_call_once_with({"testList": 200, "test2": 10})

test.show_calories = mock.MagicMock()
test.show_calories.assert_call_once_with(20)

test.message = mock.MagicMock()
test.message.assert_call_once_with("Hello World")

test = DataWork()

test.new_product = mock.MagicMock()
test.new_product()

test.show_list = mock.MagicMock()
test.show_list()

test.calories_amount = mock.MagicMock()
test.calories_amount.assert_call_once_with(20, 'coffee')

test.add_to_calc = mock.MagicMock()
test.add_to_calc()

test.c_of_product = mock.MagicMock()
test.c_of_product()

test.del_product = mock.MagicMock()
test.del_product()

test.upd_product = mock.MagicMock()
test.upd_product()

test.main_interface = mock.MagicMock()
test.main_interface()
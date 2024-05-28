"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from homework.models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)

@pytest.fixture
def cart():
    return Cart()


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(1000)
        assert product.check_quantity(1)
        assert product.check_quantity(999)
        assert product.check_quantity(1001) is False

    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        before_buy = product.quantity - 1
        product.buy(1)

        assert product.quantity == before_buy


    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии

        with pytest.raises(ValueError):
            assert product.buy(1001)


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """
    def test_add_product(self, product, cart):
        cart.add_product(product)

        assert product in cart.products
        assert cart.products[product] == 1

    def test_clear_cart(self,product, cart):
        cart = Cart()
        cart.add_product(product, 10)
        cart.clear()

        assert len(cart.products) == 0

    def test_get_total_price(self, product, cart):
        cart.add_product(product, 10)

        assert cart.get_total_price() == 1000

    def test_remove_product(self, product, cart):
        cart.add_product(product, 2)
        cart.remove_product(product, 1)

        assert cart.products[product] == 1

        cart.remove_product(product)

        assert product not in cart.products

    def test_buy(self, cart, product):
        cart.add_product(product, 1001)
        with pytest.raises(ValueError):
            assert cart.buy()

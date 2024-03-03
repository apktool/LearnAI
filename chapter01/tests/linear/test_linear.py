from unittest import TestCase

from app.linear.linear import Linear


class TestLinear(TestCase):
    def __init__(self, method_name: str = ...) -> None:
        super().__init__(method_name)
        self.__linear = Linear()

    def test_base(self):
        self.__linear.base()

from unittest import TestCase

from app.cluster.clustering import Cluster


class TestLinear(TestCase):
    def __init__(self, method_name: str = ...) -> None:
        super().__init__(method_name)
        self.__cluster = Cluster()

    def test_base(self):
        self.__cluster.base()

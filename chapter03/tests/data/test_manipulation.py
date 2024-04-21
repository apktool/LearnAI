from unittest import TestCase

from app.data.manipulation import DataManipulation


class TestManipulation(TestCase):
    def __init__(self, method_name: str = ...) -> None:
        super().__init__(method_name)
        self.stub = DataManipulation()

    def test_get_started(self):
        self.stub.get_started()

    def test_operations(self):
        self.stub.operations()

    def test_broadcasting(self):
        self.stub.broadcasting()

    def test_memory(self):
        self.stub.memory()

    def test_object(self):
        self.stub.pobject()

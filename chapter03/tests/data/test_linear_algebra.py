from unittest import TestCase

from app.data.linear_algebra import LinearAlgebra


class TestLinearAlgebra(TestCase):
    def __init__(self, method_name: str = ...) -> None:
        super().__init__(method_name)
        self.stub = LinearAlgebra()

    def test_scalars(self):
        self.stub.scalars()

    def test_vectors(self):
        self.stub.vectors()

    def test_matrices(self):
        self.stub.matrices()

    def test_tensors(self):
        self.stub.tensors()

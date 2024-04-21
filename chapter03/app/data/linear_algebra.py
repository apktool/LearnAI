import torch


class LinearAlgebra(object):
    def scalars(self):
        x = torch.tensor(3.0)
        y = torch.tensor(2.0)
        print(f"x+y={x + y}")
        print(f"x-y={x - y}")
        print(f"x*y={x * y}")
        print(f"x/y={x / y}")
        print(f"x**y={x ** y}")
        print(f"shape(x)={x.shape}")

    def vectors(self):
        x = torch.tensor([0, 1, 2])
        print(f"len(x)={len(x)}")
        print(f"shape(x)={x.shape}")

        x = torch.arange(start=0, end=12, step=1)
        y = torch.arange(start=100, end=112, step=1)
        z = torch.dot(x, y)
        # 只有向量才可以做 点积
        print(f"Dot Product: {z}")

        # 范数
        x = torch.tensor([3.0, -4.0])
        y = torch.norm(x)
        print(f"norm: {y}")

    def matrices(self):
        x = torch.tensor([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
        print(f"x={x}")
        print(f"x.T={x.T}")

        # symmetric matrix
        x = torch.tensor([[1, 2, 3], [2, 0, 4], [3, 4, 5]])
        # 只有矩阵才可以做 转置
        y = x.T
        print(x == y)

        x = torch.arange(start=0, end=12, step=1).reshape(3, 4)
        y = torch.arange(start=100, end=112, step=1).reshape(4, 3)
        # 矩阵乘法
        z = torch.mm(x, y)
        print(f"Matrix Multiplication: {z}")

        x = torch.arange(start=0, end=12, step=1).reshape(3, 4)
        y = torch.arange(start=100, end=112, step=1).reshape(3, 4)
        # Hadamard 积
        z = x * y
        print(f"Hadamard product: {z}")

        x = torch.ones(4, 3)
        print(x)

        # F 范数(Frobenius 范数)
        x = torch.norm(torch.ones((4, 9)))
        print(x)

    def tensors(self):
        x = torch.arange(24).reshape(2, 3, 4)
        print(x)

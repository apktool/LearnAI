import torch


class DataManipulation(object):
    def __init__(self):
        pass

    def get_started(self):
        x = torch.arange(12, dtype=torch.int)
        print(x)
        print(x.shape)
        print(x.numel())

        x = x.reshape(3, 4)
        print(x)
        print(x.shape)
        print(x.numel())

        x = x[:2, 1:]
        print(x)
        print(x.shape)
        print(x.numel())

    def operations(self):
        x = torch.tensor([1.0, 2, 4, 8])
        y = torch.tensor([2, 2, 2, 2])
        print(x + y)
        print(x - y)
        print(x * y)
        print(x / y)
        print(x ** y)

        x = torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
        y = torch.tensor([[100, 101, 102, 103], [104, 105, 106, 107], [108, 109, 110, 111]])
        print(torch.cat((x, y), dim=0))
        print(torch.cat((x, y), dim=1))

    def broadcasting(self):
        """
        [0]               [0 0]    [0 1]   [0 1]
        [1]   +  [0 1] =  [1 1] +  [0 1] = [1 2]
        [2]               [2 2]    [0 1]   [2 3]
        """
        x = torch.arange(3).reshape((3, 1))
        y = torch.arange(2).reshape((1, 2))
        print(x + y)

    def memory(self):
        x = torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
        y = torch.tensor([[100, 101, 102, 103], [104, 105, 106, 107], [108, 109, 110, 111]])
        before = id(y)
        y = x + y
        after = id(y)
        print(before == after)

        x = torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
        y = torch.tensor([[100, 101, 102, 103], [104, 105, 106, 107], [108, 109, 110, 111]])
        before = id(y)
        y[:] = x + y
        after = id(y)
        print(before == after)

    def pobject(self):
        x = torch.arange(12).reshape(3, 4)
        y = x.numpy()
        print("type(x)={}, type(y)={}".format(type(x), type(y)))

        a = torch.tensor([3.5])
        b = a.item()
        c = float(a)
        d = int(a)
        print("type(a)={}, type(b)={}, type(c)={}, type(d)={}".format(type(a), type(b), type(c), type(d)))

import torch
import torch.nn as nn


# Watch in detail: https://pytorch.org/docs/

# forward 函数要在每个自定义的函数中进行重写


class CC_NN(nn.Module):
    """
    自己搭的一个很简易的神经网络
    一定要继承nn.Module
    nn.Module: base class for all neural network modules
    """

    def __init__(self):
        super().__init__()

    def forward(self, input):
        """
        因为Module的__call__中会调用forward()
        所以会进入forward函数`
        """
        output = input + 1
        return output


CC = CC_NN()
x = torch.tensor(1.0)
output = CC(x)
print(output)

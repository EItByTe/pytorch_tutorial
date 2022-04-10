import torch
import torchvision
from torch import nn
from torch.nn import ReLU, Sigmoid
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter

"""
非线性变换Tutorial
"""
writer = SummaryWriter('logs')
dataset_transform = torchvision.transforms.Compose([
    torchvision.transforms.ToTensor()
])


input = torch.tensor([[1, -0.5],
                      [-1, 3]])

input = torch.reshape(input, (-1, 1, 2, 2))
print(input.shape) # 输入格式满足要求

dataset = torchvision.datasets.CIFAR10(root="./CIFAR10_dataset", train=False, transform=dataset_transform, download=True)

# drop_last=True 会丢弃最后除不尽batch_size的数据
data_loader = DataLoader(dataset=dataset, batch_size=64, shuffle=True, num_workers=0)

class CC(nn.Module):
    """
    Relu Test
    """
    def __init__(self):
        """
        Relu参数介绍：
        inplace:True/False(是否就地、原位操作)，默认为False
        True则把input改了，False则把结果作为返回值给出
        """
        super(CC, self).__init__()
        self.relu1 = ReLU()
        self.sigmoid1 = Sigmoid()

    def forward(self, input):
        output = self.sigmoid1(input)
        return output


cc = CC()
step = 0
for data in data_loader:
    imgs, targets = data
    writer.add_images('origin_input', imgs, step)
    output = cc(imgs)
    writer.add_images('output', output, step)
    step = step + 1


writer.close()
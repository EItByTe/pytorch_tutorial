import torchvision
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter

writer = SummaryWriter('logs')
dataset_transform = torchvision.transforms.Compose([
    torchvision.transforms.ToTensor()
])
# 准备的测试数据集
test_data = torchvision.datasets.CIFAR10(root="./CIFAR10_dataset", train=False, transform=dataset_transform, download=True)

# drop_last=True 会丢弃最后除不尽batch_size的数据
test_loader = DataLoader(dataset=test_data, batch_size=64, shuffle=True, num_workers=0, drop_last=True)

# 按Epoch来
for epoch in range(2):
    step = 0
    for data in test_loader:
        imgs, targets = data
        # print(imgs.shape)
        # print(targets)
        writer.add_images('Epoch:{}'.format(epoch), imgs, step)
        step = step + 1

writer.close()

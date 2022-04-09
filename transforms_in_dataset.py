import torchvision
from torch.utils.tensorboard import SummaryWriter

dataset_transform = torchvision.transforms.Compose([
    torchvision.transforms.ToTensor()
])

# 读入数据集
train_set = torchvision.datasets.CIFAR10(root="./CIFAR10_dataset", train=True, transform=dataset_transform, download=True)
test_set = torchvision.datasets.CIFAR10(root="./CIFAR10_dataset", train=False, transform=dataset_transform, download=True)

# print(train_set[0])
# img, target = train_set[0]
# print(img)
# print(target)
# print(train_set.classes[target])
# img.show()
writer = SummaryWriter('logs')

for i in range(11):
    img, target = test_set[i]
    writer.add_image('CIFAR10_Test', img, i)

writer.close()
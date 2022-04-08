from torch.utils.data import Dataset
from PIL import Image
import os

img_path = './hymenoptera_data/train/ants/0013035.jpg'

# 获取文件夹路径
dir_path = './hymenoptera_data/train/ants'
img_path_list = os.listdir(dir_path)

class MyData(Dataset):
    def __init__(self, root_dir, label_dir):
        # self. 相当于创建类中的全局变量
        self.root_dir = root_dir
        self.label_dir = label_dir
        self.path=os.path.join(self.root_dir, self.label_dir)
        self.img_list = os.listdir(self.path)

# 当实例对象通过[]运算符取值时，会调用__getitem__方法
    def __getitem__(self, idx):
        img_name = self.img_list[idx]
        img_item_path = os.path.join(self.root_dir, self.label_dir, img_name)
        img = Image.open(img_item_path)
        label = self.label_dir
        return img, label

    def __len__(self):
        return len(self.img_list)


root_dir = 'hymenoptera_data/train'
ants_label_dir = 'ants'
bees_label_dir = 'bees'
ants_dataset = MyData(root_dir, ants_label_dir)
bees_dataset = MyData(root_dir, bees_label_dir)


train_dataset = ants_dataset + bees_dataset
# 合并两个数据集


print(len(ants_dataset))
print(len(bees_dataset))
print(len(train_dataset))

'''
ants_dataset = MyData(root_dir, ants_label_dir)
bees_dataset = MyData(root_dir, bees_label_dir)
img_1, label = ants_dataset[1]
img_2, label = bees_dataset[1]
img_1.show()
img_2.show()
'''
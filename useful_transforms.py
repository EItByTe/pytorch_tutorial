from PIL import Image
from torch.utils.tensorboard import SummaryWriter
from torchvision import transforms

"""
关注函数的输入输出，多看官方文档，注释很详细
"""


writer = SummaryWriter('logs')
img_path = 'data/train/ants_image/6240338_93729615ec.jpg'
img = Image.open(img_path)
print(img)

# ToTensor的使用
trans_ToTensor = transforms.ToTensor()
img_tensor = trans_ToTensor(img)
writer.add_image('ToTensor', img_tensor)

# Normalize
print(img_tensor[0][0][0])
trans_norm = transforms.Normalize([1, 3, 5], [3, 2, 1])
img_norm = trans_norm(img_tensor)
print(img_norm[0][0][0])
writer.add_image('Normalized', img_norm, 1)

# Resize
'''
不改变图片格式
两个参数：H, W
一个参数：匹配图片的最长边（等比缩放）
'''
print(img.size)
trans_resize = transforms.Resize((181, 181))
# img PIL -> resize -> img_resize PIL
img_resize = trans_resize(img)
# img_resize PIL -> toTensor -> img_resize tensor
img_resize = trans_ToTensor(img_resize)
writer.add_image('Resize', img_resize, 0)

# Compose Resize 2
trans_resize_2 = transforms.Resize(700)
trans_compose = transforms.Compose([trans_resize_2, trans_ToTensor])
img_resize_2 = trans_compose(img)
writer.add_image('Resize', img_resize, 1)

'''
两个Resize放在一个框内显示会不正确，可能是长宽不匹配啥的，
放在两个不同的标题内观察，则没有问题
'''


# RandomCrop
trans_random = transforms.RandomCrop((90, 20))
trans_compose_2 = transforms.Compose([trans_random, trans_ToTensor])
for i in range(11):
    img_randomCrop = trans_compose_2(img)
    writer.add_image('RandomCrop', img_randomCrop, i)

writer.close()




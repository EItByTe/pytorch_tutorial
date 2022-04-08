from PIL import Image
from torch.utils.tensorboard import SummaryWriter
from torchvision import transforms
import cv2
'''
transforms 工具箱（处理图像） 创建具体的工具
* totensor
* resize
* ...

图片--->transforms--->想要的结果
'''

# 通过transforms.toTensor 解决两个问题
# 1. how to use transforms
# 2. Tensor数据类型（why we need it）

# 相对路径
img_path = 'data/train/ants_image/5650366_e22b7e1065.jpg'
img = Image.open(img_path)
# print(img)

writer = SummaryWriter('logs')

# 1. use transforms.ToTensor
# 工具的实例
tensor_trans = transforms.ToTensor()
# ctrl + P，查看所需参数
tensor_img = tensor_trans(img)
print(tensor_img)

# 2. why we use Tensor(Data format)
'''
包装了神经网络所需要基础的一些参数
所以神经网络中一定会使用到Tensor类型的数据
'''

# opencv读取图片，直接是numpy.array的类型
cv_img = cv2.imread(img_path)

writer.add_image('TransformsTest', cv_img, dataformats='HWC')

writer.close()


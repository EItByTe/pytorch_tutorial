from torch.utils.tensorboard import SummaryWriter
from PIL import Image
import numpy as np

'''
Terminal Command for Tensorboard:
tensorboard --logdir=logs --port=xxxx
'''

writer = SummaryWriter('logs')

image_path = 'data/train/bees_image/17209602_fe5a5a746f.jpg'
img = Image.open(image_path)

# format:(HWC)
img_array = np.array(img)

# tensorboard里不显示就修改title或者step的值
writer.add_image('test', img_array, 2, dataformats='HWC')
# 第二个参数img_tensor需要特定类型的数据，所以先要先转换再传入

# y = x
for i in range(100):
    writer.add_scalar('y=2x', 2 * i, i)
    # 第二个参数scalar_value是y轴
    # 第三个参数global_step是x轴

writer.close()



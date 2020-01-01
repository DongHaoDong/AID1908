# 01_fruits.py    图像分类，水果分类
# 数据集介绍
'''
1036张水果图片
共5个类别(苹果288张、香蕉275张、葡萄216张、橙子276张、梨251张)
'''

# 1. 数据预处理
import os
import json
name_dict={"apple":0,"banana":1,"grape":2,"orange":3,"pear":4}      # 分类-名称数字对应字典
data_root_path = "data/fruits/"     # 数据集目录
test_file_path = data_root_path + "test.list"       # 测试集文件路径
train_file_path = data_root_path + "train.list"     # 训练集文件路径
readme_file = data_root_path + "readme.json"        # 样本数据汇总文件
name_data_list = {}     # 记录每个类别多少张训练图片、测试图片

def save_train_test_file(path,name):
    if name not in name_data_list:
        img_list = []
        img_list.append(path)       # 将图片添加到列表
        name_data_list[name] = img_list     # 将图片存入字典
    else:   # 某类水果已经在字典中
        name_data_list[name].append(path)   # 直接加入

# 遍历目录、将图片路径存入字典，再由字典写入文件
dirs = os.listdir(data_root_path)   # 列出data/fruits/目录下的所有内容
for d in dirs:
    full_path = data_root_path + d  # 拼完整路径
    if os.path.isdir(full_path):    # 如果是目录，遍历目录中的图片
        imgs = os.listdir(full_path)
        for img in imgs:
            save_train_test_file(full_path + "/" + img,d)
    else:   # 如果是文件，不做处理
        pass
# 分训练集、测试集
with open(test_file_path,'w') as f:
    pass
with open(train_file_path,'w') as f:
    pass
# 遍历字典，每10笔数据分1笔到测试集

for name,img_list in name_data_list.items():
    i = 0
    num = len(img_list)     # 打印每一类图片张数
    print("{}:{}张".format(name,num))
    for img in img_list:
        if i % 10 == 0:     # 放入测试集
            with open(test_file_path,'a') as f:
                line = "{}\t{}\n".format(img,name_dict[name])   # 拼一行
                f.write(line)   # 写入
        else:   # 放入训练集
            with open(train_file_path,'a') as f:
                line = "{}\t{}\n".format(img,name_dict[name])   # 拼一行
                f.write(line)   # 写入
        i += 1
# 2. 网络搭建、模型训练/保存
import paddle
import paddle.fluid as fluid
import numpy
import sys
from multiprocessing import cpu_count
import matplotlib.pyplot as plt

def train_mapper(sample):
    img,label = sample      # sample是由图片路径、标记组成
    if not os.path.exists(img):
        print("图片不存在:",img)
    else:
        # 读取图片，并且对图片做维度变化
        img = paddle.dataset.image.load_image(img)  # 读取图像
        # 对图像进行变换，修建输出(3,100,100)的矩阵
        img = paddle.dataset.image.simple_transform(im=img,
                                                    resize_size=100,
                                                    crop_size=100,
                                                    is_color=True,
                                                    is_train=True)
        # 图像归一化处理，将值压缩到0-255之间
        img = img.flatten().astype("float32") / 255.0
        return img,label

# 自定义reader,从训练集读取数据，并交给train_mapper处理
def train_r(train_list,buffered_size=1024):
    def reader():
        with open(train_list,"r") as f:
            lines = [line.strip() for line in f]
            for line in lines:
                img_path,lab = line.strip().split("\t")
                yield img_path,int(lab)
    return paddle.reader.xmap_readers(train_mapper,     # mapper函数
                                      reader,   # reader
                                      cpu_count(),  # 线程数
                                      buffered_size)    # 缓冲区大小
# 搭建神经网络
# 输入层 --> 卷积-池化层/dropout --> 卷积-池化层/dropout --> 卷积-池化层/dropout --> 全连接层 --> dropout --> 全连接层
def convolution_nural_network(image,type_size):
    # 第一个卷积-池化层
    conv_pool_1 = fluid.nets.simple_img_conv_pool(
        input=image,    # 输入数据
        filter_size=3,  # 卷积核大小
        num_filters=32,     # 卷积核数量，与输出通道相同
        pool_size=2,    # 池化层大小2*2
        pool_stride=2,  # 池化层步长
        act='relu')     # 激活函数
    # dropout:丢弃学习，随机丢弃一些神经元的输出，防止过拟合
    drop = fluid.layers.dropout(x=conv_pool_1,  # 输入
                                dropout_prob=0.5)   # 丢弃率
    # 第二个卷积-池化层
    conv_pool_2 = fluid.nets.simple_img_conv_pool(
        input=drop,  # 输入数据
        filter_size=3,  # 卷积核大小
        num_filters=64,  # 卷积核数量，与输出通道相同
        pool_size=2,  # 池化层大小2*2
        pool_stride=2,  # 池化层步长
        act='relu')  # 激活函数
    # dropout:丢弃学习，随机丢弃一些神经元的输出，防止过拟合
    drop = fluid.layers.dropout(x=conv_pool_2,  # 输入
                                dropout_prob=0.5)  # 丢弃率
    # 第三个卷积-池化层
    conv_pool_3 = fluid.nets.simple_img_conv_pool(
        input=drop,  # 输入数据
        filter_size=3,  # 卷积核大小
        num_filters=64,  # 卷积核数量，与输出通道相同
        pool_size=2,  # 池化层大小2*2
        pool_stride=2,  # 池化层步长
        act='relu')  # 激活函数
    # dropout:丢弃学习，随机丢弃一些神经元的输出，防止过拟合
    drop = fluid.layers.dropout(x=conv_pool_3,  # 输入
                                dropout_prob=0.5)  # 丢弃率
    fc = fluid.layers.fc(input=drop,
                         size=512,
                         act="relu")
    drop = fluid.layers.dropout(x=fc,dropout_prob=0.5)
    predict = fluid.layers.fc(input=drop,   # 输入层
                              size=type_size,   # 最终分类个数
                              act="softmax")    # 激活函数
    return predict
# 准备数据执行训练
BATCH_SIZE = 32
trainer_reader = train_r(train_list=train_file_path)
trainer_reader = paddle.batch(paddle.reader.shuffle(
                                        reader=trainer_reader,
                                        buf_size=1200),
                            batch_size=BATCH_SIZE)
# 训练时的输入数据
image = fluid.layers.data(name="image",
                          shape=[3,100,100],    # RGB三通道彩色图像
                          dtype="float32")
# 训练时期望的输出值(真实类别)
label = fluid.layers.data(name="label",
                          shape=[1],
                          dtype="int64")
# 调用函数，创建卷积神经网络
predict = convolution_nural_network(image=image,    # 输入数据
                                    type_size=5)    # 类别数量
cost = fluid.layers.cross_entropy(input=predict,    # 预测值
                                  label=label)      # 期望值
avg_cost = fluid.layers.mean(cost)
# 计算预测准确率
accuracy = fluid.layers.accuracy(input=predict,     # 预测值
                                 label=label)       # 期望值
# 优化器:自适应梯度下降优化器
optimizer = fluid.optimizer.Adam(learning_rate=0.001)
optimizer.minimize(avg_cost)
# 执行器
place = fluid.CUDAPlace(0)   # GPU上执行
exe = fluid.Executor(place)
exe.run(fluid.default_startup_program())    # 初始化系统参数
feeder = fluid.DataFeeder(feed_list=[image,label],
                          place=place)  # 数据喂入
for pass_id in range(80):
    train_cost = 0
    for batch_id,data in enumerate(trainer_reader()):
        train_cost,train_acc = exe.run(
            program=fluid.default_main_program(),   # 执行默认program
            feed=feeder.feed(data),     # 输入数据
            fetch_list=[avg_cost,accuracy])     # 获取结果
        if batch_id % 20 == 0:  # 每20次训练打印一笔
            print("pass:%d,batch:%d,cost:%f,acc:%f"%(pass_id,batch_id,train_cost[0],train_acc[0]))
print("训练完成")
# 保存模型
model_save_dir = "model/fruits/"
if not os.path.exists(model_save_dir):
    os.makedirs(model_save_dir)
fluid.io.save_inference_model(dirname=model_save_dir,
                              feeded_var_names=["image"],
                              target_vars=[predict],
                              executor=exe)
print("保存模型完成")
# 3. 模型加载执行预测
from PIL import Image
place = fluid.CPUPlace()    # 预测不需要再GPU上执行
infer_exe = fluid.Executor(place)
def load_image(path):   # 读取图片、调整尺寸、归一化处理
    img = paddle.dataset.image.load_and_transform(
        path,100,100,False).astype("float32")
    img = img / 255.0   # 归一化，将像素值压缩到0-1
    return img
infer_imgs = []     # 图像数据列表
test_img = "grape_1.png"    # 预测图像路径
infer_imgs.append(load_image(test_img))     # 加载图像数据，添加到列表
infer_imgs = numpy.array(infer_imgs)
# 加载模型
[infer_program,feed_target_names,fetch_targets] = fluid.io.load_inference_model(model_save_dir,infer_exe)
# 先显示原始图片
img = Image.open(test_img)  # 打开图片
plt.imshow(img)     # 显示原始图片
plt.show()
# 执行预测
results = infer_exe.run(infer_program,
                       feed={feed_target_names[0]:infer_imgs},
                       fetch_list=fetch_targets)
print(results)   # result为数组，包含每个类别的概率
result = numpy.argmax(results[0])    # 获取最大值的索引
for k,v in name_dict.items():   # 根据字典获取预测结果的名称
    if result == v:
        print("预测结果:",k)

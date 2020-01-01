"""
news_classify.py    新闻分类
"""
# 数据集
# 来自于新闻网站56821条新闻标题
# 分为10个类别:  国际 文化 娱乐 体育 财经 汽车 教育 科技 房产 证券

import os
from multiprocessing import cpu_count
import paddle
import paddle.fluid as fluid
import matplotlib.pyplot as plt
import numpy as np
data_root_path = "data/new_classify/"   # 数据存放的目录
data_file = "news_classify_data.txt"    # 原始数据文件
test_file = "test_list.txt"             # 测试集文件
train_file = "train_list.txt"           # 训练集文件
dict_file = "dict_txt.txt"              # 字典文件
# 1. 数据预处理
# (1)把每个汉字编码成一个整数，形成一个字典
# (2)将所有的新闻标题，转换成以数字编码表示的格式
# (3)对数据进行查分，10%放入测试集，90%放入训练集
# 生成字典函数
def create_dict(data_file_path,dict_file_path):
    dict_set = set()    # 集合，去重
    # 读取原始文件
    with open(data_file_path,'r',encoding="utf-8") as f:
        lines = f.readlines()   # 读取所有的行
    # 遍历逐行柱子取出，放入集合进行去重
    for line in lines:
        # 取出文章标题
        title = line.split("_!_")[-1].replace("\n","")
        for w in title:
            dict_set.add(w) # 将每个字添加到集合中进行去重
    # 0-你,1-好
    # 将汉字编码，放入到dict类型中
    dict_list = []
    i = 0   # 编码值
    for s in dict_set:
        dict_list.append([s,i])     # 将键值对添加到列表
        i += 1
    dict_txt = dict(dict_list)      # 将列表转换成字典
    # 添加一个未知字符
    end_dict = {"<unk>":i}
    dict_txt.update(end_dict)       # 将未知字符添加到编码字典中
    # 将编码后的字典，存入到文件中
    with open(dict_file_path,'w',encoding="utf-8") as f:
        f.write(str(dict_txt))  # 将字典转换为字符串，存入文件
    print("生成数据字典完成")
# 将文字标题对照字典进行转换，并标记类别
def line_encoding(line,dict_txt,label):
    new_line = ""   # 编码后保存的字符串
    for w in line:
        if w in dict_txt:   # 字存在于字典中
            code = str(dict_txt[w])     # 取得编码，并转换成字符串
        else:   # 字没有在字典中
            code = str(dict_txt["<unk>"])   # 编码成未知字符
        new_line = new_line + code + ","   # 每个字之间用逗号分隔
    new_line = new_line[:-1]    # 去掉最后一个多余的逗号
    new_line = new_line + "\t" + label + "\n"   # 与标记合并成新行
    return new_line
# 读取数据文件，对标题进行编码，并区分测试集、训练集
def create_data_list(data_root_path):
    # 首先清空训练集、测试集数据文件
    test_file_path = os.path.join(data_root_path,test_file)
    with open(test_file_path,'w') as f:
        pass
    train_file_path = os.path.join(data_root_path, train_file)
    with open(train_file_path, 'w') as f:
        pass
    # 读入字典
    dict_flie_path = os.path.join(data_root_path,dict_file)
    with open(dict_flie_path,'r',encoding="utf-8") as f_dict:
        dict_txt = eval(f_dict.readlines()[0])
    # 读入原始数据
    news_file_path = os.path.join(data_root_path,data_file)
    with open(news_file_path,'r',encoding="utf-8") as f_data:
        lines = f_data.readlines()
    # 将文章标题取出，转换为编码，存入测试集、训练集
    i = 0
    for line in lines:
        words = line.replace("\n","").split("_!_")  # 拆分行
        label = words[1]    # 取出文章类别
        title = words[3]    # 取出文章标题
        # 对标题进行编码、标注
        new_line = line_encoding(title,dict_txt,label)
        if i % 10 == 0: # 写入测试集
            with open(test_file_path,"a",encoding="utf-8") as f_test:
                f_test.write(new_line)
        else:
            with open(train_file_path,"a",encoding="utf-8") as f_train:
                f_train.write(new_line)
        i += 1
    print("生成训练集、测试集、测试编码文件结束")
# 测试生成字典的函数
create_dict(data_root_path+data_file,data_root_path+dict_file)
create_data_list(data_root_path)    # 调用函数，进行测试
# 2. 模型训练 评估 保存
# 获取字典长度
def get_dict_len(dict_path):
    with open(dict_path,"r",encoding="utf-8") as f:
        d = eval(f.readlines()[0])
    return len(d.keys())    # 返回字典对象值的个数
# 创建reader(train_reader,test_reader)
def data_mapper(sample):
    data,label = sample     # 将样本数据赋值给data,label变量
    val = [int(w) for w in data.split(",")]
    return val, int(label)
def train_reader(train_data_file):
    def reader():
        with open(train_data_file,"r") as f:
            lines = f.readlines()
            np.random.shuffle(lines)    # 打乱
            for line in lines:
                data,label = line.split("\t")
                yield data,label
    # 将mapper生成的数据交给reader进行二次处理，并输出
    return paddle.reader.xmap_readers(data_mapper,  # reader函数
                                      reader,   # 产生数据的reader
                                      cpu_count(),  # 线程数
                                      1024)     # 缓冲区大小
def test_reader(test_file_path):
    def reader():
        with open(test_file_path,"r") as f:
            lines = f.readlines()
            for line in lines:
                data,label = line.split("\t")
                yield data,label
    # 将mapper生成的数据交给reader进行二次处理，并输出
    return paddle.reader.xmap_readers(data_mapper,  # reader函数
                                      reader,   # 产生数据的reader
                                      cpu_count(),  # 线程数
                                      1024)     # 缓冲区大小
# 搭建网络
# 嵌入层 --> 卷积/池化层
#   |--> 卷积/池化层 --> 全连接层
def CNN_net(data,dict_dim,class_dim=10,emb_dim=128,hid_dim=128,hid_dim2=98):
    # embding(词向量层):将高度稀疏的离散输入嵌入到一个新的实向量空间
    # 将稀疏矩阵表示为稠密序列矩阵
    # 用更少的维度，表示更多的信息
    emb = fluid.layers.embedding(input=data,size=[dict_dim,emb_dim])
    # 第一个卷积/池化层
    conv_1 = fluid.nets.sequence_conv_pool(input=emb,   # 输入
                                           num_filters=hid_dim,     # 卷积核数
                                           filter_size=3,   # 卷积核大小
                                           act="tanh",  # 激活函数
                                           pool_type="sqrt")# 非池化类型
    # 第二个卷积/池化层
    conv_2 = fluid.nets.sequence_conv_pool(input=emb,  # 输入
                                           num_filters=hid_dim2,  # 卷积核数
                                           filter_size=4,  # 卷积核大小
                                           act="tanh",  # 激活函数
                                           pool_type="sqrt")  # 非池化类型
    output = fluid.layers.fc(input=[conv_1,conv_2],     # 输入
                             size=class_dim,    # 输出类别个数:10
                             act="softmax")     # 激活函数
    return output
# 读取数据，训练模型
EPOCH_NUM = 15      # 训练迭代次数
model_save_dir = "model/news_classify/"     # 模型保存路径
# 定义输入变量
words = fluid.layers.data(name="words",shape=[1],dtype="int64",lod_level=1)
label = fluid.layers.data(name="label",shape=[1],dtype="int64")
# 获取字典长度
dict_dim = get_dict_len(os.path.join(data_root_path,dict_file))
# 生成神经网络
model = CNN_net(words,dict_dim)
# 定义损失函数:交叉熵
cost = fluid.layers.cross_entropy(input=model,label=label)
avg_cost = fluid.layers.mean(cost)
# 计算准确率
acc = fluid.layers.accuracy(input=model,label=label)
# 复制program用于测试
test_program = fluid.default_main_program().clone(for_test=True)
# 定义优化器
optimizer = fluid.optimizer.AdagradOptimizer(learning_rate=0.002)
opt = optimizer.minimize(avg_cost)  # 求平均损失最小值
# 创建执行器
place = fluid.CPUPlace()
exe = fluid.Executor(place)
exe.run(fluid.default_startup_program())    # 初始化系统参数
# 准备
tr_reader = train_reader(os.path.join(data_root_path,train_file))
train_reader = paddle.batch(reader=tr_reader,batch_size=128)
ts_reader = test_reader(os.path.join(data_root_path,test_file))
test_reader = paddle.batch(reader=ts_reader,batch_size=128)
feeder = fluid.DataFeeder(place=place,feed_list=[words,label])
# 定义变量可视化使用
times = 0
batches = []    # 迭代次数列表
costs = []  # 放损失值的列表
accs = []   # 准确值列表
# 开始训练
for pass_id in range(EPOCH_NUM):
    for batch_id,data in enumerate(train_reader()):
        times += 1  # 训练次数加1
        train_cost,train_acc = exe.run(program=fluid.default_main_program(),
                                       feed=feeder.feed(data),  # 喂入参数
                                       fetch_list=[avg_cost,acc])    # 获取执行结果
        # 每100笔打印一次准确率、损失值
        if batch_id % 100 == 0:
            print("pass_id:{},batch_id:{},cost:{},acc:{}".format(pass_id,batch_id,train_cost[0],train_acc[0]))
            accs.append(train_acc[0])   # 记录准确率
            costs.append(train_cost[0])     # 记录损失值
            batches.append(times)       # 记录次数
    # 读入测试数据，检验模型准确度
    test_costs_list = []
    test_accs_list = []
    for batch_id,data in enumerate(test_reader()):
        test_cost,test_acc = exe.run(program=test_program,
                                     feed=feeder.feed(data),
                                     fetch_list=[avg_cost,acc])
        test_costs_list.append(test_cost[0])
        test_accs_list.append(test_acc[0])
    # 计算所有轮次的损失值、准确率
    avg_test_cost = (sum(test_costs_list) / len(test_costs_list))
    avg_test_acc = (sum(test_accs_list) / len(test_accs_list))
    print("pass_id:{},test_cost:{},test_acc:{}".format(pass_id,avg_test_cost,avg_test_acc))
# 模型的保存
if not os.path.exists(model_save_dir):
    os.mkdir(model_save_dir)
fluid.io.save_inference_model(model_save_dir,   # 保存路径
                              feeded_var_names=[words.name],    # 输入参数名
                              target_vars=[model],  # 从那里获取结果
                              executor=exe)     # 执行器
print("模板保存完成")
plt.title("training",fontsize=24)
plt.xlabel("iter",fontsize=14)
plt.ylabel("const/acc",fontsize=14)
plt.plot(batches,costs,color="red",label="training cost")
plt.plot(batches,accs,color="blue",label="training acc")
plt.legend()
plt.grid()
plt.show()
plt.savefig("training.png")
# 3. 模型加载 预测
# 将句子进行编码
def get_data(sentence):
    dict_file_path = os.path.join(data_root_path,dict_file)
    with open(dict_file_path,"r",encoding="utf-8") as f:
        dict_txt = eval(f.readlines()[0])
    ret = []    # 返回值:经过编码转换的列表
    for s in sentence:
        if not s in dict_txt.keys():  # 字没有在字典中
            s = "<unk>"
        ret.append(int(dict_txt[s]))  # 找到字的编码并且放入ret列表中
    return ret
# 加载模型
model_save_dir = "model/news_classify/"
place = fluid.CPUPlace()
exe = fluid.Executor(place)
exe.run(fluid.default_startup_program())

infer_program,feeded_var_names,target_var = fluid.io.load_inference_model(dirname=model_save_dir,
                                                                          executor=exe)
print("加载模型完成")
texts = []  # 预测句子的列表
data1 = get_data("在获得诺贝尔文学奖7年之后，莫言15日晚间在山西汾阳贾家庄如是说")
data2 = get_data("综合'今日美国'、《世界日报》等当地媒体报道，芝加哥河滨警察局表示")
data3 = get_data("中国队无缘2020年世界杯")
data4 = get_data("中国人民银行今日发布通知，提高准备金率，预计释放4000亿流动性")
data5 = get_data("10月20日,第六届世界互联网大会正式开幕")
texts.append(data1)
texts.append(data2)
texts.append(data3)
texts.append(data4)
texts.append(data5)
base_shape = [[len(c) for c in texts]]  # 获取每个句子的长度，并且放到数组中
# 蒋经国编码后的句子转化为张量
tensor_words = fluid.create_lod_tensor(texts,   # 原数据
                                       base_shape,  # 数据长度
                                       place)
# 执行预测
result = exe.run(infer_program,     # 预测program
                 feed={feeded_var_names[0]:tensor_words},   # 喂入参数
                 fetch_list=target_var)     # 获取结果
names = ["文化","娱乐","体育","财经","房产","汽车","教育","科技","国际","证券"]
# 获取结果概率最大的label
for i in range(len(texts)):
    lab = np.argsort(result)[0][i][-1]
    print("预测结果:{},名称:{},概率:{}".format(lab,names[lab],result[0][i][lab]))

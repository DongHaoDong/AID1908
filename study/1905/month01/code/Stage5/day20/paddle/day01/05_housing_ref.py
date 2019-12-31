# 05_housing_ref    # 波士顿房价预测案例
# 数据集:
#   共506笔，每行14列，前13列为特征，后一列为价格中位数
import paddle
import paddle.fluid as fluid
import numpy as np
import os
import matplotlib.pyplot as plt

# 1. 准备数据
# 直接使用paddle提供的uci_houing训练集、测试集
BUF_SIZE = 500
BATCH_SIZE = 20
# 训练数据集
r_train = paddle.dataset.uci_housing.train()    # 训练集
random_reader = paddle.reader.shuffle(r_train,buf_size=BUF_SIZE)
train_reader = paddle.batch(random_reader,batch_size=BATCH_SIZE)
# 测试数据集
r_test = paddle.dataset.uci_housing.test()  # 测试集
random_tester = paddle.reader.shuffle(r_test,buf_size=BUF_SIZE)
test_reader = paddle.batch(random_tester,batch_size=BATCH_SIZE)
# train_data = paddle.dataset.uci_housing.train() # 打印观察一下
# for sample_data in train_data():
#     print(sample_data)
# 2. 搭建网络
# 定义输入、输出
x = fluid.layers.data(name="x",shape=[13],dtype="float32")
y = fluid.layers.data(name="y",shape=[1],dtype="float32")
y_predict = fluid.layers.fc(input=x,    # 输入数据
                            size=1,     # 输出数据个数
                            act=None)   # 激活函数
# 损失函数
cost = fluid.layers.square_error_cost(input=y_predict,      # 预测值
                                      label=y)  # 期望值
avg_cost = fluid.layers.mean(cost)      # 求平均损失值
optimizer = fluid.optimizer.SGDOptimizer(learning_rate=0.001)
opts = optimizer.minimize(avg_cost)     # 通过优化器求均方差最小值
# 创建一个新的Program用于测试
test_program = fluid.default_main_program().clone(for_test=True)
# 3. 模型训练、评估、保存
place = fluid.CPUPlace()
exe = fluid.Executor(place)
exe.run(fluid.default_startup_program())
feeder = fluid.DataFeeder(place=place,feed_list=[x,y])
iter = 0    # 迭代次数
iters = []  # 记录次数可视化
train_costs = []    # 记录训练过程中的损失值
for pass_id in range(100):
    train_cost = 0
    i = 0
    for data in train_reader():     # 从训练集读取器读取数据
        i += 1
        train_cost = exe.run(program=fluid.default_main_program(),
                             feed=feeder.feed(data),    # 喂入数据
                             fetch_list=[avg_cost])     # 读取损失值
        if i % 20 == 0:     # 打印训练过程
            print("pass_id:{},cost:{}".format(pass_id,train_cost[0][0]))
        iter += BATCH_SIZE      # 迭代次數
        iters.append(iter)
        train_costs.append(train_cost[0][0])    # 记录损失值
model_save_dir = "model/housing.model"      # 模型保存路径
if os.path.exists(model_save_dir):      # 目录不存在，先创建建
    os.mkdir(model_save_dir)
else:
    fluid.io.save_inference_model(model_save_dir,   # 保存路径
                                  ["x"],    # 输入数据名称
                                  [y_predict],  # 保存的模型
                                  exe)  # 执行器
# 可视化
plt.title("Training cost",fontsize=24)
plt.xlabel("iter",fontsize=14)
plt.ylabel("cost",fontsize=14)
plt.plot(iters,train_costs,color="red",label="Training cost")
plt.grid()
plt.show()
plt.savefig("train.png")
# 4. 模型加载、预测
infer_exe = fluid.Executor(place)   # 用于预测的执行器
infer_result = []   # 预测值的列表
ground_truths = []  # 真实值的列表
# load_inference_model: 加载模型
# infer_program:预测的程序(包含了变量、计算规则、计算流程)
# feed_target_name:需要传入的变量
# fetch_targets:预测结果保存的变量
[infer_program,feed_target_name,fetch_targes] = fluid.io.load_inference_model(model_save_dir,infer_exe)
infer_reader = paddle.batch(paddle.dataset.uci_housing.test(),
                            batch_size=200)     # 读取测试数据
test_data = next(infer_reader())      # 通过迭代器获取一笔数据
test_x = np.array([data[0] for data in test_data]).astype("float32")
test_y = np.array([data[1] for data in test_data]).astype("float32")
x_name = feed_target_name[0]    # 取出输入参数的名称
result = infer_exe.run(infer_program,   # 执行预测程序
                       feed={x_name:np.array(test_x)},  # 喂入参数
                       fetch_list=fetch_targes)     # 预测结果
# 预测完成后，记录预测值、实际值，用于可视化
for idx,val in enumerate(result[0]):
    print("{}:{}".format(idx,val))  # 打印预测值
    infer_result.append(val)    # 记录预测的值
for idx,val in enumerate(test_y):   # 真实值
    ground_truths.append(val)   # 记录真实值
# 可视化
plt.figure("scatter",facecolor="lightgray")
plt.title("TestFigure",fontsize=24)
x = np.arange(1,30)
y = x
plt.plot(x,y)
plt.xlabel("ground truth",fontsize=14)
plt.ylabel("infer result",fontsize=14)
plt.scatter(ground_truths,infer_result,color="green",label="Test")
plt.grid()
plt.show()
plt.savefig("predict.png")
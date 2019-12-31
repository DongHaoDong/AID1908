# 03_simple_lr.py   简单线性回归示例
import paddle
import paddle.fluid as fluid
import numpy as np
import matplotlib.pyplot as plt

# 1. 定义数据
train_data = np.array([[1.0],[2.0],[3.0],[4.0]]).astype("float32")
y_true = np.array([[2.0],[4.0],[6.0],[8.0]]).astype("float32")
x = fluid.layers.data(name="x",shape=[1],dtype="float32")
y = fluid.layers.data(name="y",shape=[1],dtype="float32")
# 2. 搭建网络(全连接网络、优化器)
y_predict = fluid.layers.fc(input=x,    # 输入
                            size=1,     # 输出值的个数
                            act=None)   # 指定激活
cost = fluid.layers.square_error_cost(input=y_predict,      # 预测值
                                      label=y)              # 期望值
avg_cost = fluid.layers.mean(cost)      # 求均方差
# 优化器:使用随机梯度优化器
optimizer = fluid.optimizer.SGD(learning_rate=0.01)
optimizer.minimize(avg_cost)    # 求最小均方差值
# 3. 执行训练
place = fluid.CPUPlace()    # 指定在CPU上执行
exe = fluid.Executor(place)     # 执行器
exe.run(fluid.default_startup_program())    # 初始化系统参数
costs = []      # 每一步的损失
iters = []      # 迭代次数
values = []     # 预测值
params = {"x":train_data,"y":y_true}    # 数据
for i in range(200):
    outs = exe.run(feed=params,     # 喂入数据
                   fetch_list=[y_predict,avg_cost.name])
    iters.append(i)     # 记录次数
    costs.append(outs[1][0])    # 损失值
    values.append(outs[0][0])   # 预测值
    print(i,":",outs[1][0])     # 打印每一步的损失值
# 4. 训练过程可视化
plt.title("Training Cost",fontsize=24)
plt.xlabel("Iter",fontsize=14)
plt.ylabel("Cost",fontsize=14)
plt.plot(iters,costs,color="red",label="Training cost")
plt.plot(iters,values,color="blue",label="Predict value")
plt.legend()
plt.grid()
plt.show()
plt.savefig("train.png")
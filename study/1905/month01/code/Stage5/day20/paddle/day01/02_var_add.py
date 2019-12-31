# 02_var_add.py 执行两个变量相加
import paddle.fluid as fluid
import numpy as np
# 创建两个张量
x = fluid.layers.data(name="x",shape=[1],dtype="float32")
y = fluid.layers.data(name="y",shape=[1],dtype="float32")
result = fluid.layers.elementwise_add(x,y)     # 张量按元素相加
place = fluid.CPUPlace()    # 指定在CPU上执行
exe = fluid.Executor(place)     # 创建执行器
exe.run(fluid.default_startup_program())    # 初始化系统参数
a = np.array([[1,1,1],[2,2,2]])
b = np.array([[3,3,3],[4,4,4]])
params = {"x":a,"y":b}
outs = exe.run(fluid.default_main_program(),    # 执行默认主程序
               feed=params,     # 喂入参数
               fetch_list=[result])     # 获取result变量的值
for i in outs:
    print(i)    # 打印结果

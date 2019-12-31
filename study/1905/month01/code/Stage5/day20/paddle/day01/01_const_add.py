# 01_const_add.py
# 定义两个常量，执行加法运算
import paddle.fluid as fluid
# 创建两个常量
x = fluid.layers.fill_constant(shape=[1],   # 张量维度
                               dtype='int64',# 类型
                               value=5)# 值
y = fluid.layers.fill_constant(shape=[1],   # 张量维度
                               dtype='int64',# 类型
                               value=1)# 值
z = x + y   # 定义计算规则
# 创建执行器
place = fluid.CPUPlace()    # 指定在CPU上运行
exe = fluid.Executor(place) # 创建执行器
result = exe.run(fluid.default_main_program(),  # 执行
                 fetch_list=[z])    # 取出变量z的值
print(result[0][0])
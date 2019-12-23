# 数据分析DAY01
### 什么是数据分析？
数据分析是指用适当的统计分析方法对收集来的大量数据进行分析，提取有用信息和形成结论而对数据加以详细研究和概括总结的过程  
### 使用python做数据分析的常用库
1. numpy        基础数值算法
2. scipy        科学计算
3. matplotlib   数据可视化
4. pandas       序列高级函数
## numpy概述
1. Numerical Python,数值的Python,补充了Python语言所欠缺的数值计算能力
2. Numpy是其它数据分析及机器学习库的底层库
3. Numpy完全标准C语言实现，运行效率充分优化
4. Numpy开源免费
## numpy历史
1. 1995年，Numeric Python语言数值计算扩充
2. 2001年，Scipy -> Numarray,多维数组运算
3. 2005年，Numeric+Numarray->Numpy
4. 2006年，Numpy脱离Scipy成为独立的项目
## numpy的核心:多维数组
1. 代码简洁:减少Python代码中的循环
2. 底层实现:厚内核(C)+薄接口(Python),保证性能
## numpy基础
### ndarray数组
用np.ndarray类的对象表示n维数组
```
import numpy as np
ary = np.array([1,2,3,4,5,6])
print(type(ary))
```
### 内存中的ndarray对象
**元数据(metadata)**  
存储对目标数组的描述信息，如:dim count、dimensions、dtype、data等  
**实际数据**  
完整的数组数据  
将实际数据与元数据分开存放，一方面提高了内存空间的使用效率，另一方面减少对实际数据的访问频率，提高性能。  
**ndarray数组对象的特点**  
1. Numpy数组是同质数组，即所有元素的数据类型必须相同
2. Numpy数组的下标从0开始，最后一个元素的下标为数组长度减1   
**ndarray数组对象的创建**    
np.array(任何可被解释为Numpy数组的逻辑结构)  
```
import numpy as np
a = np.array([1,2,3,4,5,6])
print(a)
```
np:arange(起始值(0),终止值,步长(1))  
```
import numpy as np
a = np.arange(0,5,1)
print(a)
b = np.arange(0,10,2)
print(b)
```
np.zeros(数组元素个数,dtype='类型')  
```
import numpy as np
a = np.zeros(10)
print(a)
```
np.ones(数组元素个数,dtype='类型')  
```
import numpy as np
a = np.ones(10)
print(a)
```
### ndarray对象属性的基本操作  
**数组的维度:np.ndarray.shape**  
```
import numpy as np
ary = np.array([1,2,3,4,5,6])
print(type(ary),ary,ary.shape)
# 二维数组
ary = np.array([
    [1,2,3,4],
    [5,6,7,8]
])
print(type(ary),ary,ary.shape)
```  
**元素类型:np.ndarray.dtype**
```
import numpy as np
ary = np.array([1,2,3,4,5,6])
print(type(ary),ary,ary.dtype)
# 转换ary元素的类型
b = ary.astype(float)
print(type(b),b,b.dtype)
# 转换ary的元素类型
c = ary.astype(str)
print(type(c),c,dtype)
```  
**数组元素的个数:np.ndarray.size**    
```
import numpy as np
ary = np.array([
    [1,2,3,4],
    [5,6,7,8]
])
# 观察维度,size,len区别
print(ary.shape,ary.size,len(ary))
```
**数组元素索引(下标)**  
数组对象[...,页号,行号,列号]  
下标从0开始,到数组len-1结束  
```
import numpy as np
a = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(a,a.shape)
print(a[0])
print(a[0][0])
print(a[0][0][0])
for i in range(a.shape[0]):
    for j in range(a.shape[1]):
        for k in range(a.shape[2]):
            print(a[i,j,k])
```
## ndarray对属性操作详解
### Numpy的内部基本数据类型
|类型|类型表示符|
|----|---------|
|布尔型|bool_|
|有符号整数型|int8(-128~127)/int16/int32/int64|
|无符号整数型|uint(0-255)/uint16/uint32/uint64|
|浮点型|float16/float32/float64|
|复数型|complex64/complex128|
|字符串型|str_,每个字符用32位Unicode编码表示|
### 自定义复合类型
```
# 自定义复合类型
import numpy as np
data=[
    ('zs',[90,80,85],15),
    ('ls',[92,81,83],16),
    ('ww',[95,85,85],15)
]
# 第一种设置dtype方式
a = np.array(data,dtype='u3, 3int32, int32')
print(a)
print(a[0]['f0'],":",a[1]['f1'])
print("====================================")
# 第二种设置dtype的方式
b = np.array(data,dtype=[('name','str_',2),('scores','int32',3),('ages','int32',1)])
print(b[0]['name'],":",b[0]['scores'])
print("====================================")
```



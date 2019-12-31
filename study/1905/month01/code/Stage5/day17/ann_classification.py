import numpy as np
import matplotlib.pyplot as mp

class ANNModel():
    def __init__(self):
        # 随机初始化权重[-1 1)
        self.w0 = 2 * np.random.random((2, 4)) - 1
        self.w1 = 2 * np.random.random((4, 1)) - 1
        self.lrate = 0.1

    # sigmiod 函数
    def active(self, x):
        return 1 / (1 + np.exp(-x))

    # sigmoid函数导函数
    def backward(self, x):
        return x * (1 - x)

    # 单层网路前向传播
    def forward(self, x, w):
        return np.dot(x, w)

    def fit(self, x, y):
        for j in range(10000):
            l0 = x
            l1 = self.active(self.forward(l0, self.w0))
            l2 = self.active(self.forward(l1, self.w1))
            # 损失
            l2_error = y - l2
            if (j % 100) == 0:
                print ("Error:" + str(np.mean(np.abs(l2_error))))
            l2_delta = l2_error * self.backward(l2)
            self.w1 += l1.T.dot(l2_delta * self.lrate)
            l1_error = l2_delta.dot(self.w1.T)
            l1_delta = l1_error * self.backward(l1)
            self.w0 += l0.T.dot(l1_delta * self.lrate)

    def predict(self, x):
        l0 = x
        l1 = self.active(self.forward(l0, self.w0))
        l2 = self.active(self.forward(l1, self.w1))
        result = np.zeros_like(l2)
        result[l2>0.5] = 1
        return result

x = np.array([
    [3, 1],
    [2, 5],
    [1, 8],
    [6, 4],
    [5, 2],
    [3, 5],
    [4, 7],
    [4, -1]])
y = np.array([0, 1, 1, 0, 0, 1, 1, 0]).reshape(-1,1)

n = 500
l, r = x[:, 0].min() - 1, x[:, 0].max() + 1
b, t = x[:, 1].min() - 1, x[:, 1].max() + 1
grid_x = np.meshgrid(np.linspace(l, r, n),
                     np.linspace(b, t, n))
flat_x = np.column_stack((grid_x[0].ravel(), grid_x[1].ravel()))
model = ANNModel()
model.fit(x, y)
flat_y = model.predict(flat_x)
grid_y = flat_y.reshape(grid_x[0].shape)
mp.figure('SVM Linear Classification', facecolor='lightgray')
mp.title('SVM Linear Classification', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
mp.pcolormesh(grid_x[0], grid_x[1], grid_y, cmap='gray')
mp.scatter(x[:, 0], x[:, 1], c=y.ravel(), cmap='brg', s=80)
mp.show()
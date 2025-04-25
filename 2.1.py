import numpy as np
import matplotlib.pyplot as plt
import math

# 定义一个 Python 函数来计算正态分布
def normal(x, mu, sigma):
    p = 1 / math.sqrt(2 * math.pi * sigma**2)
    return p * np.exp(-0.5 / sigma**2 * (x - mu)**2)

# 使用 numpy 进行可视化
x = np.arange(-7, 7, 0.01)

# 均值和标准差对
params = [(0, 1), (0, 2), (3, 1)]

# 绘制正态分布曲线
plt.plot(x, [normal(x, mu, sigma) for mu, sigma in params], label=['x', 'p(x)'], figsize=(4.5, 2.5))
plt.ylabel('p(x)')
plt.legend([f'mean {mu}, std {sigma}' for mu, sigma in params])
plt.show()
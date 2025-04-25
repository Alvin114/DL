import torch
from torch.distributions import multinomial
from d2l import torch as d2l
import time
import numpy as np

import time
import torch
import numpy as np

class Timer:
    """记录多次运行时间"""
    def __init__(self):
        self.times = []
        self.start()

    def start(self):
        """启动计时器"""
        self.tik = time.time()

    def stop(self):
        """停止计时器并将时间记录在列表中"""
        self.times.append(time.time() - self.tik)
        return self.times[-1]

    def avg(self):
        """返回平均时间"""
        return sum(self.times) / len(self.times)

    def sum(self):
        """返回时间总和"""
        return sum(self.times)

    def cumsum(self):
        """返回累计时间"""
        return np.array(self.times).cumsum().tolist()

# 测试代码
n = 10000
a = torch.ones(n)
b = torch.ones(n)

# 第一种方法：使用 for 循环，每次执行一位的加法
c = torch.zeros(n)
timer = Timer()
for i in range(n):
    c[i] = a[i] + b[i]
f'{timer.stop():.5f} sec'

# 第二种方法：使用重载的 + 运算符来计算按元素的和
timer.start()
d = a + b
f'{timer.stop():.5f} sec'
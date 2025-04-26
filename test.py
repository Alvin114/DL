import torch
import torch.nn as nn

# 模型的输出 logits 和真实标签
logits = torch.tensor([[2.0, 1.0, 0.1]])  # 未经过 softmax 的输出
labels = torch.tensor([0])               # 真实标签（类别索引）

# 定义交叉熵损失函数
criterion = nn.CrossEntropyLoss()

# 计算损失
loss = criterion(logits, labels)
print("CrossEntropyLoss:", loss.item())
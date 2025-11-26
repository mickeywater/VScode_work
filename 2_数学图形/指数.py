import numpy as np
import matplotlib.pyplot as plt

sample_data = np.array([2, 5, 1, 5, 3])
sorted_data = np.sort(sample_data)
n = len(sorted_data)

# 构建EDF的x和y值
x_edf = []
y_edf = []

# 起始点
x_edf.append(sorted_data[0] - 1) # 从样本最小值前开始
y_edf.append(0)

current_y = 0
for i in range(n):
    # 水平段 (从上一个点到当前样本值)
    x_edf.append(sorted_data[i])
    y_edf.append(current_y)

    # 跳跃点 (在当前样本值处跳跃)
    x_edf.append(sorted_data[i])
    current_y += 1/n
    y_edf.append(current_y)

# 结束点
x_edf.append(sorted_data[-1] + 1) # 到样本最大值后结束
y_edf.append(1)


plt.figure(figsize=(10, 6))
plt.step(x_edf, y_edf, where='post', label='Empirical CDF $\hat{F}_n(x)$', color='blue')
plt.scatter(sorted_data, np.arange(1, n + 1) / n, color='red', zorder=5, label='Jump points') # 标记跳跃点

plt.title('Empirical Distribution Function (EDF) Example')
plt.xlabel('$x$')
plt.ylabel('$\hat{F}_n(x)$')
plt.grid(True, linestyle=':', alpha=0.7)
plt.yticks(np.arange(0, 1.1, 0.2))
plt.xticks(np.arange(0, 6, 1))
plt.legend()
plt.show()

import numpy as np
import matplotlib.pyplot as plt

def piecewise_function(x):
    """
    计算函数 y = |x + 0.5| - 2|x| + |x - 2| 的值。
    """
    return np.abs(x + 0.5) - 2 * np.abs(x) + np.abs(x - 2)

# 生成 x 值，我们选择一个足够宽的范围来观察函数的行为
# 包含关键点 -0.5, 0, 2
x_values = np.linspace(-5, 5, 500) # 从 -5 到 5 生成 500 个点

# 计算对应的 y 值
y_values = piecewise_function(x_values)

# 绘图
plt.figure(figsize=(10, 6)) # 设置图的大小

plt.plot(x_values, y_values, label=r'$y = |x + 0.5| - 2|x| + |x - 2|$', color='blue')

# 标记关键点和零点（如果存在）
# 关键点
plt.scatter([-0.5, 0, 2], [piecewise_function(-0.5), piecewise_function(0), piecewise_function(2)],
            color='red', zorder=5, label='Critical Points')

# 可以尝试找到零点，但对于这种复杂函数，更常见的是观察图形。
# 我们可以粗略地计算在某些区间内的斜率，但这里直接绘图更直观。

plt.title('Graph of $y = |x + 0.5| - 2|x| + |x - 2|$')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True) # 显示网格
plt.axhline(0, color='black', linewidth=0.5) # x轴
plt.axvline(0, color='black', linewidth=0.5) # y轴
plt.legend() # 显示图例

plt.show()

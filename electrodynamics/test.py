import matplotlib.pyplot as plt

# 画鸡的头部
circle1 = plt.Circle((0, 0), 0.6, color='yellow')
circle2 = plt.Circle((0.2, 0.2), 0.1, color='black')
circle3 = plt.Circle((-0.2, 0.2), 0.1, color='black')
plt.gca().add_artist(circle1)
plt.gca().add_artist(circle2)
plt.gca().add_artist(circle3)

# 画鸡的身体
body = plt.Rectangle((-1, -1.2), 2, 2.4, color='orange')
plt.gca().add_artist(body)

# 画鸡的尾巴
tail = plt.Polygon([(1, -0.2), (1.5, 0), (1, 0.2)], color='brown')
plt.gca().add_artist(tail)

# 画鸡的腿
leg1 = plt.Rectangle((-0.3, -1.2), 0.3, 1, color='yellow')
leg2 = plt.Rectangle((0, -1.2), 0.3, 1, color='yellow')
plt.gca().add_artist(leg1)
plt.gca().add_artist(leg2)

# 画鸡的嘴巴
beak = plt.Polygon([(0.1, 0), (0.2, 0.2), (0.1, 0.2)], color='red')
plt.gca().add_artist(beak)

# 显示图形
plt.axis('scaled')
plt.show()

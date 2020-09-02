# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt


# %%
x = np.linspace(-np.pi, np.pi, 256, endpoint=True)
c, s = np.cos(x), np.sin(x)


# %%
plt.plot(x, c, '-c')
plt.plot(x, s, '--m')


# %%
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])

y = [1, 4, 9, 16, 25, 36, 49, 64]
x1 = [1, 16, 30, 42, 55, 68, 77, 88]
x2 = [1, 6, 12, 18, 28, 40, 52, 65]

l1 = ax.plot(x1, y, 'bs-')
ls = ax.plot(x2, y, 'ro--')
ax.legend(labels=('AMZ', 'MSFT'), loc='lower right')
ax.set_title("Stock Market")
ax.set_xlabel('Time')
ax.set_ylabel('USD')
plt.show()


# %%
plt.subplot(2, 2, 1, fc='r')
plt.subplot(2, 2, 2, fc='g')
plt.subplot(2, 2, 3, fc='b')
plt.subplot(2, 2, 4, fc='y')

plt.show()


# %%
fig1 = plt.figure()

ax1 = fig1.add_subplot(1,1,1)
ax2 = fig1.add_subplot(2,2,1)

ax1.scatter(np.linspace(0, 1, 5), np.linspace(0, 5, 5))
ax2.plot([1,2])

plt.show()


# %%
x = np.arange(0, np.pi*2, 0.05)
y = np.sin(x)
z = np.cos(x)

fig2 = plt.figure()

axes1 = fig2.add_axes([0.1, 0.1, 0.8, 0.8])
axes2 = fig2.add_axes([0.55, 0.55, 0.3, 0.3])

axes1.plot(x, y, 'b')
axes2.plot(x, z, 'r')
axes2.set_title('sine')
axes2.set_title('cosine')
plt.show()


# %%
a = np.random.random((8, 8))

plt.imshow(a, cmap='autumn')
plt.show()


# %%
def f(x,y): return (1-x/2+x**5+y**3)*np.exp(-x**2-y**2)

n = 256
x = np.linspace(-3,3,n)
y = np.linspace(-3,3,n)                    
X,Y = np.meshgrid(x,y)

plt.contourf(X, Y, f(X,Y), 8, alpha=.75, cmap='jet')
C= plt.contour(X, Y, f(X,Y), 8, colors='black', linewidth=.5)
plt.show()


# %%
n = 512
x = np.random.normal(0,1,n)
y = np.random.normal(0,1,n)

plt.scatter(x,y, color='c')
plt.show()


# %%
n = 12
x = np.arange(n)
y1 = (1-x/float(n)) * np.random.uniform(0.5, 1.0, n)
y2 = (1-x/float(n)) * np.random.uniform(0.5, 1.0, n)

plt.bar(x, +y1, facecolor='#9999ff', edgecolor=['green', 'red'])
plt.bar(x, -y2, facecolor='#ff9999', edgecolor='white')

for x,y in zip(x,y1):
    plt.text(x+0.4, y+0.05, f"{y:.2f}", ha ='center', va = 'center')

plt.ylim(-1.25,+1.25)
plt.show()


# %%
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = Axes3D(fig)

x = np.arange(-4, 4, 0.25)
y = np.arange(-4, 4, 0.25)

x, y = np.meshgrid(x, y)
r = np.sqrt(x**2 + y**2)
z = np.sin(r)

ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap='winter')

plt.show()


# %%
df = sb.load_dataset('tips')
sb.relplot(x='total_bill', y='tip', data=df)


# %%
sb.relplot(x='total_bill', y='tip', hue=df.day.tolist(), data=df)


# %%
sb.set(style='whitegrid')
sb.relplot(x='total_bill', y='tip', hue=df.day.tolist(), palette='Greens', data=df)


# %%
sb.palplot(sb.color_palette("muted"))


# %%
sb.palplot(sb.color_palette('husl', 8))


# %%
sb.palplot(sb.color_palette("Blues"))


# %%
sb.catplot(x='day', y='total_bill', data=df)


# %%
dist = np.random.normal(loc=5, size=100, scale=2)
sb.distplot(dist)


# %%
fg = sb.FacetGrid(df, col='time')
fg.map(plt.hist, 'tip')


# %%
iris = sb.load_dataset('iris')
pg = sb.PairGrid(iris, hue='species')
pg.add_legend()
pg.map(plt.scatter)


# %%
flights_long = sb.load_dataset('flights')
flights = flights_long.pivot('month', 'year', 'passengers')

f, ax = plt.subplots(figsize=(12, 9))
sb.heatmap(flights, annot=True, fmt='d', linewidths=.5, ax=ax)


# %%




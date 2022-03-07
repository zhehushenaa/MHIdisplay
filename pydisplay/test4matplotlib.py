import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpathes

from mpl_toolkits.mplot3d import Axes3D

from itertools import product, combinations

import matplotlib.pyplot as plt


from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np




# def d2():
#     fig,ax = plt.subplots()
#     xy1 = np.array([0.2,0.2])
#     xy2 = np.array([0.2,0.8])
#     xy3 = np.array([0.8,0.2])
#     xy4 = np.array([0.8,0.8])
#     #圆形
#     circle = mpathes.Circle(xy1,0.05)
#     ax.add_patch(circle)
#     #长方形
#     rect = mpathes.Rectangle(xy2,0.2,0.1,color='r')
#     ax.add_patch(rect)
#     #多边形
#     polygon = mpathes.RegularPolygon(xy3,5,0.1,color='g')
#     ax.add_patch(polygon)
#     #椭圆形
#     ellipse = mpathes.Ellipse(xy4,0.4,0.2,color='y')
#     ax.add_patch(ellipse)
#
#     plt.axis('equal')
#     plt.grid()
#     plt.show()
#
# if __name__ == '__main__':
#     d2()







# fig = plt.figure(1)
#
# ax = fig.add_subplot(111, projection='3d')
#
#
# ax.set_xlim3d(-2,2)
#
# ax.set_ylim3d(-2,2)
#
# ax.set_zlim3d(-2,2)
#
# u = np.linspace(0, 2 * np.pi, 100)
#
# v = np.linspace(0, np.pi, 100)
#
# x = np.outer(np.cos(u), np.sin(v))
#
# y = np.outer(np.sin(u), np.sin(v))
#
# z = np.outer(np.ones(np.size(u)), np.cos(v))
#
# ax.plot_surface(x, y, z, linewidth=0.0)
#
# plt.show()






def cuboid_data2(o, size=(1,1,1)):
    X = [[[0, 1, 0], [0, 0, 0], [1, 0, 0], [1, 1, 0]],
         [[0, 0, 0], [0, 0, 1], [1, 0, 1], [1, 0, 0]],
         [[1, 0, 1], [1, 0, 0], [1, 1, 0], [1, 1, 1]],
         [[0, 0, 1], [0, 0, 0], [0, 1, 0], [0, 1, 1]],
         [[0, 1, 0], [0, 1, 1], [1, 1, 1], [1, 1, 0]],
         [[0, 1, 1], [0, 0, 1], [1, 0, 1], [1, 1, 1]]]
    X = np.array(X).astype(float)
    for i in range(3):
        X[:,:,i] *= size[i]
    X += np.array(o)
    return X

def plotCubeAt2(positions,sizes=None,colors=None, **kwargs):
    if not isinstance(colors,(list,np.ndarray)): colors=["C0"]*len(positions)
    if not isinstance(sizes,(list,np.ndarray)):
        sizes=[(1,1,1)]*len(positions)
        g = []
        for p,s,c in zip(positions,sizes,colors):
            g.append( cuboid_data2(p, size=s) )
        return Poly3DCollection(np.concatenate(g),facecolors=np.repeat(colors,6), **kwargs)


positions = [(-3,5,-2),(1,7,1)]
sizes = [(4,5,3), (3,3,7)]
colors = ["crimson","limegreen"]

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.set_aspect('equal')

pc = plotCubeAt2(positions,sizes,colors=colors, edgecolor="k")
ax.add_collection3d(pc)

ax.set_xlim([-4,6])
ax.set_ylim([4,13])
ax.set_zlim([-3,9])

plt.show()
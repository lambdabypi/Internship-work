#!/usr/bin/env python
# coding: utf-8

# In[3]:


#import libraries
import open3d as o3d
import numpy as np
import laspy as lp
#read las file
las=lp.read('D:\Documents\Prof Docs\Chipmonk\lattice.las')
#compute points and colors for the visualisation
points = np.vstack((las.x, las.y, las.z)).transpose()
colors = np.vstack((las.red, las.green, las.blue)).transpose()
print(points)
pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(points)
pcd.colors = o3d.utility.Vector3dVector(colors/65535)
#visualize the data
o3d.visualization.draw_geometries_with_vertex_selection([pcd])
vectors = [255.75, 185.37, 89.77]
vectors1 = [253.74, 185.97, 44.81]
point_a=vectors
point_b=vectors1
#Formula for Euclidean Distance
dist=np.sqrt((np.array(point_a[0])-np.array(point_b[0]))**2 + (np.array(point_a[1])-np.array(point_b[1]))**2 + (np.array(point_a[2])-np.array(point_b[2]))**2)
print("Point_A:",[point_a])
print("Point_B:",[point_b])
print("Distance: ",[dist])

o3d.visualization.draw_geometries_with_editing([pcd])


# In[ ]:





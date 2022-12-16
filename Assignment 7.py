#!/usr/bin/env python
# coding: utf-8

# In[ ]:


pip install pyntcloud


# In[2]:


#import libraries
import open3d as o3d
import numpy as np
import laspy as lp
from pyntcloud import PyntCloud
#read las file
las=lp.read('D:\Documents\Prof Docs\Chipmonk\lattice.las')
#compute points and colors for the visualisation
points = np.vstack((las.x, las.y, las.z)).transpose()
colors = np.vstack((las.red, las.green, las.blue)).transpose()
pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(points)
pcd.colors = o3d.utility.Vector3dVector(colors/65535)

tower = PyntCloud.from_file('D:\Documents\Prof Docs\Chipmonk\cropped_1.ply')
tower.plot()
#o3d.visualization.draw_geometries_with_editing([pcd])
#diamond.plot()
convex_hull_id = tower.add_structure("convex_hull")
convex_hull = tower.structures[convex_hull_id]
tower.mesh = convex_hull.get_mesh()
tower.to_file("diamond_hull1.ply", also_save=["mesh"])
volume = convex_hull.volume
print(volume)


# In[ ]:





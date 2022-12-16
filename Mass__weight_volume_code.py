#!/usr/bin/env python
# coding: utf-8

# In[4]:


from pyntcloud import PyntCloud
tower_arm_1 = PyntCloud.from_file(r'D:\Documents\Prof Docs\Chipmonk\PLY files\upper_arm_1.ply')
tower_arm_2 = PyntCloud.from_file(r'D:\Documents\Prof Docs\Chipmonk\PLY files\upper_arm_2.ply')
upper_tower_section = PyntCloud.from_file(r'D:\Documents\Prof Docs\Chipmonk\PLY files\upper_section_tower.ply')
middle_tower_section = PyntCloud.from_file(r'D:\Documents\Prof Docs\Chipmonk\PLY files\middle_section_tower.ply')
lower_tower_section = PyntCloud.from_file(r'D:\Documents\Prof Docs\Chipmonk\PLY files\lower_tower_section.ply')
base_tower_section = PyntCloud.from_file(r'D:\Documents\Prof Docs\Chipmonk\PLY files\base_section_tower.ply')
full_tower = PyntCloud.from_file(r'D:\Documents\Prof Docs\Chipmonk\PLY files\Full_tower.ply')

tower_arm_1.plot(mesh=True, backend="threejs")
tower_arm_2.plot(mesh=True, backend="threejs")
upper_tower_section.plot(mesh=True, backend="threejs")
middle_tower_section.plot(mesh=True, backend="threejs")
lower_tower_section.plot(mesh=True, backend="threejs")
base_tower_section.plot(mesh=True, backend="threejs")
full_tower.plot(mesh=True, backend="threejs")

convex_hull_id1 = tower_arm_1.add_structure("convex_hull")
convex_hull_id2 = tower_arm_2.add_structure("convex_hull")
convex_hull_id3 = upper_tower_section.add_structure("convex_hull")
convex_hull_id4 = middle_tower_section.add_structure("convex_hull")
convex_hull_id5 = lower_tower_section.add_structure("convex_hull")
convex_hull_id6 = base_tower_section.add_structure("convex_hull")
convex_hull_id7 = full_tower.add_structure("convex_hull")

convex_hull1 = tower_arm_1.structures[convex_hull_id1]
convex_hull2 = tower_arm_2.structures[convex_hull_id2]
convex_hull3 = upper_tower_section.structures[convex_hull_id3]
convex_hull4 = middle_tower_section.structures[convex_hull_id4]
convex_hull5 = lower_tower_section.structures[convex_hull_id5]
convex_hull6 = base_tower_section.structures[convex_hull_id6]
convex_hull7 = full_tower.structures[convex_hull_id7]

tower_arm_1.mesh = convex_hull1.get_mesh()
tower_arm_1.mesh = convex_hull2.get_mesh()
middle_tower_section.mesh = convex_hull3.get_mesh()
middle_tower_section.mesh = convex_hull4.get_mesh()
lower_tower_section.mesh = convex_hull5.get_mesh()
base_tower_section.mesh = convex_hull6.get_mesh()
full_tower.mesh = convex_hull7.get_mesh()

volume1 = convex_hull1.volume
volume2 = convex_hull2.volume
volume3 = convex_hull3.volume
volume4 = convex_hull4.volume
volume5 = convex_hull5.volume
volume6 = convex_hull6.volume
volume7 = convex_hull7.volume

print("Volume of first tower arm is : ", volume1)
print("Volume of second tower arm is : ", volume2)
print("Volume of upper tower section is : ", volume3)
print("Volume of middle tower section is : ", volume4)
print("Volume of lower tower section is : ", volume5)
print("Volume of base tower section is : ", volume6)
print("Volume of full tower is : ", volume7)

print("\nAssuming the density of the material used on the tower (steel) is ~7750 kg/m3")
print("\nUsing this, the mass of each section of the tower is :\n")

#formula for mass is Density X Volume
mass1 = 7750*volume1
mass2 = 7750*volume2
mass3 = 7750*volume3
mass4 = 7750*volume4
mass5 = 7750*volume5
mass6 = 7750*volume6
mass7 = 7750*volume7

print("Mass of first tower arm is : ", mass1)
print("Mass of second tower arm is : ", mass2)
print("Mass of upper tower section is : ", mass3)
print("Mass of middle tower section is : ", mass4)
print("Mass of lower tower section is : ", mass5)
print("Mass of base tower section is : ", mass6)
print("Mass of full tower is : ", mass7)

print("\nNow weight is given by mass X gravitational force")

weight1= mass1*9.8
weight2= mass2*9.8
weight3= mass3*9.8
weight4= mass4*9.8
weight5= mass5*9.8
weight6= mass6*9.8
weight7= mass7*9.8

print("Weight of first tower arm is : ", weight1)
print("Weight of second tower arm is : ", weight2)
print("Weight of upper tower section is : ", weight3)
print("Weight of middle tower section is : ", weight4)
print("Weight of lower tower section is : ", weight5)
print("Weight of base tower section is : ", weight6)
print("Weight of full tower is : ", weight7)

print("\nLets assume the ratio of the actual object to the point cloud is 1:150000")
Final_weight=weight7/150000
print("\ntherefore, the actual weight of the object is ~:\n", Final_weight)


# In[ ]:





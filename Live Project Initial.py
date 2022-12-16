#!/usr/bin/env python
# coding: utf-8

# In[2]:


import io
import os
import PySimpleGUI as sg
import cv2
import open3d as o3d
import numpy as np
import laspy as lp
file_types = [("LAS (*.las)", "*.las")]
def main():
    sg.theme('DarkBrown3')
    las_output = [
        [sg.Text("OUTPUT")],
        [sg.Text(size=(40,1), key="-TOUT-")],
        [sg.Button("Process")]
    ]
    layout =[
        [
            sg.Text("LAS file"),
            sg.Input(size=(25, 1), key="-FILE-"),
            sg.FileBrowse(file_types=file_types),
            sg.VSeperator(),
            sg.Column(las_output),
        ],
    ]
    window = sg.Window("LAS Processor", layout)
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "Process":
            las=lp.read(values["-FILE-"])
            points = np.vstack((las.x, las.y, las.z)).transpose()
            colors = np.vstack((las.red, las.green, las.blue)).transpose()
            pcd = o3d.geometry.PointCloud()
            pcd.points = o3d.utility.Vector3dVector(points)
            pcd.colors = o3d.utility.Vector3dVector(colors/65535)
            o3d.visualization.draw_geometries_with_editing([pcd])
    window.close()
if __name__ == "__main__":
    main()


# In[ ]:





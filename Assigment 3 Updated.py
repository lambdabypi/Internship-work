#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install tensorflow


# In[ ]:


import io
import os
import PySimpleGUI as sg
from PIL import Image
import base64
import cv2
file_types = [("JPEG (*.jpg)", "*.jpg"),
              ("All files (*.*)", "*.*")]
def main():
    li1=sg.theme_list()
    print(li1)
    sg.theme('Material1')   
    Encode_column = [
        [sg.Text("Click to encode image")],
        [sg.Text(size=(40,1), key="-TOUT-")],
        [sg.Button("Encode")],
    ]
    Decode_column = [
        [sg.Text("Click to decode image")],
        [sg.Multiline(size=(30, 5), key='textbox')],
        [sg.Text(size=(40, 1), key="-TOUT-")],
        [sg.Button("Decode")],
    ]
    layout =[
        [sg.Image(key="-IMAGE-")],
        [
            sg.Text("Image File"),
            sg.Input(size=(25, 1), key="-FILE-"),
            sg.FileBrowse(file_types=file_types),
            sg.Button("Load Image"),
            sg.VSeperator(),
            sg.Column(Encode_column),
            sg.VSeperator(),
            sg.Column(Decode_column),
        ],
    ]
    window = sg.Window("Image Viewer/Encoder/Decoder", layout)
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "Load Image":
            filename = values["-FILE-"]
            if os.path.exists(filename):
                image = Image.open(values["-FILE-"])
                image.thumbnail((400, 400))
                bio = io.BytesIO()
                image.save(bio, format="PNG")
                window["-IMAGE-"].update(data=bio.getvalue())
        if event == "Encode":
            OUTPUT_FILENAME = 'output1.txt'
            i=0
            folder = sg.popup_get_folder('Source folder for images\nImages will be encoded and results saved to %s'%OUTPUT_FILENAME, title='Base64 Encoder')

            if not folder:
                sg.popup_cancel('Cancelled - No valid folder entered')
                return
            try:
                namesonly = [f for f in os.listdir(folder) if f.endswith('.png') or f.endswith('.ico') or f.endswith('.gif') or f.endswith('.jpg') or f.endswith('.jpeg')]
            except:
                sg.popup_cancel('Cancelled - No valid folder entered')
                return

            outfile = open(os.path.join(folder, OUTPUT_FILENAME), 'w')

            for i, file in enumerate(namesonly):
                contents = open(values["-FILE-"], encoding="utf-8", errors='ignore').read()
                res = bytes(contents, 'utf-8')
                encoded = base64.b64encode(res)
                base64_message=encoded.decode('utf-8')
                outfile.write('\n\n{} = {}\n\n'.format(file[:file.index(".")], base64_message))
                sg.OneLineProgressMeter('Base64 Encoding', i+1, len(namesonly), key='-METER-')

            outfile.close()
            sg.popup('Completed!', 'Encoded %s files'%(i+1))
        if event == "Decode":
            OUTPUT_FILENAME1='Out_img.jpeg'
            folder = sg.popup_get_folder('Source folder for images\nString will be decoded and results saved to %s'%OUTPUT_FILENAME1, title='Base64 Decoder')
            base_img=open(values["textbox"])
            byte1=b'=='+base_img
            outfile1 = open(os.path.join(folder, OUTPUT_FILENAME1), 'w')
            decode_it=open('Output_img.jpeg', 'wb')
            outfile1.write(base64.b64decode((byte1)))
            
    window.close()
if __name__ == "__main__":
    main()


# 

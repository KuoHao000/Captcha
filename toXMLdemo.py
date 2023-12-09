width  = 1
height = 2
x = 1
y = 2
import contextlib

file_path = "randomfile.xml"
with open(file_path, "w") as o:
    with contextlib.redirect_stdout(o):
        print(f'<annotation>\n<folder>"folder"</folder>\n<path>"path"</path>\n<size>\n<width>{width}</width>\n<height>{height}</height>\n<depth>"depth"</depth>\n</size>\n<segmented>0</segmented>\n<object>\n<name>dog</name>\n<pose>Unspecified</pose>\n<truncated>0</truncated>\n<difficult>0</difficult>\n<bndbox>\n<xmin>{x}</xmin>\n<ymin>{y}</ymin>\n<xmax>{x+width}</xmax>\n<ymax>{y+height}</ymax>\n</bndbox>\n</object>\n</annotation>')
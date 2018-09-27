# -*- coding:utf-8 -*-

import os
from PIL import Image
from xml.etree import ElementTree as ET

from copy import deepcopy


class Cut_pic:
    def __init__(self):
        self.folder = None
        self.path = None
        self.size = None
        self.classification = None
        self.bndbox = None

    def __str__(self):
        return "文件夹：{0},路径：{1},尺寸：{2},类别：{3},盒子：{4}".format(self.folder, self.path, self.size, self.classifaction,
                                                            self.bndbox)


def get_imlist(path):
    """返回目录中所有png图像的文件名列表"""
    # return [os.path.join(path,f) for f in os.listdir(path) if f.endswith(".png")]
    return [os.path.join(path, f) for f in os.listdir(path)]


def save_change(save_dir, pil_im, n, x1, y1, x2, y2):
    box = (x1, y1, x2, y2)
    region = pil_im.crop(box)

    out = region.resize((128, 128))
    save_dir = save_dir  + '%05d' % n +".png"
    print(save_dir)
    out.save(save_dir)


if __name__ == "__main__":

    """
    读取的图片的路径： /home/xuna/桌面/pic/img_2/
    结果的图片的路径：/home/xuna/桌面/pic/res/
    """
    path = "/home/xuna/桌面/pic/img_2/"
    # listdir = get_imlist(path)
    """ 
    cut图片保存路径
    """
    save_dir = "F:\windows_v1.7.0\\cut_pic\\"
    """
    读取label路径
    """
    path_label = "F:\windows_v1.7.0\\volley_data\\Serve\\1\\"
    listdir_label = get_imlist(path_label)

    """
    保存类的list
    """
    label_list = []

    for dir_label in listdir_label:
        cut_get_final = Cut_pic()
        infile = os.path.splitext(dir_label)[0]
        tree = ET.parse(dir_label)
        root = tree.getroot()
        print(root.tag, root.attrib, root.text)
        cut_get_final.folder = root.find("folder")
        cut_get_final.filename = root.find("filename")
        cut_get_final.path = root.find("path").text
        size = root.find("size")
        """
        size下面宽和高
        """
        width = size.find("width")
        height = size.find("height")
        cut_get_final.size = [width, height]

        object = root.find("object")
        """
        object下面
        """
        cut_get_final.classification = object.find("name")

        bndbox = object.find("bndbox")
        """
        四个坐标
        """
        xmin = bndbox.find("xmin").text
        ymin = bndbox.find("ymin").text
        xmax = bndbox.find("xmax").text
        ymax = bndbox.find("ymax").text

        cut_get_final.bndbox = [xmin, ymin, xmax, ymax]
        label_list.append(deepcopy(cut_get_final))

    num_bel = 0
    for label in label_list:
        num_bel += 1
        current_path = label.path
        pil_im = Image.open(current_path)
        # pil_im.show()
        xy = label.bndbox
        xmin = int(xy[0])
        ymin = int(xy[1])
        xmax = int(xy[2])
        ymax = int(xy[3])
        save_change(save_dir,pil_im,num_bel,xmin,ymin,xmax,ymax)


"""
<annotation>
	<folder>volley_JPG</folder>
	<filename>10136.jpg</filename>
	<path>I:\volley_JPG\10136.jpg</path>
	<source>
		<database>Unknown</database>
	</source>
	<size>
		<width>1920</width>
		<height>1080</height>
		<depth>3</depth>
	</size>
	<segmented>0</segmented>
	<object>
		<name>Reception</name>
		<pose>Unspecified</pose>
		<truncated>0</truncated>
		<difficult>0</difficult>
		<bndbox>
			<xmin>589</xmin>
			<ymin>639</ymin>
			<xmax>829</xmax>
			<ymax>957</ymax>
		</bndbox>
	</object>
</annotation>
"""

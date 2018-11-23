# -*- coding: utf-8 -*-
"""
Created on Mon Apr 02 21:03:44 2018
@author: Fsl
"""
import os
import shutil




############################################################################
# 创建文件夹
def mkdir(path):
    # 去掉路径空格
    path = path.strip()
    # 判断路径是否存在
    isExists = os.path.exists(path)

    if not isExists:
        # 如果不存在就创建目录
        os.makedirs(path)
        print(path + " 路径创建成功")
    else:
        print(path + " 路径已存在")


##############################################################################
# 这个库复制文件比较省事

def objFileName():
    '''
    生成文件名列表
    :return:
    '''
    local_file_name_list = 'spking.txt'
    # 指定名单
    obj_name_list = []
    for i in open(local_file_name_list, 'r'):
        obj_name_list.append(i.replace('\n', '').split(","))
    return obj_name_list


def copy_img():
    '''
    复制、重命名、粘贴文件
    :return:
    '''
    local_img_name = 'E:\需要剪辑视频\分帧YN040029'
    # 指定要复制的图片路径
    path = '../data/进攻/后面'
    # 指定存放图片的目录
    list_dir = objFileName()


    for i in list_dir:
        star_index = i[0]
        end_index = i[1]
        mkdir(path + '/' + star_index)
        for j in range(int(star_index), int(end_index)):
            new_obj_name = '%06d'% j + '.jpg'
            shutil.copy(local_img_name + '/' + new_obj_name, path + '/' + star_index + '/' + new_obj_name)


if __name__ == '__main__':
    mkdir("../data/进攻/后面")
    copy_img()

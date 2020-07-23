#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/23 11:29
# @Author  : zhang yanguang
# @Site    : 
# @File    : imgfile_op.py
# @Software: PyCharm

import os
import shutil
import cv2
import numpy as np
from datetime import datetime
print(f"当前时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")


'''
visit the dir every file
'''
def visit_dir(in_dir):
    if not os.path.exists(in_dir):
        ValueError("visit path is not exits")
    abs_file = []
    for root, _, files in os.walk(in_dir):
        for file in files:
            abs_file.append( os.path.join(root, file))
    return  abs_file




def get_modify_datetime(in_dir):
    abs_file = visit_dir(in_dir)
    for af in abs_file:
        mod_time = datetime.fromtimestamp(os.path.getmtime(af))
        now = datetime.now()
        diff_time = now - mod_time
        if diff_time.days < 20:  # 条件筛选超过指定时间的文件
            print(f"""{af}
                修改时间[{mod_time.strftime('%Y-%m-%d %H:%M:%S')}]
                距今[{diff_time.days:3d}天{diff_time.seconds // 3600:2d}时{diff_time.seconds % 3600 // 60:2d}]"""
                  )  # 打印相关信息


def  rm_file(in_dir,ext=None):
    abs_file = visit_dir(in_dir)
    for af in abs_file:
        _, filename = os.path.split(af)
        suffix , ext_ = os.path.splitext(filename)
        if (ext_ == ext):
            os.remove(af)



def mv_file(in_dir,out_dir):
    if not os.path.exists(out_dir):
        os.mkdir(out_dir)
    abs_file = visit_dir(in_dir)
    for af in abs_file:
        _, filename = os.path.split(af)
        # suffix , ext = os.path.splitext(filename)
        new_file = os.path.join(out_dir,filename)
        shutil.copyfile(af, new_file)


"""
resize img with value or scale_percent
"""
def resize_img_scale(in_dir,out_dir,height=None,width=None,scale_percent =None):
    if not os.path.exists(out_dir):
        os.mkdir(out_dir)
    abs_file = visit_dir(in_dir)
    for af in abs_file:
        _, filename = os.path.split(af)
        # suffix , ext = os.path.splitext(filename)
        src = cv2.imread(af)
        if height is not None:
            dst = cv2.resize(src, dsize=(height,int(height*src.shape[1]/src.shape[0])))
        elif width is not None:
            dst = cv2.resize(src, dsize=(int(width*src.shape[0]/src.shape[1]),width))
        else:
            dst = cv2.resize(src, dsize=(src.shape[:-1]), fx=scale_percent, fy=scale_percent)
        new_file = os.path.join(out_dir,filename)
        cv2.imwrite(new_file,dst)




if __name__ =='__main__':
    in_dir = 'E:/vs2015_project/ChineseIdCard/ChineseIDOCR/out'
    out_dir = 'E:/vs2015_project/ChineseIdCard/ChineseIDOCR/out362'
    resize_img_scale(in_dir, out_dir,height= 361)

#!/usr/bin/python
#coding:utf-8

from sklearn import datasets
import numpy as np

# print data.shape
from compiler.ast import flatten
import Image
import os

def load_data():
    data = np.empty((198, 8 * 10), dtype="float32")
    label = np.empty((198,), dtype="uint8")
    imgs = os.listdir("./traindata")
    num = len(imgs)
    for i in range(num):
        img = Image.open("./traindata/" + imgs[i])
        arr = np.asarray(img,dtype="float32")
        data[i, :]=arr.flatten()
        label[i] = int(imgs[i].split('.')[0])
    data /= np.max(data)
    data -= np.mean(data)
    return data,label
def load_testdata():
    data = np.empty((16, 8 * 10), dtype="float32")
    label = np.empty((16,), dtype="uint8")
    imgs = os.listdir("./testdata")
    num = len(imgs)
    for i in range(num):
        img = Image.open("./testdata/" + imgs[i])
        arr = np.asarray(img,dtype="float32")
        data[i, :]=arr.flatten()
        label[i] = int(imgs[i].split('.')[0])
    data /= np.max(data)
    data -= np.mean(data)
    return data,label
import ocrtool

#将test下的图片切割分类,存到test1文件价下
def dealtheimage():
    # dirname = './p1'
    dirname='./test'
    imgs = os.listdir(dirname)
    num = len(imgs)
    for i in range(num):
        path=dirname+'/' + imgs[i]
        ocrtool.getverify1(path,'./test1')


#将已经分类的文件重命名
def rename():
    dirpath='./traindata'
    dir = os.listdir(dirpath)
    num = len(dir)
    for i in xrange(num):
        dirname=dirpath+'/' + dir[i]

        sign=dirname.split('/')[-1]
        imgs = os.listdir(dirname)
        num = len(imgs)
        i=0
        for i in range(num):
            path = dirname + '/' + imgs[i]
            os.rename(path, dirname+'/'+sign+'.'+str(i)+'.'+imgs[i].split('.')[-1])
            i+=1

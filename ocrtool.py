#!/usr/bin/python
# coding:utf-8





import os, urllib2
import uuid
def getuuid():

    return uuid.uuid1()
def downloadFile(data,name=None,type=None,url=None):
    path=''
    if name is not None:
        path = os.path.split(os.path.realpath(__file__))[0]+'/' + name
    else:
        name=url.split('/')[-1]
        if type is None:


            path = os.path.split(os.path.realpath(__file__))[0] + '/download/' + name
        else:

            path = os.path.split(os.path.realpath(__file__))[0] + '/download/' + name+type
    localpic = open(path, "wb")
    localpic.write(data)
    localpic.close()
    return path




import Image
from PIL import Image
from PIL import ImageEnhance

import pytesseract





# google验证码识别引擎,此处未使用
def figure_pic(path=None):
    print str(os.path.split(os.path.realpath(__file__))[0] + '/a.png')

    image = Image.open(os.path.split(os.path.realpath(__file__))[0] + '/a.png')

    vcode = pytesseract.image_to_string(image)

    print vcode




def getcutcolor(im):
    x, y = im.size
    for i in xrange(x):
        for j in xrange(y):

            r, g, b, p = im.getpixel((i, j))

            if b == 0 and r == 0 and g == 0 and p == 255:
                b = 255
                r = 255
                g = 255
            else:
                b = 0
                r = 0
                g = 0

            p = 0

            im.putpixel((i, j), (r, g, b, p))
    return im


def cut(im):
    x, y = im.size
    x1 = -1
    x2 = -1
    y1 = -1
    y2 = -1
    for i in xrange(x):
        for j in xrange(y):
            r, g, b, p = im.getpixel((i, j))
            r1, g1, b1, p1 = im.getpixel((x - i - 1, j))
            if r == 255 and x1 < 0:
                x1 = i
            if r1 == 255 and x2 < 0:
                x2 = x - i - 1
            if x1 >= 0 and x2 >= 0:
                break
                pass

    for j in xrange(y):
        for i in xrange(x):
            r, g, b, p = im.getpixel((i, j))
            r1, g1, b1, p1 = im.getpixel((i, y - j - 1))
            if r == 255 and y1 < 0:
                y1 = j
            if r1 == 255 and y2 < 0:
                y2 = y - j - 1
            if y1 >= 0 and y2 >= 0:
                break
    if x1 > x2:
        t = x1
        x1 = x2
        x2 = t
    if y1 > y2:
        t = y1
        y1 = y2
        y2 = t
    # box = (x1-1, y1-1, x1-1+8,  y1-1+10)
    box = (x1 - 1, y1 - 1, x2 + 2, y2 + 2)
    newIm = im.crop(box)
    return newIm


import numpy as np


def cutdigit(im, name, path):
    filename = name.split('/')[-1]
    x, y = im.size
    i = 0
    predictnum = ''
    while i < x and x - i > 5:
        box = (i, 0, i + 8, 0 + 10)
        newIm = im.crop(box)
        # print '图片切割'
        if path is not None:
            newIm.save(path + '/setp2_' + str(i) + '_' + filename + '.png')

        predictnum += runmodel(newIm)

        i = i + 7
    return predictnum


pkl_file = None
import pickle


def getModel():
    global pkl_file

    model_save_file = './model.bin'
    pkl_file = open(model_save_file, 'rb')
    object = pickle.load(pkl_file)
    if pkl_file is not None:
        pkl_file.close()
    return object['GBDT']


def runmodel(img):
    data = np.empty((1, 8 * 10), dtype="float32")
    arr = np.asarray(img, dtype="float32")
    data[0, :] = arr.flatten()

    data /= np.max(data)
    data -= np.mean(data)
    model = getModel()
    predict = int(model.predict(data))
    return str(predict)


def changecolor(im):
    x, y = im.size
    for i in xrange(x):
        for j in xrange(y):
            im.putpixel((i, j), 255 - im.getpixel((i, j)))
    return im


def getverifyimg(name, path=None):
    # 打开图片
    im = Image.open(name)

    enhancer = ImageEnhance.Contrast(im)
    im = enhancer.enhance(150)
    im = getcutcolor(im)
    im = cut(im)
    im = im.convert('L')

    im = changecolor(im)
    print '图片处理完结果'
    # im.show()

    num = cutdigit(im, name, path)
    print '识别的结果为',name, num
    return num
    # im.save(path+'/step1_'+name)



    # text = pytesseract.image_to_string(im)
    # print text


import time

if __name__ == "__main__":


    start_time = time.time()

    getverifyimg('9011')

    print 'training took %fs!' % (time.time() - start_time)











    # import os
    # import ctypes
    #
    # libname = "/usr/lib/libtesseract.so.3" # tesseract引擎的动态库
    # lang = "eng" # 识别的语言，eng是英文，chi_sim是中文，自己选择
    # filename = "/home/guzhenping/Desktop/tests.jpg"  # 待识别图片
    #
    # # 加载动态库
    # tesseract = ctypes.cdll.LoadLibrary(libname)
    # TESSDATA_PREFIX = os.environ.get("TESSDATA_PREFIX")
    #
    # # 创建一个handle,请看TessBaseAPI,你就懂了为啥非要有handle
    # api = tesseract.TessBaseAPICreate()
    #
    # # 初始化引擎
    # rc = tesseract.TessBaseAPIInit3(api,TESSDATA_PREFIX,lang)
    #
    # # 处理待识别图片
    # text_out = tesseract.TessBaseAPIProcessPages(api,filename,None,0)
    #
    # #转成字符串
    # result_text = ctypes.string_at(text_out)
    # print result_text  # 输出结果

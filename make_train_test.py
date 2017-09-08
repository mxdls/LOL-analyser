from dbcontroller import get_all_battls, get_batlle_detail
from numpy import *
from tool import make_dics

random.seed(123)
from keras.utils import np_utils
import sys


# 旧的函数
# def make_train_file(zonepy, n_test=2000, path='F:/MachineLearning/LOL_train/'):
#     big_to_little,little_to_big=make_dics()
#     battls = get_all_battls(zonepy, True)
#     test = True
#     xbuffer = []
#     ybuffer = []
#     for x in battls:
#         details = get_batlle_detail(x)
#         if len(details) != 10: continue
#         one = []
#         trans = (random.randint(0, 2) == 1)
#         for y in details:
#             if (y.win == 1 and (not trans)) or (not y.win == 1 and trans):
#                 one.insert(0, y.heroId)
#             else:
#                 one.append(y.heroId)
#         xbuffer.append(one)
#         if trans:
#             ybuffer.append(0)
#         else:
#             ybuffer.append(1)
#
#         if (len(xbuffer) == n_test) and test:
#             array(xbuffer).tofile(path + "%s-xte.bin" % zonepy)
#             array(ybuffer).tofile(path + "%s-yte.bin" % zonepy)
#             test = False
#             xbuffer.clear()
#             ybuffer.clear()
#         if (len(xbuffer) % 1000 == 0): print(len(xbuffer))
#     array(xbuffer).tofile(path + "%s-xtr.bin" % zonepy)
#     array(ybuffer).tofile(path + "%s-ytr.bin" % zonepy)

def make_train_file(zonepy, n_test=2000, path='F:/MachineLearning/LOL_train/', n_train=-1):
    big_to_little, little_to_big = make_dics()
    battls = get_all_battls(zonepy, True)
    test = True
    xbuffer = []
    ybuffer = []
    for x in battls:
        details = get_batlle_detail(x)
        if len(details) != 10: continue
        one = zeros(400, dtype=int32)
        trans = (random.randint(0, 2) == 1)
        for y in details:
            if (y.win == 1 and (not trans)) or (not y.win == 1 and trans):
                one[big_to_little[y.heroId]] = 1
            else:
                one[big_to_little[y.heroId] + 200] = 1
        xbuffer.append(one)
        if trans:
            ybuffer.append(0)
        else:
            ybuffer.append(1)

        if (len(xbuffer) == n_test) and test:
            array(xbuffer).tofile(path + "%s-xte.bin" % zonepy)
            array(ybuffer).tofile(path + "%s-yte.bin" % zonepy)
            test = False
            xbuffer.clear()
            ybuffer.clear()
        if len(xbuffer) % 1000 == 0:
            print(len(xbuffer))
        if len(xbuffer) == n_train:
            break
    array(xbuffer).tofile(path + "%s-xtr.bin" % zonepy)
    array(ybuffer).tofile(path + "%s-ytr.bin" % zonepy)


if __name__ == "__main__":
    make_train_file('dx7', 2000, 'F:/MachineLearning/LOL_train/')

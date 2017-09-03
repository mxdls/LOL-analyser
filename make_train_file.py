from dbcontroller import get_all_battls, get_batlle_detail
from numpy import *


def make_train_file(zonepy, n=1000):
    battls = get_all_battls(zonepy)
    filecount = 0
    buffer = []
    for x in battls:
        details = get_batlle_detail(x)
        if (len(details) != 10): continue
        one = []
        for y in details:
            if (y.win == 1):
                one.insert(0, y.heroId)
            else:
                one.append(y.heroId)
        buffer.append(one)
        # 保存数组为二进制文件
        if (len(buffer) == n):
            file = array(buffer)
            file.tofile("F:/MachineLearning/LOL_train/%s-%s.bin" % (zonepy, filecount))
            filecount += 1
            buffer.clear()


if __name__ == "__main__":
    make_train_file('dx7')

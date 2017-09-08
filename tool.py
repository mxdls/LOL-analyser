import json
import dbcontroller
import numpy as np

def res_to_dic(r):
    j = json.loads(r.text)
    return j


def output_r(r):
    j = json.dumps(res_to_dic(r), indent=1, ensure_ascii=False)
    print(j)
    return


def make_dics():
    heros = dbcontroller.get_all_heros()
    big_to_little = np.zeros(1000, dtype=np.int32)
    little_to_big = np.zeros(200, dtype=np.int32)
    for x in heros:
        big_to_little[x.heroId] = x.myId
        little_to_big[x.myId] = x.heroId
    big_to_little.astype(int)
    little_to_big.astype(int)
    return big_to_little, little_to_big


if __name__ == '__main__':
    big_to_little, little_to_big = make_dics()
    print(little_to_big)

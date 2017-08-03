from battle import *
from dbcontroller import *


# 在选定服务器选区n个用户读取最近32场比赛插入数据库
def get_nplayers_battle(zonepy, n):
    users = get_n_players(zonepy, n)
    for x in users:
        bl = battlelist(userid=x.userId, zonepy=x.zonepy)
        bl.update_list()
        bl.insert_battles()


get_nplayers_battle("dx7", 5)

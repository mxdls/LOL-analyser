from battle import *
from dbcontroller import *
import threading


# 在选定服务器选区n个用户读取最近32场比赛插入数据库
def get_nplayers_battle(zonepy, n, circle=False):
    while (circle):
        users = get_n_players(zonepy, n)
        for x in users:
            bl = battlelist(userid=x.userId, zonepy=x.zonepy)
            bl.update_list(-1, True)
            bl.insert_battles()
    users = get_n_players(zonepy, n)
    for x in users:
        bl = battlelist(userid=x.userId, zonepy=x.zonepy)
        bl.update_list(-1, True)
        bl.insert_battles()


# 多线程
def m_thread(zonepy, n):
    threads = []
    for _ in range(n):
        t = threading.Thread(target=get_nplayers_battle, args=(zonepy, 10, True))
        threads.append(t)
    for t in threads:
        t.setDaemon(True)
        t.start()
    t.join()


if __name__ == "__main__":
    # get_nplayers_battle("dx7", 1)
    while (True):
        m_thread('dx7', 50)

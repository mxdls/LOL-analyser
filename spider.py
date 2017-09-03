from battle import *
from dbcontroller import *
import threading


# 在选定服务器选区n个用户读取最近32场比赛插入数据库
def get_nplayers_battle(zonepy, n):
    users = get_n_players(zonepy, n)
    for x in users:
        bl = battlelist(userid=x.userId, zonepy=x.zonepy)
        bl.update_list()
        bl.insert_battles()


# 多线程
def m_thread(zonepy, n):
    threads = []
    for _ in range(n):
        t = threading.Thread(target=get_nplayers_battle, args=(zonepy, 5))
        threads.append(t)
    for t in threads:
        t.setDaemon(True)
        t.start()
    t.join()
    print("ok")


if __name__ == "__main__":
    # get_nplayers_battle("dx7", 1)
    for _ in range(10000):
        m_thread('dx7', 3)

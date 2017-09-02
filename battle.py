import requests, json
from get_url import *
from tool import *
from dbcontroller import *


# 游戏种类:1 自定义 2人机？ 3匹配赛 4单双排 5灵活组排 6大乱斗
class battlelist(object):
    def __init__(self, userid='4006716018', zonepy='dx7', user=None):
        self.userid = userid
        self.zonepy = zonepy
        self.battleid_list = []
        self.battle_list = []
        if (user != None):  # 如果传入了user对象
            self.userid = user.userid
            self.zonepy = user.zonepy

    def update_list(self, n=-1):
        r = requests.get(get_battle_list_url(self.zonepy, self.userid))
        j = res_to_dic(r)
        for x in j["game_list"]:
            self.battleid_list.append(x["game_id"])
            # 查询有误的战局不加入队列
            try:
                b = battle(self.zonepy, self.userid, x["game_id"], x["game_type"]["const"])
            except:
                n -= 1
                if (n == 0): break
                continue
            self.battle_list.append(b)
            n -= 1
            if (n == 0): break

    def insert_battles(self):
        for x in self.battle_list:
            try:
                insert_battle(x)
            except:
                print("战局查询错误：%s %s" % (x.zonepy, x.battleid))
                return
        print("插入完毕")


class battle(object):
    def __init__(self, zonepy, userid, battleid, type):
        self.zonepy = zonepy
        self.userid = userid
        self.battleid = battleid
        self.type = type
        r = requests.get(get_battle_detail_url(self.zonepy, self.userid, self.battleid))
        #将战斗的json文件存放到硬盘目录
        with open("F:/MachineLearning/LOLdata/%s.json" % (str(self.zonepy) + "-" + str(self.battleid)), 'w',
        # with open("./battle_details/%s.json" % (str(self.zonepy) + "-" + str(self.battleid)), 'w',
                  encoding='utf-8') as json_file:
            json.dump(r.text, json_file, ensure_ascii=False)
        try:
            self.detail = res_to_dic(r)
        except:
            print("请求错误：%s %s %s" % (self.zonepy, self.userid, self.battleid))
        r.close()


if __name__ == "__main__":
    b = battlelist()
    b.update_list(1)
    b.insert_battles()

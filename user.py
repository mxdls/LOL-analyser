# -*-coding:UTF-8-*-
import requests, json
from get_url import *
from dbcontroller import *
from tool import *


class user(object):
    # 默认小婶婶
    def __init__(self, userid='4006716018', zonepy='dx7', level=30, username='525B丶小婶婶'):
        self.userid = userid
        self.zonepy = zonepy
        self.level = level
        self.name = username
        self.t = 0
        self.r = 0

    def print_info(self):
        print('Name:%s\nUserId:%s\nZonePY:%s\nLevel:%s' % (self.name, self.userid, self.zonepy, self.level))

    def find_user_by_name(self, username, zonepy='none'):
        self.name = username
        r = requests.get(get_user_list_by_name_url(username))
        j = res_to_dic(r)
        # 若未输入服务器
        if (zonepy == 'none'):
            for x in j["player_list"]:
                print(x["game_zone"]["alias"], x["game_zone"]["pinyin"])
            print("输入编号:")
            n = int(input())
            self.zonepy = j["player_list"][n - 1]["game_zone"]["pinyin"]
            self.level = int(j["player_list"][n - 1]["level"])
            self.userid = j["player_list"][n - 1]["user_id"]
        else:
            for x in j["player_list"]:
                if (zonepy == x["game_zone"]["pinyin"]):
                    self.zonepy = zonepy
                    self.level = x["level"]
                    self.userid = x["user_id"]
                    break

    def insert_to_db(self):
        insert_user(self)

    def update_detail_info(self):
        r = requests.get(get_detail_by_user_id_url(self.zonepy, self.userid))
        try:
            j = res_to_dic(r)
        except:
            print("未找到该用户：%s %s" % (self.zonepy, self.userid))

        self.level = j["player_list"][0]["level"]
        self.t = j["player_list"][0]["formatted_ranked_history"]["s7"]["t"]
        self.r = j["player_list"][0]["formatted_ranked_history"]["s7"]["r"]
        self.name = j["player_list"][0]["pn"]
        # print("Updated user:",self.name)


if __name__ == "__main__":
    aa = user()
    aa.find_user_by_name('525B丶小科科')
    aa.update_detail_info()
    aa.insert_to_db()
    print(aa.userid)

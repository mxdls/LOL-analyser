import requests, json
from get_url import *
from tool import *
from dbcontroller import *


class battlelist(object):
    def __init__(self, userid='4006716018', zonepy='dx7'):
        self.userid = userid
        self.zonepy = zonepy
        self.battleid_list = []
        self.battle_list = []

    def update_list(self):
        r = requests.get(get_battle_list_url(self.zonepy, self.userid))
        j = res_to_dic(r)
        for x in j["game_list"]:
            self.battleid_list.append(x["game_id"])
            print(x["game_id"])


class battle(object):
    def __init__(self):
        self


if __name__ == "__main__":
    b = battlelist()
    b.update_list()

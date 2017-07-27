import time


def get_time_stamp():
    return str(time.time())[0:-3]


def get_user_list_by_name_url(name):
    url = 'http://api.lolbox.duowan.com/api/v2/player/search/?player_name_list=%s&callback=&_=%s' \
          % (name, get_time_stamp())
    return url


def get_detail_by_user_id_url(area, id):
    path = area + "/" + str(id)
    url = "http://api.lolbox.duowan.com/api/v3/player/%s/?callback=&_=%s" \
          % (path, get_time_stamp())
    return url


def get_battle_list_url(area, id):
    url = "http://api.lolbox.duowan.com/api/v3/player/%s/%s/game_recent/?callback=&_=%s" \
          % (area, id, get_time_stamp())
    return url


def get_battle_detail_url(area, uid, bid):
    url = "http://api.lolbox.duowan.com/api/v3/player/%s/%s/game/%s/?callback=&_=%s" \
          % (area, uid, bid, get_time_stamp())
    return url

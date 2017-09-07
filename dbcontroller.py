from sqlalchemy import Column, String, create_engine, Integer, Float, and_, or_
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.expression import func
from sqlalchemy.pool import NullPool
from user import *
import global_var
import sys

# 连接信息
mySQLConfig = 'mysql+pymysql://root@localhost:3306/lol?charset=utf8mb4'
# 创建对象的基类:
Base = declarative_base()

# 初始化数库连接:
engine = create_engine(mySQLConfig, pool_size=100)
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)


# 定义User对象:
class User(Base):
    # 表的名字:
    __tablename__ = 'user'
    # 表的结构:
    userId = Column(String(20), primary_key=True)
    userName = Column(String(20))
    zonepy = Column(String(20))
    level = Column(Integer)
    t = Column(Integer)
    r = Column(Integer)


class Hero(Base):
    __tablename__ = 'hero'
    heroId = Column(Integer, primary_key=True)
    displayName = Column(String(20))
    name = Column(String(20))
    title = Column(String(20))


class Battle(Base):
    __tablename__ = 'battle'
    battleId = Column(String(20), primary_key=True)
    zonepy = Column(String(20))
    type = Column(Integer)
    time = Column(String(20))
    # details = relationship("BattleDetail",backref="battle")


class BattleDetail(Base):
    __tablename__ = 'battledetail'
    battleId = Column(String(20), primary_key=True)
    zonepy = Column(String(20))
    userId = Column(String(20), primary_key=True)
    win = Column(Integer)
    heroId = Column(Integer)
    mvp = Column(Integer)
    K = Column(Integer)
    D = Column(Integer)
    A = Column(Integer)
    score = Column(Float)


def insert_user(user):
    session = DBSession()
    new_user = User(userId=user.userid, userName=user.name, zonepy=user.zonepy, level=user.level, t=user.t, r=user.r)
    session.add(new_user)
    try:
        session.commit()
    except:
        # print("已存在用户:", user.name)
        session.close()
        return False
    session.close()
    return True


def insert_hero(hero_dic):
    new_hero = Hero(heroId=hero_dic["id"], displayName=hero_dic["display_name"], name=hero_dic["name"],
                    title=hero_dic["title"])
    session = DBSession()
    session.add(new_hero)
    try:
        session.commit()
    except:
        session.close()
        return False
    session.close()
    return True


def query_and_insert_user(userid, zonepy):
    session = DBSession()
    if (len(session.query(User).filter(User.userId == userid, User.zonepy == zonepy).all()) != 0):
        session.close()
        return False
    else:
        new_user = user(userid=userid, zonepy=zonepy)
        try:
            new_user.update_detail_info()
        except:
            return False
        insert_user(new_user)
        session.close()
        return True


def insert_battle(battle):
    session = DBSession()
    new_battle = Battle(battleId=battle.battleid, zonepy=battle.zonepy, type=battle.type,
                        time=battle.detail["player_game_list"][0]["start_timestamp"])
    session.add(new_battle)
    for x in battle.detail["player_game_list"][0]["team_lose"]["player_champions"]:
        new_battle_detail = BattleDetail(battleId=battle.battleid, zonepy=x["game_zone"]["pinyin"],
                                         userId=x["player"]["user_id"], win=0,
                                         heroId=x["champion"]["id"],
                                         mvp=x["flag_mvp_carry"], K=x["total_killed"], D=x["total_death"],
                                         A=x["total_assist"], score=x["evaluate_in_game"])
        if global_var.add_new_users:
            query_and_insert_user(userid=x["player"]["user_id"], zonepy=x["game_zone"]["pinyin"])
        session.add(new_battle_detail)
        insert_hero(x["champion"])
    for x in battle.detail["player_game_list"][0]["team_win"]["player_champions"]:
        new_battle_detail = BattleDetail(battleId=battle.battleid, zonepy=x["game_zone"]["pinyin"],
                                         userId=x["player"]["user_id"], win=1,
                                         heroId=x["champion"]["id"],
                                         mvp=x["flag_mvp_carry"], K=x["total_killed"], D=x["total_death"],
                                         A=x["total_assist"], score=x["evaluate_in_game"])
        if global_var.add_new_users:
            query_and_insert_user(userid=x["player"]["user_id"], zonepy=x["game_zone"]["pinyin"])
        session.add(new_battle_detail)
        insert_hero(x["champion"])
    try:
        session.commit()
    except:
        global_var.battle_exist += 1
        print("Battle%s 已存在 %s/%s" % (
            battle.battleid, global_var.battle_exist, global_var.battle_exist + global_var.battle_insert))
        session.close()
        return False
    print("插入 Battle%s 成功" % battle.battleid)
    global_var.battle_insert += 1
    session.close()
    return True


def get_n_players(zonepy, n):
    session = DBSession()
    users = session.query(User).filter(User.zonepy == zonepy).order_by(func.random()).limit(n).all()
    session.close()
    return users


def get_all_battls(zonepy, ranked_only=True):
    session = DBSession()
    # 只查询匹配、排位
    if (ranked_only):
        battles = session.query(Battle).filter(and_(Battle.type.in_([4, 5]), Battle.zonepy == zonepy)).all()
    else:
        battles = session.query(Battle).filter(Battle.zonepy == zonepy).all()
    session.close()
    return battles


def get_batlle_detail(battle):
    session = DBSession()
    details = session.query(BattleDetail).filter(
        and_(BattleDetail.zonepy == battle.zonepy, BattleDetail.battleId == battle.battleId)).all()
    session.close()
    return details


if __name__ == "__main__":
    print(get_batlle_detail(get_all_battls('dx7', True)[0]))

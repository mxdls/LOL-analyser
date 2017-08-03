from sqlalchemy import Column, String, create_engine, Integer, Float
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.expression import func
from user import *

# 连接信息
mySQLConfig = 'mysql+pymysql://root@localhost:3306/lol?charset=utf8mb4'
# 创建对象的基类:
Base = declarative_base()

# 初始化数库连接:
engine = create_engine(mySQLConfig)
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
        new_user.update_detail_info()
        insert_user(new_user)
        session.close()
        return True


def insert_battle(battle):
    session = DBSession()
    new_battle = Battle(battleId=battle.battleid, type=battle.type,
                        time=battle.detail["player_game_list"][0]["start_timestamp"])
    session.add(new_battle)
    for x in battle.detail["player_game_list"][0]["team_lose"]["player_champions"]:
        new_battle_detail = BattleDetail(battleId=battle.battleid, zonepy=x["game_zone"]["pinyin"],
                                         userId=x["player"]["user_id"], win=0,
                                         heroId=x["champion"]["id"],
                                         mvp=x["flag_mvp_carry"], K=x["total_killed"], D=x["total_death"],
                                         A=x["total_assist"], score=x["evaluate_in_game"])
        query_and_insert_user(userid=x["player"]["user_id"], zonepy=x["game_zone"]["pinyin"])
        session.add(new_battle_detail)
        insert_hero(x["champion"])
    for x in battle.detail["player_game_list"][0]["team_win"]["player_champions"]:
        new_battle_detail = BattleDetail(battleId=battle.battleid, zonepy=x["game_zone"]["pinyin"],
                                         userId=x["player"]["user_id"], win=1,
                                         heroId=x["champion"]["id"],
                                         mvp=x["flag_mvp_carry"], K=x["total_killed"], D=x["total_death"],
                                         A=x["total_assist"], score=x["evaluate_in_game"])
        query_and_insert_user(userid=x["player"]["user_id"], zonepy=x["game_zone"]["pinyin"])
        session.add(new_battle_detail)
        insert_hero(x["champion"])
    try:
        session.commit()
    except:
        print("Battle%s 已存在" % battle.battleid)
        session.close()
        return False
    print("插入 Battle%s 成功" % battle.battleid)
    session.close()
    return True


def get_n_players(zonepy, n):
    session = DBSession()
    users = session.query(User).filter(User.zonepy == zonepy).order_by(func.random()).limit(n).all()
    return users

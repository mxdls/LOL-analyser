from sqlalchemy import Column, String, create_engine, Integer, Float
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 连接信息
mySQLConfig = 'mysql+pymysql://root@localhost:3306/lol?charset=utf8mb4'
# 创建对象的基类:
Base = declarative_base()


# 定义User对象:
class User(Base):
    # 表的名字:
    __tablename__ = 'user'
    # 表的结构:
    userid = Column(String(20), primary_key=True)
    username = Column(String(20))
    zonepy = Column(String(20))
    level = Column(Integer)
    t = Column(Integer)
    r = Column(Integer)


class Hero(Base):
    __tablename__ = 'hero'
    heroid = Column(Integer, primary_key=True)
    displayname = Column(String(20))
    name = Column(String(20))
    title = Column(String(20))


class Battle(Base):
    __tablename__ = 'battle'
    battleid = Column(String(20), primary_key=True)
    type = Column(Integer)
    time = Column(String(20))


class BattleDetail(Base):
    __tablename__ = 'battledetail'
    battleId = Column(String(20), primary_key=True)
    userId = Column(String(20), primary_key=True)
    win = Column(Integer)
    heroId = Column(Integer)
    mvp = Column(Integer)
    K = Column(Integer)
    D = Column(Integer)
    A = Column(Integer)
    score = Column(Float)


# 初始化数库连接:
engine = create_engine(mySQLConfig)
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)


def insert_user(user):
    session = DBSession()
    new_user = User(userid=user.userid, username=user.name, zonepy=user.zonepy, level=user.level, t=user.t, r=user.r)
    session.add(new_user)
    try:
        session.commit()
    except:
        print("已存在用户:", user.name)
        session.close()
        return False
    session.close()
    return True

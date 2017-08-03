from dbcontroller import *


def show_info(zonepy=None):
    session = DBSession()
    u = 0
    b = 0
    if (zonepy != None):
        u = session.query(func.count(User.userId)).filter(User.zonepy == zonepy).scalar()
        b = session.query(func.count(Battle.battleId)).filter(Battle.zonepy == zonepy).scalar()
    else:
        u = session.query(func.count(User.userId)).scalar()
        b = session.query(func.count(Battle.battleId)).scalar()
    print("%s名用户\n%s场战绩" % (u, b))


if __name__ == "__main__":
    show_info()

# coding: utf-8

from fablib.graphite import Carbon, Ceres, GraphiteWeb
from fabkit import task

carbon = Carbon('cache')
ceres = Ceres()
graphite_web = GraphiteWeb()


@task
def setup():
    ceres.setup()
    carbon.setup()
    graphite_web.setup()

    return {'status': 1}

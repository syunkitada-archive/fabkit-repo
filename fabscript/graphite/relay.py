# coding: utf-8

from fablib.graphite import Carbon, Ceres, GraphiteWeb
from fabkit import task, env

carbon = Carbon('relay')
ceres = Ceres()
graphite_web = GraphiteWeb()


@task
def setup():
    ceres.setup()
    carbon.setup()
    graphite_web.setup()
    if env.fabscript['status'] == 0:
        if env.host == env.hosts[0]:
            graphite_web.syncdb()
            return {'status': 1}
    else:
        return {'status': 1}

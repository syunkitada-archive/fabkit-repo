# coding: utf-8

from fabkit import task, env


@task(is_bootstrap=False)
def setup():
    st = env.fabscript['status']
    if st == 0:
        print 'setup db'
        return {'status': 1}
    elif st == 1:
        print 'sync db'
        return {'status': 2}
    elif st == 2:
        print 'setup db2'
        return {'status': 2}

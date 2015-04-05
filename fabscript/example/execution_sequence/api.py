# coding: utf-8

from fabkit import task


@task(is_bootstrap=False)
def setup():
    print 'setup api'
    return {'status': 1}

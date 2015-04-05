# coding: utf-8

from fabkit import task


@task(is_bootstrap=False)
def setup():
    print 'setup web'
    return {'status': 1}

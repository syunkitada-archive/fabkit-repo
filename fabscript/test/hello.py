# coding: utf-8

from fabkit import task, run


@task(is_bootstrap=False)
def setup():
    print 'TEST'
    # run('touch /tmp/test')

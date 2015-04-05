# coding: utf-8

from fabkit import task


@task(is_bootstrap=False)
def setup2():
    print 'setup lib 2'


@task(is_bootstrap=False)
def setup3():
    print 'setup lib 3'

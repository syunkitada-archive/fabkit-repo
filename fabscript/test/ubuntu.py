# coding: utf-8

from fabkit import task
from fablib.base.test import Test


test = Test()


@task
def setup():
    test.setup()
    print 'test'

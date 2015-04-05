# coding: utf-8

from fabkit import task
from multi_setup_lib import *  # noqa


@task(is_bootstrap=False)
def setup1():
    print 'setup 1'


@task(is_bootstrap=False)
def setup3():
    print 'setup 3'

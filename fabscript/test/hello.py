# coding: utf-8

from fabkit import task, run


@task
def setup():
    run('touch /tmp/test')

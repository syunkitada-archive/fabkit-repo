# coding: utf-8

from fabkit import task, run


@task
def setup():
    run('cd ~/ && git clone git@github.com:syunkitada/home.git')

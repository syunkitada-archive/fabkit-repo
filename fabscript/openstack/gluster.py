# coding: utf-8

from fabkit import task, api
from fablib.gluster import Gluster

gluster = Gluster()


@task
def setup0():
    gluster.setup()


@task
@api.serial
def setup1_peer():
    gluster.setup_peer()


@task
def setup2_volume():
    gluster.setup_volume()

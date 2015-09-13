# coding: utf-8

from fabkit import task
from fablib.openstack import Cinder

cinder = Cinder()


@task
def setup():
    cinder.setup()

    return {'status': 1}


@task
def restart():
    cinder.restart_services()

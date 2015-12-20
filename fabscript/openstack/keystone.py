# coding: utf-8

from fabkit import task, parallel
from fablib.openstack import Keystone

keystone = Keystone()


@task
@parallel
def setup():
    keystone.setup()

    return {'status': 1}


@task
def restart():
    keystone.restart_services()

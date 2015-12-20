# coding: utf-8

from fabkit import task, parallel
from fablib.openstack import Horizon

horizon = Horizon()


@task
@parallel
def setup():
    horizon.setup()

    return {'status': 1}


@task
def restart():
    horizon.restart_services()

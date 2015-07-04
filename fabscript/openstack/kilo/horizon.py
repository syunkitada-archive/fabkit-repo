# coding: utf-8

from fabkit import task
from fablib.openstack.kilo import Horizon

horizon = Horizon()


@task
def setup():
    horizon.setup()

    return {'status': 1}
# coding: utf-8

from fabkit import task
from fablib.openstack.icehouse import Glance

glance = Glance()


@task
def setup():
    glance.setup()

    return {'status': 1}

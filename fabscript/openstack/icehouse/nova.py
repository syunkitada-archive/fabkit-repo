# coding: utf-8

from fabkit import task
from fablib.openstack.icehouse import Nova

nova = Nova()


@task
def setup():
    nova.setup()

    return {'status': 1}

# coding: utf-8

from fabkit import task
from fablib.openstack.icehouse import Neutron

neutron = Neutron()


@task
def setup():
    neutron.setup()

    return {'status': 1}

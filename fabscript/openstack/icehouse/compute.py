# coding: utf-8

from fabkit import task
from fablib.openstack.icehouse import Nova, Neutron, nova, neutron

nova = Nova(mode=nova.MODE_COMPUTE)
neutron = Neutron(mode=neutron.MODE_COMPUTE)


@task
def setup():
    nova.setup()
    neutron.setup()

    return {'status': 1}

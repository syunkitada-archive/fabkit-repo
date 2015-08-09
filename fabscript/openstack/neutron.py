# coding: utf-8

from fabkit import task
from fablib.openstack import Neutron

neutron = Neutron()


@task
def setup():
    neutron.setup()

    return {'status': 1}


@task
def restart():
    neutron.restart_services()

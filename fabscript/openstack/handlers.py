# coding: utf-8

from fabkit import task
from fablib.openstack import Neutron

neutron = Neutron()


@task
def handler_setup_start():
    print 'setup handler test'

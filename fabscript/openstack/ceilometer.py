# coding: utf-8

from fabkit import task, parallel
from fablib.openstack import Ceilometer

ceilometer = Ceilometer()


@task
@parallel
def setup():
    ceilometer.setup()

    return {'status': 1}


@task
def register_images():
    ceilometer.register_images()


@task
def restart():
    ceilometer.restart_services()

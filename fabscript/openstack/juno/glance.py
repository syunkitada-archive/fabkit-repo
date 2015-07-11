# coding: utf-8

from fabkit import task
from fablib.openstack import Glance

glance = Glance()


@task
def setup():
    glance.setup()

    return {'status': 1}


@task
def register_images():
    glance.register_images()

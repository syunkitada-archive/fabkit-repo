# coding: utf-8

from fabkit import task
from fablib.openstack import Heat

heat = Heat()


@task
def setup():
    heat.setup()

    return {'status': 1}


@task
def register_images():
    heat.register_images()


@task
def restart():
    heat.restart_services()

# coding: utf-8

from fabkit import task, parallel
from fablib.openstack import Heat

heat = Heat()


@task
@parallel
def setup():
    heat.setup()

    return {'status': 1}


@task
def register_images():
    heat.register_images()


@task
def restart():
    heat.restart_services()

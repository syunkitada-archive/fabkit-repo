# coding: utf-8

from fabkit import task, parallel
from fablib.rabbitmq import RabbitMQ

rabbitmq = RabbitMQ()


@task
@parallel
def setup0():
    rabbitmq.setup()
    return {'status': 1}


@task
def setup1_cluster():
    rabbitmq.setup_cluster()
    return {'status': 1}


@task
def restart():
    rabbitmq.restart_services()

# coding: utf-8

from fabkit import task, parallel
from fablib.mysql import MySQL

mysql = MySQL()


@task
@parallel
def setup0():
    mysql.setup()
    return {'status': 1}


@task
def setup1_slave():
    mysql.setup_slave()
    return {'status': 1}


@task
def restart():
    mysql.restart_services()

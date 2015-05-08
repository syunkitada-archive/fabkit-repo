# coding: utf-8

from fablib.mysql import MySQL
from fabkit import task

mysql = MySQL()


@task
def setup():
    mysql.setup()
    return {'status': 1}

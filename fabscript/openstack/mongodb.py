# coding: utf-8

from fabkit import task
from fablib.mongodb import MongoDB

mongodb = MongoDB()


@task
def setup():
    mongodb.setup()
    return {'status': 1}

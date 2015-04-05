# coding: utf-8

from fabkit import Package, Service, task


mysqld = Service('mysqld')


@task
def setup():
    Package('mysql-server').install()
    mysqld.enable().start()


@task
def check():
    if mysqld.status().return_code == 0:
        return {'status': 0}
    else:
        return {'status': 1000}

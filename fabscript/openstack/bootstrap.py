# coding: utf-8

from fabkit import task, Service, parallel, sudo


@task
@parallel
def setup():
    sudo('setenforce 0')
    Service('firewalld').stop().disable()
    return {'status': 1}

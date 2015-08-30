# coding: utf-8

from fabkit import task, Service, parallel


@task
@parallel
def setup():
    Service('firewalld').stop().disable()
    return {'status': 1}

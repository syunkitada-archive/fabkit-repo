# coding: utf-8

from fabkit import task, Service, parallel, sudo, Editor


@task
@parallel
def setup():
    sudo('setenforce 0')
    Editor('/etc/selinux/config').s('SELINUX=enforcing', 'SELINUX=disable')

    Service('firewalld').stop().disable()

    return {'status': 1}

# coding: utf-8

from fabkit import task, env, run, sudo, Package, Service, filer


@task()
def setup():
    print '{0}: hello'.format(env.host)
    print env.cluster
    run('hostname')
    sudo('hostname')
    Package('memcached').install()
    Service('memcached').start()
    # run('touch /tmp/test')
    filer.file('/etc/memcached.conf')
    filer.template('/etc/memcached.conf')


@task()
def local():
    filer.file('/etc/memcached.conf')
    filer.template('/etc/memcached.conf')

# coding: utf-8

from fabkit import task, run


@task
def setup():
    run('echo "hello world" > ~/hello')
    return {'status': 0, 'msg': 'success hello world'}


@task
def check():
    if run('cat ~/hello').find('hello world') == -1:
        return {'status': 100, 'msg': 'not found'}
    else:
        return {'status': 0, 'msg': 'success check hello world'}


@task
def touch():
    run('touch ~/hello')


@task(is_bootstrap=False)
def boot():
    print 'boot virtual machine'

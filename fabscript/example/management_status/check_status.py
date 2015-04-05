# coding: utf-8

from fabkit import task, env


@task(is_bootstrap=False)
def setup():
    return {'task_status': 0}


@task(is_bootstrap=False)
def check():
    if env.host.find('success') > -1:
        return {'status': 0}
    elif env.host.find('warning') > -1:
        return {'status': 201}
    else:
        return {'status': 20001}

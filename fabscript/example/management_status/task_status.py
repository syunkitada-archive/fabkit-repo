# coding: utf-8

from fabkit import task, env


@task(is_bootstrap=False)
def setup():
    if env.host.find('success') > -1:
        return {'task_status': 0}
    elif env.host.find('warning') > -1:
        return {'task_status': 101}
    else:
        return {'task_status': 10001}


@task(is_bootstrap=False)
def check():
    if env.host.find('success') > -1:
        return {'task_status': 0}
    elif env.host.find('warning') > -1:
        return {'task_status': 201}
    else:
        return {'task_status': 20001}


@task(is_bootstrap=False)
def manage():
    if env.host.find('success') > -1:
        return {'task_status': 0}
    elif env.host.find('warning') > -1:
        return {'task_status': 301}
    else:
        return {'task_status': 30001}

# coding: utf-8

from fabkit import task, parallel
import random


@task
def setup():
    print 'test'
    return {
        'task_status': 100,
    }


@task(is_bootstrap=False)
def hello():
    print 'chef'
    return {
        'task_status': 100,
    }


@parallel
@task(is_bootstrap=False)
def df():
    print 'df'
    rand1 = random.randint(0, 100)
    rand2 = random.randint(0, 100)
    rand3 = random.randint(0, 100)
    return {
        'data_map': {
            'df': {
                'type': 'table',
                'data': {
                    '/dev/sda1': rand1,
                    'tmpfs': rand2,
                    '/vagrant': rand3,
                }
            }
        }
    }

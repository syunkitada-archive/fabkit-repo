# coding: utf-8

from fabkit import *  # noqa


@task
def setup():
    log.console("debug")

    return {
        'status': 1,
    }


@task
def check():
    return {'status': 0}

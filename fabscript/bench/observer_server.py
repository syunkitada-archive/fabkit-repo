# coding: utf-8

from fabkit import *  # noqa

observer = Observer()


@task
def setup():
    return {
        'status': 1,
    }


@task
def check():
    return {'status': 0}

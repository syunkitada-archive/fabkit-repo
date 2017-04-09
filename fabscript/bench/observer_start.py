# coding: utf-8

from fabkit import *  # noqa

observer = Observer()


@task
@api.parallel
def setup():
    log.console("start observer")
    observer.start()

    return {
        'status': 1,
    }


@task
def check():
    return {'status': 0}

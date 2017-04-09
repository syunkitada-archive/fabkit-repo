# coding: utf-8

from fabkit import *  # noqa

observer = Observer()


@task
@api.parallel
def setup():
    log.console("stop observer")
    observer.stop()

    return {
        'status': 1,
    }


@task
def check():
    return {'status': 0}

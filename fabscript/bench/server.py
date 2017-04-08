# coding: utf-8

import time
from fabkit import *  # noqa

observer = Observer()


@task
def setup():
    log.console("debug")

    observer.start()

    print 'sleep 5'
    time.sleep(5)

    observer.stop()

    return {
        'status': 1,
    }


@task
def check():
    return {'status': 0}

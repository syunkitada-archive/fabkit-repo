# coding: utf-8

from fabkit import *  # noqa
import time

observer = Observer()


@task
@api.parallel
def setup():
    log.console("start wrk")
    observer.wrk(c=1, t=1, d=10, url='http://192.168.122.101/')
    time.sleep(5)
    observer.update_stats()
    time.sleep(5)
    observer.update_stats()
    time.sleep(5)
    observer.update_stats()

    return {
        'status': 1,
    }


@task
def check():
    return {'status': 0}

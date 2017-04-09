# coding: utf-8

from fabkit import *  # noqa


@task
@api.parallel
def setup():
    Package('wget').install()
    Package('git').install()
    if not filer.exists('/usr/bin/wrk'):
        run('wget https://github.com/wg/wrk/archive/4.0.2.tar.gz')
        run('tar xf 4.0.2.tar.gz')
        run('cd wrk-4.0.2 && make')
        sudo('cp wrk-4.0.2/wrk /usr/bin/')

    return {
        'status': 1,
    }


@task
def check():
    return {'status': 0}

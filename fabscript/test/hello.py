# coding: utf-8

from fabkit import task, env


@task(is_bootstrap=False)
def setup():
    print '{0}: hello'.format(env.host)
    print env.cluster
    # run('touch /tmp/test')

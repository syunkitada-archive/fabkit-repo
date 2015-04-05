from fabkit import task, env


@task(is_bootstrap=False)
def setup():
    print 'hello {0}\n'.format(env.host)  # out


@task(is_bootstrap=False)
def check():
    return {'status': 0}

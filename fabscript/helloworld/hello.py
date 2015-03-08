from fabkit import task, run, env


@task
def setup():
    run('hostname')
    print env.cluster['msg']

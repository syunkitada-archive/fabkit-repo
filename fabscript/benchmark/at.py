# coding: utf-8

from fabkit import *  # noqa


at_times = []
args = [
    {'clients': 100, 'requests': 100},
    {'clients': 100, 'requests': 500},
    {'clients': 100, 'requests': 1000},
]


@task
def setup():
    global at_time, args

    interval = 3

    for len_time in range(1, len(args) + 1):
        span = len_time * interval
        if env.hosts[0] == env.host:
            at_time = str(run('date +"%H:%M %d.%m.%y" -d "{0} minute"'.format(span)))
            at_times.append(at_time)

    print at_times
    print args
    for i, arg in enumerate(args):
        at_time = at_times[i]
        script_file = '/tmp/at_ab_{0}.sh'.format(i)
        filer.template(script_file, data=arg, src='at_ab.sh')
        run('at {0} -f {1}'.format(at_time, script_file))

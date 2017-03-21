# coding: utf-8

from fabkit import *  # noqa


@task
def setup():
    result = run('ab -n 1000 -c 100 http://192.168.122.101/')
    results = str(result).split('\n')
    data = {}
    for r in results:
        kv = r.split(':')
        if len(kv) < 2:
            continue
        key = kv[0]
        value = kv[1]
        value = value.strip()
        if key == 'Concurrency Level':
            key = 'concurrency'
        elif key == 'Requests per second':
            key = 'rps [#/sec]'
            value = value.split(' ')[0]
        elif key == 'Time per request':
            key = 'tps [ms]'
            value = value.split(' ')[0]
        elif key == 'Complete requests':
            key = 'requests'
        elif key == 'Failed requests':
            key = 'failed requests'
        elif key == 'Write errors':
            key = 'errors'
        else:
            continue
        data[key] = value

    return {
        'status': 0,
        'data_map': {
            'ab': {
                'type': 'table',
                'data': data,
            }
        }
    }

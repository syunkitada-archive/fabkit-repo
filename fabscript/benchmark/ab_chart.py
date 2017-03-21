# coding: utf-8

from fabkit import *  # noqa


@task
def setup():
    clients = 100
    requests = [100, 500, 1000, 1500, 2000, 4000]
    data = {
        'x': requests,
        'y': [ab(r, clients) for r in requests],
    }

    return {
        'status': 0,
        'data_map': {
            'ab_chart': {
                'type': 'line-chart',
                'data': data,
                'ex_data': [
                    {
                        'name': 'sum',
                        'x': 'data_0_x',
                        'y': 'sum(y)',
                    },
                ],
                'layout': {
                    'title': 'Apache Bench',
                    'xaxis': {
                        'title': 'Requests',
                        'showgrid': False,
                        'zeroline': True,
                    },
                    'yaxis': {
                        'title': 'RPS',
                        'showline': False,
                        'zeroline': True,
                    },
                }
            }
        }
    }


def ab(requests=1000, clients=100):
    result = run('ab -n {0} -c {1} http://192.168.122.101/'.format(requests, clients))
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
            key = 'rps'
            value = float(value.split(' ')[0])

        data[key] = value

    return data['rps']

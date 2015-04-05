# coding: utf-8

from fabkit import task, filer


@task
def setup():
    filer.template('/tmp/test_template', data={'msg': 'world'})
    filer.file('/tmp/test_file')

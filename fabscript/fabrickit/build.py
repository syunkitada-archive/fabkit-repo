# coding: utf-8

from fabkit import *  # noqa


@task
def setup():
    python_version = '2.7.13'
    python = 'Python-{0}'.format(python_version)
    python_tgz = '{0}.tgz'.format(python)

    if not filer.exists(python_tgz):
        run('wget https://www.python.org/ftp/python/{0}/{1}'.format(python_version, python_tgz))

    if not filer.exists(python):
        run('[ -e {0} ] || tar xzf {1}'.format(python, python_tgz))

    sudo('yum groupinstall -y "Development tools"')
    sudo('yum install -y zlib-devel bzip2-devel python-devel openssl-devel'
         'ncurses-devel sqlite-devel readline-devel tk-devel')

    if not filer.exists('/tmp/python27/bin/pip'):
        with api.cd(python):
            run('./configure --prefix=/tmp/python27')
            run('make')
            run('make altinstall')

        run('wget https://bootstrap.pypa.io/get-pip.py')
        run('/tmp/python27/bin/python2.7 get-pip.py')

    sudo('rm -rf /tmp/fabkit-repo')
    run('mkdir /tmp/fabkit-repo')
    with api.cd('/tmp/fabkit-repo'):
        run('git clone https://github.com/fabrickit/fabkit.git fabfile')
        run('/tmp/python27/bin/pip install -r fabfile/requirements.txt')
        run('cp -r /tmp/python27 /tmp/fabkit-repo/.python27')
        filer.template('/tmp/fabkit-repo/.gitignore')
        run('.python27/bin/fab -l')
        run('.python27/bin/fab -e genconfig')
        run('mv fabfile.ini.sample fabfile.ini')
        run('cp fabfile/etc/local_settings.py.sample conf/local_settings.py')
        run('cd .python27/bin/; ln -s python2.7 python')

    with api.cd('/tmp'):
        run('tar czf fabkit-repo.tar.gz fabkit-repo')

    scp('/tmp/fabkit-repo.tar.gz', '/tmp/fabkit-repo.tar.gz', is_local=False, is_receive=True)

    return {'status': 0}

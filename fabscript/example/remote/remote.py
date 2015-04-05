# coding: utf-8

from fabkit import task, sudo, api, run, Package


@task
def setup():
    Package('python-crypto').uninstall()
    Package('python-devel').install()
    Package('libevent-devel').install()
    Package('libxml2-devel').install()
    Package('libxslt-devel').install()

    with api.warn_only():
        if run('which easy_install').return_code != 0:
            sudo('wget https://bootstrap.pypa.io/ez_setup.py -O - | python')
        if run('which pip').return_code != 0:
            sudo('easy_install pip')

    sudo('pip install fabric==1.10.1')
    sudo('pip install pyyaml==3.11')
    sudo('pip install jinja2==2.7.3')
    sudo('pip install Django==1.6.5')

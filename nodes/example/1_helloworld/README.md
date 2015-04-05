# hello world

``` bash
# setup node
$ fab node:example/helloworld/ setup

# check node
$ fab node:example/helloworld/ check

# manage node
# manage:[task name(regx)]
$ fab node:example/helloworld/ manage:touch

# manage node
# boot task dosen't execute bootstrap
# @task(is_bootstrap=False)
# def boot():
#   ...
$ fab node:example/helloworld/ manage:boot
```

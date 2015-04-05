# execution sequence

## execute multi setup task
``` bash
% fab node:example/2_execution_sequence/multi setup
[localhost] Executing task 'node'
----------------------------------------------------------------------------------
cluster                      host           fabscript
----------------------------------------------------------------------------------
example/2_execution_sequence multi.mydns.jp example/execution_sequence/multi_setup: 0 > 0

...
[multi.mydns.jp] Executing task 'setup1'
setup 1
...
[multi.mydns.jp] Executing task 'setup2'
setup lib 2
...
[multi.mydns.jp] Executing task 'setup3'
setup 3
```

## execute run relation setup task
``` bash
% fab node:example/2_execution_sequence/[web+api+db] setup
[localhost] Executing task 'node'
--------------------------------------------------------------------------------
cluster                      host         fabscript
--------------------------------------------------------------------------------
example/2_execution_sequence db1.mydns.jp example/execution_sequence/db: 0 > 1
example/2_execution_sequence db2.mydns.jp example/execution_sequence/db: 0 > 1
example/2_execution_sequence db1.mydns.jp example/execution_sequence/db: 0 > 2
example/2_execution_sequence db2.mydns.jp example/execution_sequence/db: 0 > 2
example/2_execution_sequence api.mydns.jp example/execution_sequence/api: 0 > 1
example/2_execution_sequence web.mydns.jp example/execution_sequence/web: 0 > 1

...
[db1.mydns.jp] Executing task 'setup'
setup db
...
[db2.mydns.jp] Executing task 'setup'
setup db
...
[db1.mydns.jp] Executing task 'setup'
sync db
...
[db2.mydns.jp] Executing task 'setup'
sync db
...
[api.mydns.jp] Executing task 'setup'
setup api
...
[web.mydns.jp] Executing task 'setup'
setup web
```

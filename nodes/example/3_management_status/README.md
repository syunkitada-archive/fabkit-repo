# management status

There are three types of status.

* status
    * This is status to control execution sequence.
    * See 'execution sequence'.
* check_status
    * This is status check task returns.
    * Check task returns 0 if successful, returns a value of 1 or more otherwise.
    * Default value is -1.
* task_status
    * This is task_status task returns.
    * Task returns 0 if successful, returns a value of 1 or more otherwise.
    * Default value is 0.
    * When you run the task, task_status is automaticaly updated.
    * If when the task was stopped for some exceptions, or the task returns a value greater than or equal to 1, suspends the subsequent execution. And you will be able to notice if by status is not 0.

``` bash
% fab node:example/3_status/success setup
[localhost] Executing task 'node'
------------------------------------------------------------------------
cluster          host             fabscript
------------------------------------------------------------------------
example/3_status success.mydns.jp example/status/success: 0 > 0

[success.mydns.jp] Executing task 'setup'
setup success
INFO:example/3_status/success.mydns.jp:Success task example/status/success.setup [0]. success


% fab node:example/3_status/danger setup
[localhost] Executing task 'node'
-----------------------------------------------------------------------
cluster          host            fabscript
-----------------------------------------------------------------------
example/3_status danger.mydns.jp example/status/danger: 0 > 0

[danger.mydns.jp] Executing task 'setup'
ERROR:example/3_status/danger.mydns.jp:Failed task example/status/danger.setup [11]. failed
ERROR:root:Failed task example/status/danger.setup. Exit setup.
```

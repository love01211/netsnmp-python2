python2的netsnmp模块

环境：
python 2.7
snmpd 5.7.2

安装使用：
python setup.py build
python setup.py test
#上面都不报错，再执行此步骤，否则也不可用
python setup.py install

验证：
```python
$ python
>>> import netsnmp
>>> help(netsnmp)

Help on package netsnmp:

NAME
    netsnmp

FILE
    /root/test/netsnmp-python2/netsnmp/__init__.py

PACKAGE CONTENTS
    client
    client_intf
    tests (package)

DATA
    secLevelMap = {'authNoPriv': 2, 'authPriv': 3, 'noAuthNoPriv': 1}
    stderr = <open file '<stderr>', mode 'w'>
    verbose = 1

(END)
```

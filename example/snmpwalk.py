#!/usr/bin/python
#encoding=utf-8
#description:测试netsnmp.snmpwalk中Timeout值对应的具体时间
# Timeout参数的时间为Timeout/1000000/4 秒，即如果Timeout=10^6，则超时时间为4秒！
# 不加Timeout参数，则超时时间默认为4秒
import time
import netsnmp

sysName_oid = netsnmp.Varbind("sysName")#系统名称
location_oid = netsnmp.Varbind("sysLocation") #物理位置
sysContact_oid = netsnmp.Varbind("sysContact") #联系人信息

startTime=time.time()
result = netsnmp.snmpwalk(location_oid,sysContact_oid,sysName_oid,Version = 2,DestHost='192.168.113.138', Community='public',Timeout=1000000)
endTime=time.time()

costTime=endTime-startTime

print costTime
print result[0]

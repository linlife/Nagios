#!/usr/bin/env python
import os
import sys
import time
import paramiko
import re


ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('10.10.20.110', 11658, 'root', 'bMoE&xqI7h')
stdin, stdout, stderr = ssh.exec_command('cat /data/nagios/phone/phonelist.txt')
phone=[line for line in stdout.read().strip().split('\n') if re.match(r'\d{11}',line)]
ssh.close()


fpath=['/etc/passwd','/etc/my.cnf']


localip=os.popen("ifconfig |grep -v '127' | grep 'inet addr' |awk  '{print $2}'|awk -F: '{print $2}'").read().strip()


if os.path.isfile('/usr/local/nagios/libexec/linmdfile'):
    pass
else:
    os.popen("echo %s >/usr/local/nagios/libexec/linmdfile && chmod 666 /usr/local/nagios/libexec/linmdfile"%fstr)

ostr=os.popen("cat /usr/local/nagios/libexec/linmdfile").read().strip()
for fline in fpath:
    fstr=fline+':'+os.popen("stat %s | grep Modify | awk '{print $2,$3}'"%fline).readline().strip()+'$'


if ostr==fstr:
    print 'no file be changed ,everything is ok now !'
    sys.exit(0)
else:
    a=ostr.split('$')
    b=fstr.split('$')
    for i in range(len(a)):
        if a[i]!=b[i]:
            print 'file:',b[i].split(':')[0],' has been changed just now,please note!'
            smsstr='IP:%s file:'%localip+b[i].split(':')[0]+' has been changed just now,please note!'
            os.popen("echo %s > /usr/local/nagios/libexec/linmdfile"%fstr)
            for num in phone:
                os.popen("links --dump 'http://smsapi.tg.com.cn:3338/SendSmsForYunwei.aspx?mobile=%s&smscontent=%s'"%(num,smsstr))
            sys.exit(1)
        

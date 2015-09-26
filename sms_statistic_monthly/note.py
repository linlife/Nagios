#!/usr/bin/env python
#_*_ coding:utf-8 _*_
import os



serversdir='/usr/local/nagios/etc/servers'
logsdir='/usr/local/nagios/var/archives'
serverip=[]
totally={}
log201503=[]
log201504=[]
log201505=[]


for root,dirs,files in os.walk('%s'%serversdir):
    for f in files:
        serverip.append(f.split('.')[0])

serverip.sort()
for f in serverip:
    totally['%s'%f]=[]

for root,dirs,files in os.walk('%s'%logsdir):
    for f in files:
        newf=f.split('-')
        if newf[3]=='2015' and newf[1]=='03':
            log201503.append(f)
        if newf[3]=='2015' and newf[1]=='04':
            log201504.append(f)
        if newf[3]=='2015' and newf[1]=='05':
            log201505.append(f)
        
log201503.sort()
log201504.sort()
log201505.sort()

os.chdir('%s'%logsdir)

for sname in serverip:
    warning=[]
    critical=[]
    for logs in log201503:
        warning.append(int(os.popen("cat %s | grep WARNING | grep %s | wc -l"%(logs,sname)).read().strip()))
        critical.append(int(os.popen("cat %s | grep CRITICAL| grep %s | wc -l"%(logs,sname)).read().strip()))
       # critical.append(int(os.popen("grep %s %s|grep WARNING | wc -l"%(sname,logs)).read().strip()))
    totally['%s'%sname].append(sum(warning)+sum(critical))

    warning=[]
    critical=[]
    for logs in log201504:
        warning.append(int(os.popen("cat %s | grep WARNING | grep %s | wc -l"%(logs,sname)).read().strip()))
        critical.append(int(os.popen("cat %s | grep CRITICAL| grep %s | wc -l"%(logs,sname)).read().strip()))
      #  critical.append(int(os.popen("grep %s %s|grep WARNING | wc -l"%(sname,logs)).read().strip()))
    totally['%s'%sname].append(sum(warning)+sum(critical))
    warning=[]
    critical=[]
    for logs in log201504:
        warning.append(int(os.popen("cat %s | grep WARNING | grep %s | wc -l"%(logs,sname)).read().strip()))
        critical.append(int(os.popen("cat %s | grep CRITICAL| grep %s | wc -l"%(logs,sname)).read().strip()))
       # critical.append(int(os.popen("grep %s %s|grep WARNING | wc -l"%(sname,logs)).read().strip()))
    totally['%s'%sname].append(sum(warning)+sum(critical))


for line in serverip:
    print line, 'March:',totally['%s'%line][0],'  April:',totally['%s'%line][1],'  May:',totally['%s'%line][2]
'''
os.chdir('/root/lin')
f=open('message2.xlsx','a')
f.write('IP\tMarch\tApril\tMay\n')
for line in serverip:
    f.write('%s\t%s\t%s\t%s\n'%(line,totally['%s'%line][0],totally['%s'%line][1],totally['%s'%line][2]))

'''





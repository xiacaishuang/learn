# -*- coding: UTF-8 -*-
import sys,os,time
#fh = open(sys.argv[1])
count=0
error_count=0
flag = 0
flag1= 0
s1=''
s2=''
files = open(sys.argv[1])


def func(s):
    if s[13:14]!='[':
        if s[8:10] != '**':
            #print '>>>>>>>>>>>>>>>'
            #print time.mktime(time.strptime(s[28:36], '%H:%M:%S'))
            return time.strptime(s[28:36], '%H:%M:%S')
        else:
           # print '---------------'
           # print time.mktime(time.strptime(s[26:34],'%H:%M:%S'))
            return time.strptime(s[26:34],'%H:%M:%S')

    else:
       # print '++++++++++++++++++++'
       # print time.mktime(time.strptime(('0'+s[26:33]), '%H:%M:%S'))
        return time.strptime(('0'+s[26:33]), '%H:%M:%S')



for line in files.readlines():
    if '****' in line:
        if flag == 0:
            s1=line
            flag =1
            #s_time=s[26:34]
        else:
            s2=line
    if ':9:' in line:
        #print s
        #print s_time
        count=count+1
        if flag1 == 0:
            a=line
            flag1=1
        else:
            b=line

            first = func(s1)
            second = func(s2)
            if ((time.mktime(second)-time.mktime(first))!=1.0) and ((time.mktime(second)-time.mktime(first))!=0.0):
                if ((abs(time.mktime(second)-time.mktime(first))) < 5.0):
                    print ("%s\n%s\n%s\n%s\n"%(s1,a,s2,b))
                    error_count=error_count+1
                    #s1=s2
                    #a=b
                    print ('时间差:%ss\n\n\n'%abs(time.mktime(second)-time.mktime(first)))
            s1=s2
            a=b
print ('Count All:%s,Error count:%s\n'%(count,error_count))
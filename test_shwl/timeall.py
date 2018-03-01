import sys,os
import time
#fh = open(sys.argv[1])

def func(s):
    return time.strptime(s[20:28], '%H:%M:%S')

files = os.listdir(sys.argv[1])
#files = os.listdir('./nv')
for file in files:
    print('Check File:%s\n'%file)
    flag=0
    count = 0
    error_count = 0
    err_flag = 0
    s1=''
    s2=''
    if 'init' not in file:
        #fh = open('./nv/'+file)
        fh = open(sys.argv[1] +'/'+ file)
        #print ('file:%s'%file)
        for line in fh.readlines():
            if 'INFO'in line or 'DEBUG' in line or 'ERROR' in line:
                if flag==0:
                    s1=line
                    flag=1
                else:
                    s2=line
                    if(time.mktime(func(s2)) - time.mktime(func(s1))) > 1.0:
                        error_count=error_count+1
                        err_flag=1
                        print('Time Error At:%s\n              %s\n'%(s1,s2))
                    s1=s2
                count=count+1

        if err_flag == 0:
            print ('File:%s------------pass\n'%file)
            print ('File:%s  Count Time All:%s  Count Time Error:%s\n\n' % (file, count, error_count))
        else:
            print('File:%s-------------fail\n'%file)
            print ('File:%s  Count Time All:%s  Count Time Error:%s\n\n' % (file,count, error_count))
        fh.close()
print('All File Checked\n')


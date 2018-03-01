import sys,os
#fh = open(sys.argv[1])

flag = 0
files = os.listdir(sys.argv[1])
#files = os.listdir('./nv')
for file in files:
    count = 0
    error_count = 0
    flag = 0
    if 'init' not in file:
        #fh = open('./nv/'+file)
        fh = open(sys.argv[1] +'/'+ file)
        #print ('file:%s'%file)
        for line in fh.readlines():
            if 'INFO'in line or 'DEBUG' in line or 'ERROR' in line:
                count=count+1
                if line[12:14]!=line[41:43] and abs(int(line[12:14])-int(line[41:43]))>1:
                    error_count=error_count+1
                    print ('Time error at:%s ' % (line))
                    flag = 1
        if flag == 0:
            print ('File:%s------------pass\n'%file)
            print ('File:%s  Count Time All:%s  Count Time Error:%s\n\n' % (file, count, error_count))
        else:
            print('File:%s-------------fail\n'%file)
            print ('File:%s  Count Time All:%s  Count Time Error:%s\n\n' % (file,count, error_count))
        fh.close()
print('All File Checked\n')


import sys,os
#fh = open(sys.argv[1])
flag = 0
files = os.listdir(sys.argv[1])
#files = os.listdir('./nv')
for file in files:
    if 'init' not in file:
        #fh = open('./nv/'+file)
        fh = open(sys.argv[1] +'/'+ file)
        print ('file:%s'%file)
        for line in fh.readlines():
            if 'nv' in line:
                if 'error' in line:
                    print ('nv error at:%s ' % (line))
                    flag = 1
        if flag == 0:
            print ('----------------pass\n')
        else:
            print('----------------fail\n')
            flag = 0
        fh.close()


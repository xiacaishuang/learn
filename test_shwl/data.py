# -*- coding: UTF-8 -*-
import sys,os
import time
import xlrd
#fh = open(sys.argv[1])

def func(s):
    return time.strptime(s[11:19], '%H:%M:%S')
def detail(l):
    for ss in l:
        print (ss,'',end='')
    print('\n')

files = os.listdir(sys.argv[1])
file_count=0
err=0
#files = os.listdir('./nv')
for file in files:
    file_count=file_count+1
    flag=0
    count = 0
    error_count = 0
    err_flag = 0
    s1=''
    s2=''
    if 'init' not in file:
        print('Check File:%s\n' % file)
        #fh = open('./nv/'+file)
        file_path= sys.argv[1] +'/'+ file
        #print ('file:%s'%file)

        workbook = xlrd.open_workbook(file_path)
        sheet_name=workbook.sheet_names()[0]
        sheet = workbook.sheet_by_name(sheet_name)
        #print (sheet.name, sheet.nrows, sheet.ncols)
        #print (sheet.row_values(4).encode('utf-8'))

        #print sheet.cell(5, 1).value.encode('utf-8')
        for row in range(5,sheet.nrows):
            if flag==0:
                s1=sheet.cell(row, 1).value
                x=sheet.row_values(row)[0:3]#encode('utf-8')
                flag=1
            else:
                s2 = sheet.cell(row, 1).value
                y = sheet.row_values(row)[0:3]#encode('utf-8')
                if abs(time.mktime(func(s2)) - time.mktime(func(s1))) > 10.0:
                    if abs(time.mktime(func(s2)) - time.mktime(func(s1))) !=86390.0:
                        error_count=error_count+1
                        err_flag=1
                        #print ('Error At:\n%s\n%s\n'%(s1,s2))
                        print ('Error At:')
                        detail(x)
                        detail(y)
                #print('\n')

                s1=s2
                x=y
            count=count+1
            #print sheet.cell(row, 1).value#encode('utf-8')
    print ('****File:%s'%file)
    if err_flag == 0:
        print ('Result:Pass\nCount :%s\n' % count)
        #print ('File:%s   Count :%s\n\n' % (file, count))
    else:
        #print('File:%s-------------fail\n' % file)
        #print ('File:%s  Count All:%s  Count  Error:%s\n\n' % (file, count,error_count))
        print ('Result:Fail\nCount :%s  Error Count:%s\n' % (count,error_count))
        err=err+1
print('\n********Check File:%d  Error File:%d'%(file_count,err))
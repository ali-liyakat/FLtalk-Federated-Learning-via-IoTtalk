import csv



dictwriter_count = 1

def Dummy_Control(data):
    global dictwriter_count

    ''' **** Data collection start ***** '''

    with open('test.csv','a',newline='') as file:
        writer=csv.DictWriter(file,['acc1','acc2','acc3','gyro1','gyro2','gyro3'])

        global dictwriter_count
        print("----- count  =  ",dictwriter_count)
        print(data[0][0],data[0][1],data[0][2],data[0][3],data[0][4],data[0][5])

        
        writer.writerow({'acc1':data[0][0],'acc2':data[0][1],'acc3':data[0][2],
                         'gyro1':data[0][3],'gyro2':data[0][4],'gyro3':data[0][5]})

        dictwriter_count=dictwriter_count + 1
        print("**********")

        ''' ***** Data collection end ***** '''

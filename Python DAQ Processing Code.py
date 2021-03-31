import serial    #this code has good csv out data 
import matplotlib as plt
import numpy as np
import datetime
import time
import csv
from drawnow import *

te1 = []
te2 = []
te3 = []
te4 = []
te5 = []
te6 = []
te7 = []
te8 = []
te9 = []
te10 = []
te11 = []
te12 = []
te13 = []
te14 = []
te15 = []
te16 = []
teTime = []
arduinoData = serial.Serial('COM5', 9600)
plt.ion()
cnt=0
x = [datetime.datetime.now() + datetime.timedelta(hours=i) for i in range(12)]

def makeFig(): #create a function that makes our desired plot
     plt.ylim(26,50)
     #plt.yticks(np.arange(26,50,1))
     plt.title('Temp Sensor')
     plt.ylabel ('Temperature')
     
     plt.xlabel('Seconds')
     plt.cla()
     plt.grid(True)
     plt.plot(te1, 'r^-', label ='Sensor 1')
     plt.plot(te2, 'b^-', label ='Sensor 2')
     plt.plot(te3, 'g^-',label = 'Sensor 3')
     plt.plot(te4, 'm^-',label = 'Sensor 4')
     plt.plot(te5, 'y^-',label = 'Sensor 5')
     plt.plot(te6, 'c^-',label = 'Sensor 6')
     plt.plot(te7, 'k^-',label = 'Sensor 7')
     plt.plot(te8, 'ro-', label ='Sensor 8')
     plt.plot(te9, 'bo-', label ='Sensor 9')
     plt.plot(te10, 'go-',label = 'Sensor 10')
     plt.plot(te11, 'mo-',label = 'Sensor 11')
     plt.plot(te12, 'yo-',label = 'Sensor 12')
     plt.plot(te13, 'co-',label = 'Sensor 13')
     plt.plot(te14, 'ko-',label = 'Sensor 14')
     #plt.plot(te15, 'gd-',label = 'Sensor 15')
     #plt.gcf().autofmt_xdate()
     plt.legend(loc='upper left')
     #plt.show()
     



while True:
     arduinoString1 = arduinoData.readline()
     arduinoString = arduinoString1.decode('utf-8')
     arduinoString
     dataArray = arduinoString.split(",")
     #print (dataArray)

     t1 = float(dataArray[0])
     t2 = float(dataArray[1])
     t3 = float(dataArray[3])
     t4 = float(dataArray[4])
     t5 = float(dataArray[5])
     t6 = float(dataArray[6])
     t7 = float(dataArray[7])
     t8 = float(dataArray[8])
     t9 = float(dataArray[9])
     t10 = float(dataArray[10])
     t11 = float(dataArray[11])
     t12 = float(dataArray[12])
     t13 = float(dataArray[13])
     t14 = float(dataArray[14])
     #t15 = float(dataArray[15])
     #t16 = float(dataArray[16])
     #t17 = float(dataArray[17])
    
     #te1.append(t0)
     te1.append(t1)
     te2.append(t2)
     te3.append(t3)
     te4.append(t4)
     te5.append(t5)
     te6.append(t6)
     te7.append(t7)
     te8.append(t8)
     te9.append(t9)
     te10.append(t10)
     te11.append(t11)
     te12.append(t12)
     te13.append(t13)
     te14.append(t14)
     teTime = time.asctime()
     
     tempdat = np.array([te1, te2, te3, te4, te5, te6, te7, te8, te9, te10, te11, te12, te13, te14])
     tempdat
     with open("test_data_pycode.csv","w") as f:
              mywriter = csv.writer(f,delimiter=",",lineterminator='\n') #
              mywriter.writerows(tempdat.T)         
              
               
     #te15.append(t15)
    #te16.append(t16)
    #te17.append(t17)
     
    


     drawnow(makeFig)
     plt.pause(0.000001)
     cnt=cnt+1
     if(cnt>5000):
          te1.pop(0)
          te2.pop(0)
          te3.pop(0)
          te4.pop(0)
          te5.pop(0)
          te6.pop(0)
          te7.pop(0)
          te8.pop(0)
          te9.pop(0)
          te10.pop(0)
          te11.pop(0)
          te12.pop(0)
          te13.pop(0)
          te14.pop(0)
          te15.pop(0)

"""

"""


import socket
import time
import numpy as np
import matplotlib.pyplot as plt
datas=[] 
nop=5 #number of points for averaging/Filtering
start_time=time.time() #starting system time
TCP_IP = '192.168.0.185' #change your ip address
TCP_PORT = 23 
BUFFER_SIZE = 1024


timed=[]; #time data
pm03=[]; #0.3 micron particle count , refer to datasheet for checking which column of streamed data you want
#0 : time
#7 : 0.3 micron counts
#8 : 0.5 micron counts
#9 :1.0 micron counts
#10: 2.5 micron counts
#11: 5 micron counts
#12: 10 micron counts
for k in range(1000): #set how long you want to receive data
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #set up 
    s.settimeout(15) # set timeout in case signal drops
    try:
        s.connect((TCP_IP, TCP_PORT))

        data = str(s.recv(BUFFER_SIZE),'utf-8')
        d1=data.split()
        s.close()

        d2=[]
        for i in range(len(d1)):
            if (i==0):
                d2.append(time.time()-start_time) #time related to start of experiment
            else :
                d2.append(float(d1[i]))
        d2=np.array(d2)
        d2=d2.reshape(1,-1)
        if(k==0):
            datas=np.array(d2)
        else:
           datas= np.append(datas,d2,axis=0)
        if(k<=nop):
            print('Initialising')
        elif(k==nop):
            print('ready')
            plt.figure()
            plt.xlabel('Time in Seconds')
            plt.ylabel('0.3 micron count')
        elif(k>nop):
            timed.append(datas[k,0])
            pm03.append(np.mean(datas[k-nop:k,7]))
            
            plt.plot(timed,pm03,'r*-')  
        
            plt.pause(3)
            print("received data:", data)
    except socket.timeout:
        #print('waiting')
        continue

np.savetxt("data.csv", datas, delimiter=",")  #export raw data to external file
    


    

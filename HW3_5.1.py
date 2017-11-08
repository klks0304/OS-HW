#5.1
#run module

import matplotlib.pyplot as plt
import numpy as np
#import math
#calculate the running time
def att(process,m):
    t_list = []
    t = 0
    P = np.array([i for i in process if i >0])
    #the above P is filtering those unreasonable process time.
    while(P.size!=0): #len(P)
        P = np.array([i-m for i in list(P)])
        #P -= m
        ended = np.where(P<=0)[0]
        for i in ended:
            t_list.append(t + m*(i+1)+P[i])
            t += P[i]
        t += P.size*m
        P = np.delete(P,ended)
    return np.mean(t_list)

#variable setting
Process_time = [6,3,1,7]
m = 7

#plot using matplotlib
x = range(1,m+1)
y = [att(Process_time,i) for i in x]
plt.figure(figsize=(12,6))
plt.plot(x,y)
plt.title('Turnaround Time Varies With \nThe Time Quantum')
plt.xlabel('time quantum')
plt.ylabel('average turnaround time')
plt.xlim(1,max(x)+1)
plt.ylim(min(y)-1,max(y)+1)
plt.axes().set_aspect(2)
plt.grid(True)
cell_text = [['P' +str(i+1),Process_time[i]] for i in range(len(Process_time))]

#the following variables are for adjusting the figure/table size and location
#irralevent to the hw problem
Table = plt.table(cellText=cell_text,colLabels=['process','time'],colWidths=[0.5, 0.4],loc="right", bbox=[1.2, 0.3, 0.5, 0.5])
plt.suptitle('0586010 Tseng', style='italic', y=0, fontsize=14)
plt.show()



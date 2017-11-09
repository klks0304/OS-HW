#5.4
#alpha = 0.5 is given
#tau_1 = 10 is given
#CPU burst =[6,6,4,6,4,13,13,13] is given
#teacher will randomly add some number in the CPU burst list

import matplotlib.pyplot as plt
import numpy as np

#variable setting
CPU_burst = [6,6,4,6,4,13,13,13,100,50] #the last 2 are randomly added
guess_time = [10]
#tau = 10
#t = 6
alpha = 0.5
for i in range(len(CPU_burst)-1):
    guess_time.append(alpha*guess_time[i]+(1-alpha)*CPU_burst[i])

#output figure of 5.4
#from scipy.interpolate import spline
x = range(len(guess_time))
y = guess_time
plt.figure(figsize=(6,6))
plt.xlim(1,max(x)+1)
plt.ylim(0,max(CPU_burst)+1)
plt.plot(x,guess_time)
plt.plot(x,CPU_burst)
plt.xticks(np.arange(0,len(CPU_burst),1))
plt.legend(['guess (Taui)','CPU burst (ti)'], loc='upper left')
plt.title('Prediction of the Length of the Next CPU Burst')
plt.xlabel('time ->')
plt.grid(True)
#plt.axes().set_aspect(0.1)
plt.suptitle('wolfe', style='italic', y=-0.5, fontsize=12)
#cell_text = ['CPU burst (ti)']
Table = plt.table(cellText=[CPU_burst+["..."],guess_time+["..."]],rowLabels=['CPU burst (ti)','"guess"(Taui)'],loc="bottom", bbox=[0, -0.2, 1.2 ,0.1])
#the table may not be on a perfect location
#can be adjust after output

plt.show()

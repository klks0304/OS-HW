#5.3
#In homework 5.3, we have to create a graph "same" as the one in the given pdf file
#There are some problems by creating the exactly same graph, therefore line chart is allowed
#the blue line in 5.3 is also allowed to show in line chart instead of smooth curve

import matplotlib.pyplot as plt

CPU_burst = [6,6,4,6,4,13,13,13]
guess_time = [10,8,6,6,5,9,11,12]

#output figure of 5.3
#from scipy.interpolate import spline
x = range(len(guess_time))
y = guess_time
plt.figure(figsize=(6,8))
plt.xlim(1,max(x)+1)
plt.ylim(0,max(CPU_burst)+1)
plt.plot(x,guess_time)
plt.plot(x,CPU_burst)
plt.legend(['guess (Taui)','CPU burst (ti)'], loc='upper left')
plt.title('Prediction of the Length of the Next CPU Burst')
plt.xlabel('time ->')
plt.axes().set_aspect(0.4)
plt.suptitle('wolfe', style='italic', y=-0.3, fontsize=12)
plt.grid(True)
#plt.xticks(0,8,1)
#cell_text = ['CPU burst (ti)']
Table = plt.table(cellText=[CPU_burst+["..."],guess_time+["..."]],rowLabels=['CPU burst (ti)','"guess"(Taui)'],loc="bottom", bbox=[0.3, -0.5, 0.7, 0.3])

plt.show()

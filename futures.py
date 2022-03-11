import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os


def merge(s1, s2,mode):
    l1 = os.listdir(s1)
    l2 = os.listdir(s2)
    f1 = []
    f2 = []
    v1 = []
    v2 = []
    l1 = l1[14:20]
    print(l1)
    print(l2)



    for i in range(len(l1)):

        p1 = pd.read_csv(s1+l1[i])
        p2 = pd.read_csv(s2+l2[i])
        p1 = p1.to_numpy()
        p2 = p2.to_numpy()
        p1_close = []
        p2_close = []

        print(i)
        for i in range(p2.shape[0]):
            for j in range(p1.shape[0]):

                if ((p2[i][0] == p1[j][0]) & (mode == 'h')):
                    p1_close.append(p1[j][2])
                    p2_close.append(p2[i][2])
                if ((p2[i][0] == p1[j][0]) & (mode == 'l')):
                    p1_close.append(p1[j][3])
                    p2_close.append(p2[i][3])
                if ((p2[i][0] == p1[j][0]) & (mode == 'c')):
                    p1_close.append(p1[j][4])
                    p2_close.append(p2[i][4])
                if ((p2[i][0] == p1[j][0]) & (mode == 'v')):
                    p1_close.append(p1[j][5])
                    p2_close.append(p2[i][5])


        f1 = f1 + p1_close
        f2 = f2 + p2_close


    return f1 , f2


a1 = 'spot/adausdt/1h/'
a2 = 'futures/cm/924/ADAUSD/1h/'

spot , futures = merge(a1,a2,'h')

diff = []
per = []

for i in range(len(spot)-2):
    diff.append((futures[i]-spot[i])/spot[i] *100)
    per.append(((spot[i+1]-spot[0])/spot[0]))




x = []


for i in range(len(diff)):
    x.append(i)

y = []

for i in range(len(spot)):

    y.append(i)




plt.plot(x,diff)
plt.title('ADAUSDT future and spot price difference')
plt.xlabel('time (hours)')
plt.ylabel('price difference (percent)')
plt.savefig('futures results/924/ada/diff_1h.png', dpi=None, facecolor='w', edgecolor='w',
        orientation='portrait', papertype=None, format=None,
        transparent=False, bbox_inches=None, pad_inches=0.1,
        frameon=None, metadata=None)

plt.figure()
plt.plot(y,spot,y,futures)
plt.title('ADAUSDT future and spot price')
plt.xlabel('time (hours)')
plt.ylabel('price ($)')
plt.legend(['spot price','futures price'])
plt.savefig('futures results/924/ada/basic_1h.png', dpi=None, facecolor='w', edgecolor='w',
        orientation='portrait', papertype=None, format=None,
        transparent=False, bbox_inches=None, pad_inches=0.1,
        frameon=None, metadata=None)
df = pd.DataFrame(list(zip(spot, futures)),
               columns =['spot', 'futures'])
df.to_csv('futures results/924/ada/ada.csv')
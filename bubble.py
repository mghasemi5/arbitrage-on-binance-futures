import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os


def merge(s1, s2,mode):
    asset_list1 = os.listdir(s1)
    asset_list2 = os.listdir((s2))
    final_list1 = []
    final_list2 = []

    for i in range(len(asset_list1)):
        p1 = pd.read_csv(s1+asset_list1[i])
        p2 = pd.read_csv(s2+asset_list2[i])
        p1 = p1.to_numpy()
        p2 = p2.to_numpy()
        p1_close = []
        p2_close = []
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


        final_list1 = final_list1 + p1_close
        final_list2 = final_list2 + p2_close


    return final_list1 , final_list2

def calc_expected(a1,a2):
    expect = []
    for i in range(len(a1)):
        expect.append((a1[i]/a2[i]))

    return expect




adausdt = 'spot/adausdt/1h/'
btcusdt = 'spot/btcusdt/1h/'
adabtc = 'spot/adabtc/1h/'

adausdt_sl ,btcusdt_sl = merge(adausdt,btcusdt,'l')
print('************* 25% completed ******************')
adabtc_sl , ni = merge(adabtc,btcusdt,'l')
print('************* 50% completed ******************')
adabtc_el = calc_expected(adausdt_sl,btcusdt_sl)

adausdt_sh ,btcusdt_sh = merge(adausdt,btcusdt,'h')
print('************* 75% completed ******************')
adabtc_sh , ni = merge(adabtc,btcusdt,'h')

print('************* 100% completed ******************')
adabtc_eh = calc_expected(adausdt_sh,btcusdt_sh)


x =[]
y = []
for i in range(len(adabtc_el)):
    x.append(i)



for i in range(len(adabtc_sl)):
    z1 = (adabtc_sl[i] - adabtc_el[i]) / adabtc_el[i]
    z2 = (adabtc_sh[i] - adabtc_eh[i]) / adabtc_eh[i]
    if abs(z1) > abs(z2):
        y.append(z1)
    else:
        y.append(z2)

sum = 0
for i in y:
    sum = sum + abs(i)


print(sum/len(y))

kir = pd.DataFrame(list(zip(x, y)),
               columns =['hour', 'bubble'])
kir.to_csv('bubble.csv')
plt.plot(x,y)
plt.title('ADABTC highest price bubble in 1h timescale')
plt.xlabel('hours')
plt.ylabel('price difference')
plt.savefig('adabtc.png', dpi=None, facecolor='w', edgecolor='w',
        orientation='portrait', papertype=None, format=None,
        transparent=False, bbox_inches=None, pad_inches=0.1,
        frameon=None, metadata=None)
plt.show()

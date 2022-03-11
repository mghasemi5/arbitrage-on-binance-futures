import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def merge(s1, s2):
    p1 = pd.read_csv(s1)
    p2 = pd.read_csv(s2)
    p1 = p1.to_numpy()
    p2 = p2.to_numpy()
    p1_close = []
    p2_close = []

    for i in range(p2.shape[0]):
        for j in range(p1.shape[0]):

            if p2[i][0] == p1[j][0]:
                p1_close.append(p1[j][4])
                p2_close.append(p2[i][4])

    return p1_close, p2_close


'''
btc_920 , paxg_920 = merge('btcusdt/15m/BTCUSDT-15m-2020-09.csv','paxgusdt/15m/PAXGUSDT-15m-2020-09.csv')
btc_1020 , paxg_1020 = merge('btcusdt/15m/BTCUSDT-15m-2020-10.csv','paxgusdt/15m/PAXGUSDT-15m-2020-10.csv')
btc_1120 , paxg_1120 = merge('btcusdt/15m/BTCUSDT-15m-2020-11.csv','paxgusdt/15m/PAXGUSDT-15m-2020-11.csv')
btc_1220 , paxg_1220 = merge('btcusdt/15m/BTCUSDT-15m-2020-12.csv','paxgusdt/15m/PAXGUSDT-15m-2020-12.csv')
btc_121 , paxg_121 = merge('btcusdt/15m/BTCUSDT-15m-2021-01.csv','paxgusdt/15m/PAXGUSDT-15m-2021-01.csv')
btc_221 , paxg_221 = merge('btcusdt/15m/BTCUSDT-15m-2021-02.csv','paxgusdt/15m/PAXGUSDT-15m-2021-02.csv')
btc_321 , paxg_321 = merge('btcusdt/15m/BTCUSDT-15m-2021-03.csv','paxgusdt/15m/PAXGUSDT-15m-2021-03.csv')
btc_421 , paxg_421 = merge('btcusdt/15m/BTCUSDT-15m-2021-04.csv','paxgusdt/15m/PAXGUSDT-15m-2021-04.csv')
btc_521 , paxg_521 = merge('btcusdt/15m/BTCUSDT-15m-2021-05.csv','paxgusdt/15m/PAXGUSDT-15m-2021-05.csv')
btc_621 , paxg_621 = merge('btcusdt/15m/BTCUSDT-15m-2021-06.csv','paxgusdt/15m/PAXGUSDT-15m-2021-06.csv')
'''

'''
btc_920 , paxg_920 = merge('btcusdt/4h/BTCUSDT-4h-2020-09.csv','paxgusdt/4h/PAXGUSDT-4h-2020-09.csv')
btc_1020 , paxg_1020 = merge('btcusdt/4h/BTCUSDT-4h-2020-10.csv','paxgusdt/4h/PAXGUSDT-4h-2020-10.csv')
btc_1120 , paxg_1120 = merge('btcusdt/4h/BTCUSDT-4h-2020-11.csv','paxgusdt/4h/PAXGUSDT-4h-2020-11.csv')
btc_1220 , paxg_1220 = merge('btcusdt/4h/BTCUSDT-4h-2020-12.csv','paxgusdt/4h/PAXGUSDT-4h-2020-12.csv')
btc_121 , paxg_121 = merge('btcusdt/4h/BTCUSDT-4h-2021-01.csv','paxgusdt/4h/PAXGUSDT-4h-2021-01.csv')
btc_221 , paxg_221 = merge('btcusdt/4h/BTCUSDT-4h-2021-02.csv','paxgusdt/4h/PAXGUSDT-4h-2021-02.csv')
btc_321 , paxg_321 = merge('btcusdt/4h/BTCUSDT-4h-2021-03.csv','paxgusdt/4h/PAXGUSDT-4h-2021-03.csv')
btc_421 , paxg_421 = merge('btcusdt/4h/BTCUSDT-4h-2021-04.csv','paxgusdt/4h/PAXGUSDT-4h-2021-04.csv')
btc_521 , paxg_521 = merge('btcusdt/4h/BTCUSDT-4h-2021-05.csv','paxgusdt/4h/PAXGUSDT-4h-2021-05.csv')
btc_621 , paxg_621 = merge('btcusdt/4h/BTCUSDT-4h-2021-06.csv','paxgusdt/4h/PAXGUSDT-4h-2021-06.csv')
'''

'''
btc_920 , paxg_920 = merge('btcusdt/d1/BTCUSDT-1d-2020-09.csv','paxgusdt/d1/PAXGUSDT-1d-2020-09.csv')
btc_1020 , paxg_1020 = merge('btcusdt/d1/BTCUSDT-1d-2020-10.csv','paxgusdt/d1/PAXGUSDT-1d-2020-10.csv')
btc_1120 , paxg_1120 = merge('btcusdt/d1/BTCUSDT-1d-2020-11.csv','paxgusdt/d1/PAXGUSDT-1d-2020-11.csv')
btc_1220 , paxg_1220 = merge('btcusdt/d1/BTCUSDT-1d-2020-12.csv','paxgusdt/d1/PAXGUSDT-1d-2020-12.csv')
btc_121 , paxg_121 = merge('btcusdt/d1/BTCUSDT-1d-2021-01.csv','paxgusdt/d1/PAXGUSDT-1d-2021-01.csv')
btc_221 , paxg_221 = merge('btcusdt/d1/BTCUSDT-1d-2021-02.csv','paxgusdt/d1/PAXGUSDT-1d-2021-02.csv')
btc_321 , paxg_321 = merge('btcusdt/d1/BTCUSDT-1d-2021-03.csv','paxgusdt/d1/PAXGUSDT-1d-2021-03.csv')
btc_421 , paxg_421 = merge('btcusdt/d1/BTCUSDT-1d-2021-04.csv','paxgusdt/d1/PAXGUSDT-1d-2021-04.csv')
btc_521 , paxg_521 = merge('btcusdt/d1/BTCUSDT-1d-2021-05.csv','paxgusdt/d1/PAXGUSDT-1d-2021-05.csv')
btc_621 , paxg_621 = merge('btcusdt/d1/BTCUSDT-1d-2021-06.csv','paxgusdt/d1/PAXGUSDT-1d-2021-06.csv')

'''
'''
btc_920, paxg_920 = merge('btcusdt/1h/BTCUSDT-1h-2020-09.csv', 'paxgusdt/1h/PAXGUSDT-1h-2020-09.csv')
btc_1020, paxg_1020 = merge('btcusdt/1h/BTCUSDT-1h-2020-10.csv', 'paxgusdt/1h/PAXGUSDT-1h-2020-10.csv')
btc_1120, paxg_1120 = merge('btcusdt/1h/BTCUSDT-1h-2020-11.csv', 'paxgusdt/1h/PAXGUSDT-1h-2020-11.csv')
btc_1220, paxg_1220 = merge('btcusdt/1h/BTCUSDT-1h-2020-12.csv', 'paxgusdt/1h/PAXGUSDT-1h-2020-12.csv')
btc_121, paxg_121 = merge('btcusdt/1h/BTCUSDT-1h-2021-01.csv', 'paxgusdt/1h/PAXGUSDT-1h-2021-01.csv')
btc_221, paxg_221 = merge('btcusdt/1h/BTCUSDT-1h-2021-02.csv', 'paxgusdt/1h/PAXGUSDT-1h-2021-02.csv')
btc_321, paxg_321 = merge('btcusdt/1h/BTCUSDT-1h-2021-03.csv', 'paxgusdt/1h/PAXGUSDT-1h-2021-03.csv')
btc_421, paxg_421 = merge('btcusdt/1h/BTCUSDT-1h-2021-04.csv', 'paxgusdt/1h/PAXGUSDT-1h-2021-04.csv')
btc_521, paxg_521 = merge('btcusdt/1h/BTCUSDT-1h-2021-05.csv', 'paxgusdt/1h/PAXGUSDT-1h-2021-05.csv')
btc_621, paxg_621 = merge('btcusdt/1h/BTCUSDT-1h-2021-06.csv', 'paxgusdt/1h/PAXGUSDT-1h-2021-06.csv')
'''

'''
btc_close = btc_920 + btc_1020 + btc_1120 + btc_1220 + btc_121 + btc_221 + btc_321 + btc_421 + btc_521 + btc_621
paxg_close = paxg_920 + paxg_1020 + paxg_1120 + paxg_1220 + paxg_121 + paxg_221 + paxg_321 + paxg_421 + paxg_521 + paxg_621
'''


btc_close_p = [0]
paxg_close_p = [0]
for i in range(len(btc_close) - 1):
    btc_close_p.append(((btc_close[i + 1] - btc_close[i]) / btc_close[i]))
    paxg_close_p.append(((paxg_close[i + 1] - paxg_close[i]) / paxg_close[i]))

x = []

for i in range(len(btc_close_p)):
    x.append(i)
'''
a1 = np.linalg.norm(btc_close_p)
a2 = np.linalg.norm(paxg_close_p)
btc_close_p = btc_close_p/a1
paxg_close_p = paxg_close_p/a2
'''

n = np.corrcoef(btc_close_p, paxg_close_p)
print(n)
k1 = 0
k2 = 0

for i in range(len(btc_close_p)):
    if (btc_close_p[i] >= 0) & (paxg_close_p[i] >= 0):
        k1 = k1 + 1

    if (btc_close_p[i] < 0) & (paxg_close_p[i] < 0):
        k2 = k2 + 1

print(k1, '   ', k2, '    ', (k1 + k2) / len(btc_close_p))

plt.plot(x, btc_close_p, x, paxg_close_p)
plt.show()

# np.savetxt('btcusdt_1h.csv',btc_close_p)

# np.savetxt('paxgusdt_1h',paxg_close_p)

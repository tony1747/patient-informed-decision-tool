import numpy as np
"""
generates dosing schedule from a set of drug values
d1: Taxo+Cyto
d2: trast
d3: Xeloda
d4: Fulv+Ribo
"""
def TreeToSchedule(d1, d2, d3, d4, startStrike, startCycle):
    days=0
    out=[]
    #1st strike
    if startStrike<=1:
        for i in range(0,4):
            if startStrike!=1 or (startStrike == 1 and i >= startCycle - 1):
                out.append([1,d1,days,days+21])
            days+=21
    #2nd strike
    if startStrike<=2:
        for i in range(0,4):
            if startStrike!=2 or (startStrike <= 2 and i >= startCycle - 1):
                out.append([2,d2,days,days+21])
            days+=21
    #3rd strike
    if startStrike<=3:
        for i in range(0,5):
            if startStrike!=3 or (startStrike <= 3 and i >= startCycle - 1):
                out.append([3,d3,days,days+21])
            days+=21
    #4th strike
    if startStrike<=4:
        for i in range(0,5):
            if startStrike!=4 or (startStrike <= 4 and i >= startCycle - 1):
                out.append([4,d4,days,days+28])
            days+=28
    return np.array(out,dtype=float)

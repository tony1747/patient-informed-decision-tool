import numpy as np
from numba import njit
from scipy.integrate import solve_ivp
from model import TreeToSchedule
import matplotlib.pyplot as plt
sched1=TreeToSchedule(0.5,0.25,0.75,0.5,1,1)
DRUG=0;DOSE=1;START=2;END=3

#find sched tox for given day
@njit
def FindSchedI(t,i,sched):
    while i<=len(sched):
        if i==len(sched): return 0
        if sched[i,END]>=t:break
        i+=1
    return i

@njit
def FindSchedTox(t,i,sched,patientToxs):
    if sched[i,START]>t:return 0
    if sched[i,END]<t:return 0
    return sched[i,DOSE]*patientToxs[DRUG]

@njit
def RunToxDifferenceEquation(tox0, tStart,tEnd, sched, sen1, sen2, sen3, sen4, decay,breakThresh):
    ys=np.zeros((tEnd-tStart)+1+len(sched)*14)
    breaks=np.zeros(len(sched))
    iSched=0
    y=0
    timedisp=0
    patientToxs=np.array((sen1,sen2,sen3,sen4))
    for t in range(tStart,tEnd+1):
        iSched=FindSchedI(t,iSched,sched)
        tox=FindSchedTox(t,iSched,sched,patientToxs)
        y+=tox
        y*=decay
        ys[t+timedisp]=y+tox0
        #incorporate breaks
        if t == sched[iSched, END]:
            for i in range(2):
                if y+tox0 > breakThresh:
                    breaks[iSched]+=1
                    for i in range(7):
                        timedisp += 1
                        y *= decay
                        ys[t + timedisp] = y+tox0
    return ys,breaks

#@njit
def GenNewSched(sched,breaks):
    out=np.zeros((len(sched),4))
    timeDisp=0
    for i in range(len(sched)):
        out[i,DRUG]=sched[i,DRUG]
        out[i,DOSE]=sched[i,DOSE]
        out[i,START]=sched[i,START]+timeDisp
        out[i,END]=sched[i,END]+timeDisp
        timeDisp+=breaks[i]*7
    return out

out=RunToxDifferenceEquation(0,0,400,sched1,0.5,0.25,0.75,0.25,0.8,0.9)
newSched=GenNewSched(sched1,out[1])
print("here")
plt.plot(out[0])
plt.show()
#def RunToxODE(tox0, tStart,tEnd, sched, sen1, sen2, sen3, sen4, decay):
#    iArr=np.zeros((1),dtype=int)
#    patientToxs=np.array((sen1,sen2,sen3,sen4))
#    def ToxODE(t,y):
#        addedTox=FindSchedTox(t,iArr,sched,patientToxs)
#        y+=addedTox
#        y*=decay
#        return y
#    return solve_ivp(ToxODE,y0=np.array([tox0]),t_span=(tStart,tEnd),method='LSODA',t_eval=(np.arange(tStart,tEnd+1,1)))


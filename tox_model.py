import numpy as np
from numba import njit
from scipy.integrate import solve_ivp
from scheduler import plan_to_schedule
import matplotlib.pyplot as plt
sched1=plan_to_schedule(0.5,0.25,0.75,0.5,1,1)
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
def FindSchedTox(t,i,sched,patientToxs,doseReduction):
    if sched[i,START]>t:return 0
    if sched[i,END]<t:return 0
    return (sched[i,DOSE]-doseReduction)*patientToxs[DRUG]

#@njit
#lognormal(0.5,1.4)
def ToxReductionScalar(tox):
    minVal=0.3
    maxVal=1
    minScalar=0.0
    maxScalar=0.1
    if tox<minVal: return minScalar
    if tox>=minVal and tox<maxVal: return (minScalar*(maxVal-tox)+maxScalar*(tox-minVal))/(maxVal-minVal)
    else:return maxScalar
#    result=-((0.2854959 * np.exp(-0.255102 * (np.log(tox) + 0.5) ** 2)) / tox)*scalar
#    if tox+result<0:return 0
#    return tox+result

#@njit
def RunToxDifferenceEquation(tox0, tStart, tEnd, sched, sens, decay,breakThresh,reduceThresh):
    idrug=0
    doseReduction=0
    breaking=False
    ys=np.zeros((tEnd-tStart)+1+len(sched)*14)
    breaks=np.zeros(len(sched))
    reduces=np.zeros(len(sched))
    iSched=0
    y=0
    timedisp=0
    patientToxs=np.array(sens)
    for t in range(tStart,tEnd+1):
        if breaking:
            break
        iSched=FindSchedI(t,iSched,sched)
        if(idrug!=sched[iSched,DRUG]):
            idrug=sched[iSched,DRUG]
            doseReduction=0
        tox=FindSchedTox(t,iSched,sched,patientToxs,doseReduction)
        y+=tox
        y*=decay+(1-decay)*(y*0.85)
        ys[t+timedisp]=y+tox0
        #incorporate tox reduction
        if t == sched[iSched, END]:
            reduces[iSched]=doseReduction
            for i in range(2):
                if y+tox0 > breakThresh:
                    breaks[iSched]+=1
                    if doseReduction<0.2: doseReduction += 0.1
                    for i in range(7):
                        timedisp += 1
                        y*=decay+(1-decay)*(y*0.85)
                        ys[t + timedisp] = y+tox0
                if y+tox0 > reduceThresh:
                    if doseReduction<0.2: doseReduction += 0.1
            if y + tox0 > breakThresh: breaking = True
    if breaking: return None,None
    return ys,breaks

@njit
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
from tox_model import *
from scheduler import *
import matplotlib.pyplot as plt
from growth_model import *
paramSets=[]

class ParamSet:
    def __init__(self,d1,d2,d3,d4):
        self.d1=d1
        self.d2=d2
        self.d3=d3
        self.d4=d4
        self.sched=plan_to_schedule(d1,d2,d3,d4,1,1)
        self.breakSched=None
        self.breaks=None
        self.toxs=None

#for d1 in range(0,6):
#    for d2 in range(0,6):
#        for d3 in range(0,6):
#            for d4 in range(0,6):
#                paramSets.append(ParamSet(d1/10+0.5,d2/10+0.5,d3/10+0.5,d4/10+0.5))

paramSets.append(ParamSet(1,1,1,1))
for params in paramSets:
    toxs,breaks=RunToxDifferenceEquation(0,0,365,params.sched,[0.5,0.5,0.5,0.5],0.95,10.0)
    params.breakSched=breaks
    params.toxs=toxs
    newSched=GenNewSched(params.sched,breaks)
    sol=tumour_growth(1e11,365*2,newSched,300)
    plt.plot(sol.t,np.log10(sol.y.flatten()))
    #    plt.plot(toxs)

    plt.show()

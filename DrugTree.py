from ToxModel import *
from model import *
paramSets=[]

class ParamSet:
    def __init__(self,d1,d2,d3,d4):
        self.d1=d1
        self.d2=d2
        self.d3=d3
        self.d4=d4
        self.sched=TreeToSchedule(d1,d2,d3,d4)

for d1 in range(0,6):
    for d2 in range(0,6):
        for d3 in range(0,6):
            for d4 in range(0,6):
                paramSets.append(ParamSet(d1/12+0.5,d2/12+0.5,d3/12+0.5,d4/12+0.5))

for params in paramSets:
    RunToxDifferenceEquation(0,0,365,params.sched,)
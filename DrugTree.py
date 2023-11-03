from tox_model import *
from scheduler import *
import matplotlib.pyplot as plt
from growth_model import *
from multiprocessing import Pool
import pickle


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


#SCALING_FACTOR=0.025#:1.0,0.8,0.6,0.9
SCALING_FACTOR=0.037#:0.6,0.5,0.5,0.5

#SCALING_FACTOR=0.03:0.9,0.6,0.6,0.7
#SCALING_FACTOR=0.04
DECAY=0.96

def RunParams(params):
    toxs,breaks=RunToxDifferenceEquation(0,0,365,params.sched,[0.7*SCALING_FACTOR,0.6*SCALING_FACTOR,0.5*SCALING_FACTOR,0.4*SCALING_FACTOR],DECAY,1.0,0.8)
    if toxs is None:
        return [params.d1,params.d2,params.d3,params.d4,-1]
    params.breakSched=breaks
    params.toxs=toxs
    newSched=GenNewSched(params.sched,breaks)
    sol=tumour_growth(1e11,365*2,newSched,300000,(0.1,0.075,0.05,0.025))
    return [params.d1,params.d2,params.d3,params.d4,np.min(sol.y.T[:, 0]),np.sum(toxs)]
sweep=True
if sweep:
    if __name__=='__main__':
        paramSets = []
        for d1 in range(0, 6):
            for d2 in range(0, 6):
                for d3 in range(0, 6):
                    for d4 in range(0, 6):
                        paramSets.append(ParamSet(d1 / 10 + 0.5, d2 / 10 + 0.5, d3 / 10 + 0.5, d4 / 10 + 0.5))
        with Pool(16) as pool:
            out=pool.map(RunParams,paramSets)
        pickle.dump(out, open("outRes.p", "wb"))

else:
    paramSets = []
    paramSets.append(ParamSet(1.0,0.8,0.6,0.9))
#    paramSets.append(ParamSet(0.7,0.5,0.5,0.6))
    #TEST_FACTOR=0.8
    #paramSets.append(ParamSet(TEST_FACTOR, TEST_FACTOR, TEST_FACTOR, TEST_FACTOR))
    for params in paramSets:
        toxs,breaks=RunToxDifferenceEquation(0.0,0,365,params.sched,[0.7*SCALING_FACTOR,0.6*SCALING_FACTOR,0.5*SCALING_FACTOR,0.4*SCALING_FACTOR],DECAY,1.0,0.8)
        params.breakSched=breaks
        params.toxs=toxs
        newSched=GenNewSched(params.sched,breaks)
        sol=tumour_growth(1e11,365*2,newSched,300000,(0.1,0.075,0.05,0.025))
        plt.plot(sol.t,sol.y.flatten())
        plt.title("toxicity-resistant patient")
        plt.yscale("log")
        plt.ylim((1E2,None))
        plt.ylabel("cells (log)")
        plt.xlabel("days")
        plt.show()
        plt.clf()
        plt.title("toxicity-resistant patient")
        plt.ylabel("toxicity score")
        plt.ylim((-0.1,1.1))
        plt.xlabel("days")
        plt.plot(toxs)
        plt.show()

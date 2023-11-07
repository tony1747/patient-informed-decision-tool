import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json
import scoring as sc
from multiprocessing import Pool
import pickle

# read json file patient_config.json

def PoolFun(plan):
    return sc.score(plan[1], plan[0])


if __name__=='__main__':
    with open('patient_config.json') as f:
        patient_config = json.load(f)
    #doses = [1, 0.5]
    #doses = [1.0,0.9,0.8,0.7,0.6,0.5]
    doses = [0.5]
    plans = [((t1, t2, t3, t4),patient_config) for t1 in doses for t2 in doses for t3 in doses for t4 in doses]

    start_time = time.time()
    print(f"Testing {len(plans)} treatment schedules.")
    out=sc.score(config=patient_config,plan=plans[0])
#    with Pool(16) as pool:
#        out=pool.map(PoolFun,plans)
#        pickle.dump(out, open("outRes.p", "wb"))
#        plt.plot()
#sols = [sc.score(patient_config, plan) for plan in plans]

    plt.plot(out)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Elapsed Time: {elapsed_time:.4f} seconds")


import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json
import scoring as sc
from multiprocessing.pool import ThreadPool as Pool

# read json file patient_config.json
with open('patient_config.json') as f:
    patient_config = json.load(f)
doses = [1, 0.9,0.8,0.7,0.6, 0.5]
plans = [(t1, t2, t3, t4) for t1 in doses for t2 in doses for t3 in doses for t4 in doses]

start_time = time.time()
print(f"Testing {len(plans)} treatment schedules.")

sols = [sc.score(patient_config, plan) for plan in plans]

end_time = time.time()
elapsed_time = end_time - start_time
print(f"Elapsed Time: {elapsed_time:.4f} seconds")
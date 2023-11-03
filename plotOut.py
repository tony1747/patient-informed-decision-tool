import pickle
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

out=pickle.load(open("outRes.p", "rb"))
data=pd.DataFrame(out,columns=["d1","d2","d3","d4","burden","overall toxicity"])
data=data[data.burden>=0]
data=data.sort_values(by="burden")
sns.scatterplot(data=data,x="overall toxicity",y="burden")
plt.ylim((1E2,1E7))
plt.xlim((50,375))
plt.yscale("log")
plt.ylabel("cells (log)")
plt.show()
print("here")
def ToxReductionScalar(tox):
    minVal = 0.3
    maxVal = 1
    minScalar = 0.1
    if tox < minVal: return minScalar
    if tox >= minVal and tox < maxVal: return (minScalar * (maxVal - tox) + 1 * (tox - minVal)) / (maxVal - minVal)
    else:
        return 1


#plt.plot([ToxReductionScalar(x) for x in np.arange(0,4,0.001)])
#plt.show()

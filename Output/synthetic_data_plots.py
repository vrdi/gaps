from collections import Counter
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pickle


uPA = "../Synthetic_Data/uPA.txt"
gPA = "../Synthetic_Data/gPA.txt"
uVA = "../Synthetic_Data/uVA.txt"
gVA = "../Synthetic_Data/gVA.txt"


# SET PARAMS
data_model = "gVA_choosing"
df = pd.read_csv(gVA, header=None)
df = df.iloc[:100000]


# to sort data from greedy data_model, uncomment the following
# arr = df.values
# arr.sort(axis=1)
# df = pd.DataFrame(arr)


c='k'
plt.figure()
plt.boxplot(
           np.array(df),
           whis=[1, 99],
           showfliers=False,
           patch_artist=True,
           boxprops=dict(facecolor="None", color=c),
           capprops=dict(color=c),
           whiskerprops=dict(color=c),
           flierprops=dict(color=c, markeredgecolor=c),
           medianprops=dict(color=c),
)

plt.plot([],[],color='k',label="{0} Data".format(data_model))

plt.xlabel("Unsorted districts")
#plt.xlabel("Sorted districts")

plt.savefig("{0}.png".format(data_model))
plt.show()
plt.close()

from collections import Counter
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pickle

uPA = "../Synthetic_Data/uPA.txt"
gPA = "../Synthetic_Data/gPA.txt"
uVA = "../Synthetic_Data/uVA.txt"
gVA = "../Synthetic_Data/gVA.txt"

# VA has 11 Congressional districts, PA has 18

# set model to va or pa with uniform or greedy model
data_model = "gVA_choosing"
# set correct state below
df = pd.read_csv(gVA, header=None)
df = df.iloc[:100000]

# to sort data from greedy data_model
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

plt.ylabel("BVAP %")
plt.savefig("{0}.png".format(data_model))
plt.show()
plt.close()

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("../VA_Viz/Full_State/Senate/DOJBVAP_2000.csv", header=None)
for x in range(4000,100001,2000):
    df = pd.concat([df, pd.read_csv("../VA_Viz/Full_State/Senate/DOJBVAP_{0}.csv".format(x), header=None)], ignore_index=True)

# box plot for districts sorted by BVAP

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

plt.plot([],[],color='k',label="VA Recom Ensemble")
plt.xlabel("Sorted districts")
plt.ylabel("DOJ BVAP")
plt.savefig("va_bvap_senate.png")
plt.show()


# histogram for largest gap per plan
gaps = []
left_district = []
lower_bound = []
upper_bound = []
for i in range(len(df.index)):
    x = 0
    gap = 0
    lower = 0
    upper = 0
    for j in range(df.shape[1] - 1):
        x = float(df.iloc[[i]][j+1] - df.iloc[[i]][j])
        if (x > gap):
            left = j
            gap = x
            lower = float(df.iloc[[i]][j])
            upper = float(df.iloc[[i]][j+1])
    gaps.append(gap)
    left_district.append(left)
    lower_bound.append(lower)
    upper_bound.append(upper)

plt.hist(gaps, bins=100)
plt.ylabel("Frequency")
plt.xlabel("Largest gap in BVAP")
plt.savefig("va_bvap_gap_senate.png")
plt.show()

plt.scatter(gaps, left_district)
plt.ylabel("Left district")
plt.xlabel("Size of BVAP gap")
plt.savefig("va_bvap_size_district_senate.png")
plt.show()

plt.scatter(lower_bound, upper_bound)
x = np.linspace(min(lower_bound) - .1, max(upper_bound) + .1, 100)
plt.plot(x, x, '--r')
plt.xlim([min(lower_bound) - .1, max(upper_bound) + .1])
plt.ylim([min(lower_bound) - .1, max(upper_bound) + .1])
plt.xlabel("Lower BVAP value")
plt.ylabel("Upper BVAP value")
plt.savefig("va_bvap_gap_values_senate.png")
plt.show()

plt.hist(left_district, bins=[x - .5 for  x in range(1,41)])
plt.xlabel("Left district")
plt.ylabel("Frequency")
plt.savefig("va_bvap_gap_district_senate.png")
plt.show()

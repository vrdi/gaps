from collections import Counter
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pickle


Virginia_file = "../VA_Viz/Full_State/Congressional/DOJBVAP_{0}.csv"
Pennsylvania_file = "../PA_Viz/Metrics/BPOP_{0}.csv"

va_gap_file = "va_gap_file"
va_left_district_file = "va_left_district_file"
va_true_gap_file = "va_true_gaps"
pa_gap_file = "pa_gap_file"
pa_left_district_file = "pa_left_district_file"
pa_true_gap_file = "pa_true_gaps"


## SET PARAMS BELOW
## still need to change plot axes and plot names appropriately
state_file = Pennsylvania_file
state_gap_file = pa_gap_file
state_left_district_file = pa_left_district_file
state_true_gap_file = pa_true_gap_file
state = "pa"
# Virginia has 11 Congressional districts, Pennsylvania 18
NUM_DISTRICTS = 18

df = pd.read_csv(state_file.format(2000), header=None)
for x in range(4000,100001,2000):
    df = pd.concat([df, pd.read_csv(state_file.format(x), header=None)], ignore_index=True)


# c='k'
# plt.figure()
# plt.boxplot(
#            np.array(df),
#            whis=[1, 99],
#            showfliers=False,
#            patch_artist=True,
#            boxprops=dict(facecolor="None", color=c),
#            capprops=dict(color=c),
#            whiskerprops=dict(color=c),
#            flierprops=dict(color=c, markeredgecolor=c),
#            medianprops=dict(color=c),
# )
#
# plt.plot([],[],color='k',label="PA Recom Ensemble")
# plt.xlabel("Sorted districts")
# plt.ylabel("BVAP %")
# plt.savefig("pa_bpop.png")
# plt.show()
# plt.close()
#
gap_outfile = open(state_gap_file, 'wb')
left_district_outfile = open(state_left_district_file, 'wb')
true_gap_outfile = open(state_true_gap_file, 'wb')

# histogram for largest gap per plan
gaps = []
left_district = []
lower_bound = []
upper_bound = []
true_gaps = []
d = {i:[] for i in range(1, NUM_DISTRICTS)}
#for i in range(len(df.index)):
for i in range(100):
    x = 0
    gap = 0
    lower = 0
    upper = 0
    for j in range(1, df.shape[1]): # for each gap
        if (i == 0):
            true_gaps.append(float(df.iloc[[i]][j] - df.iloc[[i]][j-1]))
        x = float(df.iloc[[i]][j] - df.iloc[[i]][j-1])
        if (x > gap):
            left = j
            gap = x
            lower = float(df.iloc[[i]][j-1])
            upper = float(df.iloc[[i]][j])
    gaps.append(gap)
    left_district.append(left)
    lower_bound.append(lower)
    upper_bound.append(upper)

for i in range(len(gaps)):
    d[left_district[i]].append(gaps[i])

pickle.dump(gaps, gap_outfile)
gap_outfile.close()
pickle.dump(left_district, left_district_outfile)
left_district_outfile.close()
pickle.dump(true_gaps, true_gap_outfile)
true_gap_outfile.close()


# SET NAMES OF AXES AND PLOT NAMES BELOW

plt.hist(gaps, bins=100)
plt.ylabel("Frequency")
plt.xlabel("Largest gap in BPOP %")
plt.axvline(x=max(true_gaps), color="red", linewidth=1)
#plt.savefig("pa_bpop_gap.png")
plt.show()
plt.close()

plt.scatter(gaps, left_district)
plt.ylabel("Left district")
plt.xlabel("Size of BVAP % gap")
#plt.savefig("pa_bpop_size_district.png")
plt.show()
plt.close()

plt.scatter(lower_bound, upper_bound)
x = np.linspace(min(lower_bound) - .1, max(upper_bound) + .1, 100)
plt.plot(x, x, '--r')
plt.xlim([min(lower_bound) - .1, max(upper_bound) + .1])
plt.ylim([min(lower_bound) - .1, max(upper_bound) + .1])
plt.xlabel("Lower BVAP % value")
plt.ylabel("Upper BVAP % value")
#plt.savefig("pa_bpop_gap_values.png")
plt.show()
plt.close()

plt.hist(left_district, bins=[x for x in range(1, NUM_DISTRICTS+1)])
plt.xlabel("Left district")
plt.ylabel("Frequency")
plt.axvline(x=np.argmax(true_gaps)+1.5, color="red", linewidth=2)
#plt.savefig("pa_bpop_gap_district.png")
plt.show()
plt.close()

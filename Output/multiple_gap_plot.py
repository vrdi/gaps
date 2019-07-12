import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pickle


## SET PARAMS
# Virginia has 11 Congressional districts, Pennsylvania 18
state = "pa"
NUM_DISTRICTS = 18


gaps = pickle.load( open( "{0}_gap_file".format(state), "rb" ) )
left_district = pickle.load( open( "{0}_left_district_file".format(state), "rb" ) )

d = {i:[] for i in range(1, NUM_DISTRICTS)}
for i in range(len(gaps)):
    d[left_district[i]].append(gaps[i])

true_gaps = pickle.load( open( "{0}_true_gaps".format(state), "rb") )

# for VA
# for i in range(1, NUM_DISTRICTS):
#     plt.subplot(NUM_DISTRICTS-1, 1, i, ylim=(0, 1000), xlim=(0, .2))
#     plt.subplots_adjust(bottom=.07, top=.97, wspace=None, hspace=2)
#     plt.hist(d[i], bins=100)
#     plt.axvline(x=true_gaps[i-1], color="red", linewidth=4)
#     plt.xlabel('Gap ' + str(i))

# plt.savefig("{0}_bvap_largest_gaps_by_district.png".format(state))
# plt.show()


# for PA
non_z_gaps = []
for i in range(1, NUM_DISTRICTS):
    if (len(d[i]) > 0):
        non_z_gaps.append(i)

for i in range(len(non_z_gaps)):
    plt.subplot(len(non_z_gaps), 1, i+1, ylim=(0, 1000), xlim=(0, .4))
    plt.subplots_adjust(wspace=None, hspace=2)
    plt.hist(d[non_z_gaps[i]], bins=100)
    plt.axvline(x=true_gaps[i-1], color="red", linewidth=4)
    plt.xlabel('Gap ' + str(non_z_gaps[i]))

plt.savefig("{0}_bpop_largest_gaps_by_district.png".format(state))
plt.show()

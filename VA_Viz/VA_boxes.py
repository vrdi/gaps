import geopandas as gpd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import json
import os
import pandas as pd



num_elections = 7
election_names= ["DLSBVAP","DOJBVAP","SEN18","GOV18","LTG17","ATG17","PRS16"]
election_columns=[["DLS_BVAP","DLS_NONB"],["DOJ_BVAP","DOJ_NONB"],["G18DSEN","G18RSEN"],
["G17DGOV","G17RGOV"],["G17DLTG","G17RLTG"],["G17DATG","G17RATG"],["G16DPRS","G16RPRS"]]

plan_name = "VA_MUNI_ALL_SEN2_RMH3_merge"


#"VA_MUNI_ALL_CON_merge"
#"VA_MUNI_ALL_SEN2_merge"
#"VA_MUNI_nova_CON_merge"
#"VA_MUNI_nova_SEN2_merge"
#"VA_MUNI_nonova_CON_merge"
#"VA_MUNI_nonovarich_SEN2_merge"
#"VA_MUNI_ALL_SEN2_RMH_merge"
#"VA_MUNI_nonovarich_SEN2_RMH_merge"





newdir = "./VAPlots/Boxes/"+plan_name+"/"

num_districts = 40


datadir = "./" + plan_name + "/" 

os.makedirs(os.path.dirname(newdir + "init.txt"), exist_ok=True)
with open(newdir + "init.txt", "w") as f:
    f.write("Created Folder")

max_steps = 25000
step_size = 1000#

ts = [x*step_size for x in range(1,int(max_steps/step_size)+1)]

a=[]
for elect in range(7):
    a=[]
    for t in ts:
        tempvotes=np.loadtxt(datadir+election_names[elect]+"_"+str(t)+".csv", delimiter=',')
        for s in range(step_size):
            a.append(tempvotes[s,:])
            
    a=np.array(a)        
    medianprops = dict( color='black')

    fig1 = plt.figure()
    ax1 = fig1.add_subplot(111)
    #ax1.add_patch(patches.Rectangle((0, .37), 35, .18,color='honeydew'))
    #plt.plot([0,34], [.55, .55], 'lightgreen')
    #plt.plot([0,34], [.37, .37], 'lightgreen')

    plt.boxplot(a,whis=[1,99],showfliers=False,medianprops=medianprops)
    plt.plot([],[],color='k',label="ReCom Ensemble")
    #fig, ax = plt.subplots()
    #draw_plot(a, 1, "black", "white")
    #plt.xticks(range(1,num_districts+1))
    #plt.plot(range(1,num_districts+1),a[0,:],'o',color='r',label='Initial Plan', markersize=3)
    #plt.plot([1,num_districts+1],[np.mean(a[0,:]),np.mean(a[0,:])],color='blue',label='Initial Mean')
    #plt.plot([1,num_districts+1],[np.median(a[0,:]),np.median(a[0,:])],color='yellow',label='Initial Median')
    plt.plot([1,num_districts+1],[.5,.5],color='green',label='50%')
        
    plt.ylabel("Dem %")
    plt.xlabel("Indexed Districts")
    plt.legend()
    plt.savefig(newdir+election_names[elect]+"_box.png")
    fig = plt.gcf()
    fig.set_size_inches((12,6), forward=False)
    fig.savefig(newdir+election_names[elect]+"_box2.png", dpi=600)


    plt.close()

dsfaajdbhasdkfj

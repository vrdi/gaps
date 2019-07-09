import geopandas as gpd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import json
import os



num_elections = 7
election_names= ["DLSBVAP","DOJBVAP","SEN18","GOV18","LTG17","ATG17","PRS16"]
election_columns=[["DLS_BVAP","DLS_NONB"],["DOJ_BVAP","DOJ_NONB"],["G18DSEN","G18RSEN"],
["G17DGOV","G17RGOV"],["G17DLTG","G17RLTG"],["G17DATG","G17RATG"],["G16DPRS","G16RPRS"]]

plan_name ="VA_MUNI_ALL_SEN2_RMH3_merge"
#"VA_MUNI_ALL_CON_merge"
#"VA_MUNI_ALL_SEN2_merge"
#"VA_MUNI_nova_CON_merge"   
#"VA_MUNI_nova_SEN2_merge"
#"VA_MUNI_nonova_CON_merge"
#"VA_MUNI_nonovarich_SEN2_merge"
#"VA_MUNI_ALL_SEN2_RMH_merge"
#"VA_MUNI_nonovarich_SEN2_RMH_merge"






newdir = "./VAPlots/Hists/"+plan_name+"/"

num_districts = 40


datadir = "./" + plan_name + "/" 

os.makedirs(os.path.dirname(newdir + "init.txt"), exist_ok=True)
with open(newdir + "init.txt", "w") as f:
    f.write("Created Folder")

max_steps = 10000 
step_size = 1000 

ts = [x*step_size for x in range(1,int(max_steps/step_size)+1)]




assignment = None
df = None

#adfgasdfad

#
cuts = np.zeros([1,max_steps])

#


for t in ts:
	temp = np.loadtxt(datadir+"cuts"+str(t)+".csv", delimiter=',')
	cuts[0,t-step_size:t]=temp
	
	
plt.plot(cuts[0,:])
#plt.plot([0,max_steps],[cuts[0,0],cuts[0,0]],color='r',label="Initial Value")
plt.plot([0,max_steps],[np.mean(cuts[0,:]),np.mean(cuts[0,:])],color='g',label="Ensemble Mean")
plt.title(plan_name + "Plan")
plt.ylabel("# Cut Edges")
plt.xlabel("Step")
#plt.plot([],[],color='green',label='Ensemble Mean')
#plt.plot([],[],color='red',label='Initial Value')
plt.legend()
plt.savefig(newdir+"cut_trace.png")
plt.close()
	
	
plt.hist(cuts[0,:],bins=1000)
plt.title(plan_name + "Plan")
#plt.axvline(x=cuts[0,0],color='r',label='Initial Value')
plt.axvline(x=np.mean(cuts[0,:]),color='g',label='Ensemble Mean')
plt.legend()
plt.ylabel("Frequency")
plt.xlabel("# Cut Edges")
plt.savefig(newdir+"cut_hist.png")
plt.close()



#sbfsdfbsd


egs = np.zeros([7,max_steps])
hmss = np.zeros([7,max_steps])
mms = np.zeros([7,max_steps])
#pops = np.zeros([7,max_steps])

for t in ts:
	temp = np.loadtxt(datadir+"egs"+str(t)+".csv", delimiter=',')
	egs[:,t-step_size:t]=temp.T
	temp = np.loadtxt(datadir+"hmss"+str(t)+".csv", delimiter=',')
	hmss[:,t-step_size:t]=temp.T
	temp = np.loadtxt(datadir+"mms"+str(t)+".csv", delimiter=',')
	mms[:,t-step_size:t]=temp.T
	#temp = np.loadtxt(datadir+"pop"+str(t)+".csv", delimiter=',')
	#pops[:,t-step_size:t]=temp    
	


for j in [0,1,2,4,5,6]:
    plt.plot(egs[j,:])
    #plt.plot([0,max_steps],[egs[j,0],egs[j,0]],color='r',label="Initial Value")
    plt.plot([0,max_steps],[np.mean(egs[j,:]),np.mean(egs[j,:])],color='g',label="Ensemble Mea")
    plt.title(plan_name + "Plan" + election_names[j])
    plt.ylabel("Efficiency Gap")
    plt.xlabel("Step")
    plt.legend()
    plt.savefig(newdir+election_names[j]+"eg_trace.png")
    plt.close()
	
	
    plt.hist(egs[j,:],bins=1000)
    plt.title(plan_name + "Plan" + election_names[j])
    #plt.axvline(x=egs[j,0],color='r',label='Initial Value')
    plt.axvline(x=np.mean(egs[j,:]),color='g',label='Ensemble Mean')
    plt.ylabel("Frequency")
    plt.xlabel("Efficiency Gap")
    #plt.plot([],[],color='green',label='Ensemble Mean')
    #plt.plot([],[],color='red',label='Initial Value')
    plt.legend()
    plt.savefig(newdir+election_names[j]+"eg_hist.png")

    plt.close()

    plt.plot(mms[j,:])
    #plt.plot([0,max_steps],[mms[j,0],mms[j,0]],color='r',label="Initial Value")
    plt.plot([0,max_steps],[np.mean(mms[j,:]),np.mean(mms[j,:])],color='g',label="Ensemble Mean")
    plt.title(plan_name + "Plan" + election_names[j])
    plt.ylabel("Mean-Median")
    plt.xlabel("Step")
    plt.legend()
    plt.savefig(newdir+election_names[j]+"mm_trace.png")
    plt.close()
	
	
    plt.hist(mms[j,:],bins=1000)
    plt.title(plan_name + "Plan" + election_names[j])
    #plt.axvline(x=mms[j,0],color='r',label='Initial Value')
    plt.axvline(x=np.mean(mms[j,:]),color='g',label='Ensemble Mean')
    plt.ylabel("Frequency")
    plt.xlabel("Mean-Median")
    #plt.plot([],[],color='green',label='Ensemble Mean')
    #plt.plot([],[],color='red',label='Initial Value')
    plt.legend()
    plt.savefig(newdir+election_names[j]+"mm_hist.png")
    plt.close()
    
    plt.plot(hmss[j,:])
    #plt.plot([0,max_steps],[hmss[j,0],hmss[j,0]],color='r',label="Initial Value")
    plt.plot([0,max_steps],[np.mean(hmss[j,:]),np.mean(hmss[j,:])],color='g',label="Ensemble Mean")
    plt.title(plan_name + "Plan" + election_names[j])
    plt.ylabel("# Seats")
    plt.xlabel("Step")
    plt.legend()
    plt.savefig(newdir+election_names[j]+"seats_trace.png")
    plt.close()
	
	
    plt.hist(hmss[j,:])
    plt.title(plan_name + "Plan" + election_names[j])
    #plt.axvline(x=hmss[j,0],color='r',label='Initial Value')
    plt.axvline(x=np.mean(hmss[j,:]),color='g',label='Ensemble Mean')
    #plt.plot([],[],color='green',label='Ensemble Mean')
    #plt.plot([],[],color='red',label='Initial Value')
    plt.ylabel("Frequency")
    plt.xlabel("# Seats")
    plt.legend()
    plt.savefig(newdir+election_names[j]+"seats_hist.png")
    plt.close()
    
    
    
    
    
with open(newdir + "Average_Values.txt", "w") as f:
    f.write("Values for Starting Plan: "+plan_name+" \n\n")
    f.write("Initial Cut: "+ str(cuts[0,0]))
    f.write("\n")
    f.write("\n")
    f.write("Average Cut: "+ str(np.mean(cuts[0,:])))
    f.write("\n")
    f.write("\n")

    for elect in range(num_elections):
        print(elect)
        

        f.write(election_names[elect] + " Initial Mean-Median: "+ str(mms[elect,0]))
        
        f.write("\n")
        f.write("\n")
        f.write(election_names[elect] + " Average Mean-Median: "+ str(np.mean(mms[elect,:])))
        
        f.write("\n")
        f.write("\n")
        f.write(election_names[elect] + " Number Mean-Median Higher: "+ str((mms[elect,:]>mms[elect,0]).sum()))
        
        f.write("\n")
        f.write("\n")
         
        f.write("\n")
        f.write("\n")
        
        
        f.write(election_names[elect] + " Initial Efficiency Gap: "+ str(egs[elect,0]))
        
        f.write("\n")
        f.write("\n")
        f.write(election_names[elect] + " Average Efficiency Gap: "+ str(np.mean(egs[elect,:])))
        
        f.write("\n")
        f.write("\n")
        f.write(election_names[elect] + " Number Efficiency Gap Higher: "+ str((egs[elect,:]>egs[elect,0]).sum()))
        
        f.write("\n")
        f.write("\n")
         
        f.write("\n")
        f.write("\n")
        
        
        f.write(election_names[elect] + " Initial Dem Seats: "+ str(hmss[elect,0]))
        
        f.write("\n")
        f.write("\n")
        f.write(election_names[elect] + " Average EDem Seats: "+ str(np.mean(hmss[elect,:])))
        
        f.write("\n")
        f.write("\n")
        f.write(election_names[elect] + " Number Dem Seats Higher: "+ str((hmss[elect,:]>hmss[elect,0]).sum()))
        
        f.write("\n")
        f.write("\n")
         
        f.write("\n")
        f.write("\n")
#
#
#a=np.zeros([max_steps,33])
#
#for t in ts:#
#	 temp=np.loadtxt(datadir4+"pop"+str(t)+".csv", delimiter=',')
#	 a[t-step_size:t,:]=temp
#
#
#mpop=np.mean(a[0,:])
#
#b=[]
#
#
#for i in range(max_steps):
#    b.append(sum([abs(mpop-x)/mpop for x in a[i,:]])/33)
#
#
#plt.hist(b,bins=100)
#plt.title("Population Deviation")
#plt.savefig(newdir+"empops.png")
#fig = plt.gcf()
#fig.set_size_inches((11,8.5), forward=False)
#fig.savefig(newdir+"empops2.png", dpi=500)
#
#plt.close()
#
#
#
#
#
#
#
#



aghafg
#
#










a=None
#a=np.zeros([max_steps,33])
#a=np.zeros([2*max_steps,33])
#b=np.zeros([2*max_steps,33])
#c=np.zeros([max_steps,33])


# for t in ts:
#     temp=np.loadtxt(datadir+"bvap"+str(t)+".csv", delimiter=',')
#     a[t - step_size:t, :] = temp
#     temp=np.loadtxt(datadir2+"bvap"+str(t)+".csv", delimiter=',')
#     #b[t-step_size:t,:]=temp
#     a[max_steps+t - step_size:max_steps+t, :] = temp

    #temp=np.loadtxt(datadir+"bpop"+str(t)+".csv", delimiter=',')
    #b[t - step_size:t, :] = temp
    #temp=np.loadtxt(datadir2+"bpop"+str(t)+".csv", delimiter=',')
    #b[t-step_size:t,:]=temp
    #b[max_steps+t - step_size:max_steps+t, :] = temp



#THIS IS FOR REDUCING THE TREE ENSEMBLE
a=[]
b=[]
c=[]
d=[]
e=[]
sizes=0
for t in ts:
    temp=np.loadtxt(datadir+"bvap"+str(t)+".csv", delimiter=',')
    for s in range(step_size):
        if temp[s,-1]<.6:
            a.append(temp[s,:])
            b.append(temp[s,:])
            sizes+=1
    temp=np.loadtxt(datadir2+"bvap"+str(t)+".csv", delimiter=',')
    for s in range(step_size):
        if temp[s,-1]<.6:
            a.append(temp[s,:])
            c.append(temp[s,:])
            sizes+=1
            
    temp=np.loadtxt(datadir3+"bvap"+str(t)+".csv", delimiter=',')
    for s in range(step_size):
        if temp[s,-1]<.6:
            a.append(temp[s,:])
            d.append(temp[s,:])
            sizes+=1
            
    temp=np.loadtxt(datadir4+"bvap"+str(t)+".csv", delimiter=',')
    for s in range(step_size):
        if temp[s,-1]<.6:
            a.append(temp[s,:])
            e.append(temp[s,:])
            sizes+=1
    
    # for mixed run with weird size enacted
    #if t % (10*step_size)==0:
     #   temp=np.loadtxt(datadir4+"bvap"+str(t)+".csv", delimiter=',')
      #  for s in range(10*step_size):
       #     if temp[s,-1]<.99:
        #        a.append(temp[s,:])
         #       e.append(temp[s,:])
          #      sizes+=1


print(sizes)
a=np.array(a)
b=np.array(b)
c=np.array(c)
d=np.array(d)
e=np.array(e)


np.savetxt(newdir+"merge_allb.csv", a, delimiter=',')

num37=[]
maxgap=[]
firstD=[]
secondD=[]
allgaps=[]
for i in range(sizes):
    firstD.append([])
    secondD.append([])
    num37.append(sum(j>.37 for j in a[i,:]))
    for k in range(32):
        firstD[i].append(a[i,k+1]-a[i,k])
        allgaps.append(firstD[i][-1])
    maxgap.append(max(firstD[i]))
    for k in range(31):
        secondD[i].append(firstD[i][k+1]-firstD[i][k])
        
np.savetxt(newdir+"merge_num37b.csv", num37, delimiter=',')
np.savetxt(newdir+"merge_maxgapb.csv", maxgap, delimiter=',')
np.savetxt(newdir+"merge_firstDb.csv", firstD, delimiter=',')      
np.savetxt(newdir+"merge_secondDb.csv", secondD, delimiter=',')      
 
plt.hist(num37,bins=100)
plt.savefig(newdir+"num37b.png")
plt.close()
plt.hist(maxgap,bins=100)
plt.savefig(newdir+"maxgapb.png")
plt.close()
plt.hist(allgaps,bins=100)
plt.savefig(newdir+"allgapsb.png")
plt.close()
afdhbuajbdhfvkahbd
# step_size = 100#100000#10000#

# ts2 =[x*step_size for x in range(1,int(max_steps/step_size)+1)]
#
# for t in ts2:
#     temp=np.loadtxt(datadir3+"bvap"+str(t)+".csv", delimiter=',')
#     c[t - step_size:t, :] = temp

#THIS IS FOR COMPARISONS!
#
def draw_plot(data, offset,edge_color, fill_color):
    pos = 10*np.arange(data.shape[1])+offset
    #bp = ax.boxplot(data, positions= pos, widths=0.3, patch_artist=True, manage_xticks=False)
    bp = ax.boxplot(data, positions= pos,widths=1, whis=[1,99],showfliers=False, patch_artist=True, manage_xticks=False)
    for element in ['boxes', 'whiskers', 'medians', 'caps']:
        plt.setp(bp[element], color=edge_color)
    for patch in bp['boxes']:
        patch.set(facecolor=fill_color)


fig, ax = plt.subplots()
draw_plot(e[0:2000,:], -2, "blue", "white")
draw_plot(e[0:10000,:], 0, "orange", "white")
draw_plot(e[0:20000,:], +2, "red", "white")




plt.plot([],[],color="blue",label="2K Steps")
plt.plot([],[],color="orange",label="10K Steps")
plt.plot([],[],color="red",label="20K Steps")
#
#
plt.ylabel("BVAP%")
plt.xlabel("Indexed Districts")
plt.xticks([])
#plt.title("BVAP% ")
plt.legend()
#plt.show()
plt.savefig(newdir+"6nvmre.png")
fig = plt.gcf()
fig.set_size_inches((12,6), forward=False)
fig.savefig(newdir+"6nvmre2.png", dpi=600)
plt.close()



fig, ax = plt.subplots()
#draw_plot(a, 0, "green", "white")
#draw_plot(b, +1,"purple", "white")
draw_plot(c, +2,"blue", "white")
draw_plot(d, 0,"orange", "white")
draw_plot(e, -2,"red", "white")


#plt.plot([],[],color="green",label="ALL COMBINED")
#plt.plot([],[],color="purple",label="Seed 23")
plt.plot([],[],color="blue",label="Seed 31")
plt.plot([],[],color="orange",label="Seed 99")
plt.plot([],[],color="red",label="Enacted")
#
#
plt.xticks([])
plt.ylabel("BVAP%")
plt.xlabel("Indexed Districts")
plt.legend()
#plt.show()
plt.savefig(newdir+"5nvmre.png")
fig = plt.gcf()
fig.set_size_inches((12,6), forward=False)
fig.savefig(newdir+"5nvmre2.png", dpi=600)
plt.close()
# #
#
#fgdvfavdf
#
medianprops = dict( color='black')

fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
ax1.add_patch(patches.Rectangle((0, .37), 35, .18,color='honeydew'))
plt.plot([0,34], [.55, .55], 'lightgreen')
plt.plot([0,34], [.37, .37], 'lightgreen')

plt.boxplot(a,whis=[1,99],showfliers=False,medianprops=medianprops)
plt.plot([],[],color='k',label="ReCom Ensemble")
#fig, ax = plt.subplots()
#draw_plot(a, 1, "black", "white")
plt.xticks(range(1,34))
#plt.plot(range(1,34), a[0,:], 'ro')
plt.plot(range(1,34), [0.07253105784916551, 0.10824003731840597, 0.13398271190814087, 0.13546485835604286, 0.13711169698855355, 0.15123053901747907, 0.16064167834079338, 0.1671916890080429, 0.1714120178778348, 0.18436445635035012, 0.18601774940250362, 0.18926480993117642, 0.19611679964912873, 0.2102159841056207, 0.2258110938774205, 0.24239331194711772, 0.2456163350922618, 0.2514435871257134, 0.27596109603820584, 0.2945835079944907, 0.33525600505689, 0.5518884518212926, 0.5534953948361769, 0.5542911182914335, 0.5545930898968396, 0.5629610159189105, 0.5636955706345689, 0.5658926317188226, 0.5723899599854493, 0.5877664632354213, 0.5952869519900984, 0.5997255028212211, 0.6071539251985842]
, 'o', color = 'red', label='Enacted', markersize=5)
#plt.title("BVAP%")
#plt.legend()
#plt.show()

plt.plot(range(1,34),[0.11285994764397905, 0.11923800918605526, 0.13897052649256864, 0.15476480623933708, 0.16074647274535397, 0.16448098456572177, 0.1924158221641059, 0.20748078731476377, 0.2389974186557889, 0.247833944163894, 0.2492809364548495, 0.24964654261802227, 0.26311193301484564, 0.26698328522521314, 0.3289734116249918, 0.32909409158231023, 0.3425087866629343, 0.3499765322802531, 0.3698742706878133, 0.38867736303932165, 0.40328054298642535, 0.4191690178691388, 0.43597163215468504, 0.4438127358869349, 0.4490251331585034, 0.451499388004896, 0.463070511068598, 0.46434859154929575, 0.4681934272618101, 0.49059480627868907, 0.5000960491771788, 0.5379312500977005, 0.570986567004151]
, 'o', color='orange', label='Princeton', markersize=5)
plt.plot(range(1,34), [0.10824003731840597, 0.13539411689800077, 0.13711169698855355, 0.1485726789200835, 0.15400372121605244, 0.15964176113233544, 0.16692439297229716, 0.1714120178778348, 0.17672291013890518, 0.2112792472024415, 0.21340934034432488, 0.2258110938774205, 0.22767239760290928, 0.24239331194711772, 0.25123302994864494, 0.2732269699021939, 0.2802270884022709, 0.3047803894000061, 0.3342634208283905, 0.33525600505689, 0.4240456445754232, 0.4797818705628151, 0.4936303619414126, 0.5012558819788885, 0.5085824894818511, 0.514421058943455, 0.5180834320390713, 0.5225580889610064, 0.5269443588037711, 0.5294892751109184, 0.5353813664186369, 0.5542911182914335, 0.5726470920201874]
, 'o', color = 'blue', label='Democratic', markersize=5)

nvm=[.088,.09,.107,.119,.131,.135,.148,.159,.163,.167,.173,.173,.175,.175,.191,.195,.198,
.2,.208,.214,.234,.238,.259,.274,.284,.307,.320,.327,.333,.421,.455,.462,.469,.484,
.484,.510,.513,.520,.521,.525,.527,.530,.558]

plt.plot(range(1,34),nvm[-34:-1], 'o', color = 'green', label='NVM', markersize=5)

plt.ylim([0,.85])
plt.axvline(4.5,color='gray',linestyle='--')
plt.axvline(8.5,color='gray',linestyle='--')
plt.axvline(17.5,color='gray',linestyle='--')
plt.axvline(21.5,color='gray',linestyle='--')
ax1.text(1,.86,"4 Districts")
ax1.text(5.25,.86,"4 Districts")
ax1.text(11.5,.86,"9 Districts")
ax1.text(18.25,.86,"4 Districts")
ax1.text(26,.86,"12 Districts")
plt.ylabel("BVAP%")
plt.xlabel("Indexed Districts")
plt.legend()
plt.savefig(newdir+"9nvmre3.png")
fig = plt.gcf()
fig.set_size_inches((12,6), forward=False)
fig.savefig(newdir+"thisone.png", dpi=600)

plt.show()

plt.close()
fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
ax1.add_patch(patches.Rectangle((0, .37), 35, .18,color='honeydew'))#lightgreen
plt.plot([0,34], [.55, .55], 'lightgreen')
plt.plot([0,34], [.37, .37], 'lightgreen')

plt.boxplot(a,whis=[1,99],showfliers=False,medianprops=medianprops)
plt.plot([],[],color='k',label="Mixed Ensemble")

plt.plot(range(1,34), [0.07253105784916551, 0.10824003731840597, 0.13398271190814087, 0.13546485835604286, 0.13711169698855355, 0.15123053901747907, 0.16064167834079338, 0.1671916890080429, 0.1714120178778348, 0.18436445635035012, 0.18601774940250362, 0.18926480993117642, 0.19611679964912873, 0.2102159841056207, 0.2258110938774205, 0.24239331194711772, 0.2456163350922618, 0.2514435871257134, 0.27596109603820584, 0.2945835079944907, 0.33525600505689, 0.5518884518212926, 0.5534953948361769, 0.5542911182914335, 0.5545930898968396, 0.5629610159189105, 0.5636955706345689, 0.5658926317188226, 0.5723899599854493, 0.5877664632354213, 0.5952869519900984, 0.5997255028212211, 0.6071539251985842]
, 'o', color = 'red', label='Enacted', markersize=5)

plt.plot(range(1,34),[0.1130,    0.1140,    0.1370,    0.1430,    0.1500,    0.1520,    0.1670,    0.1680,    0.1820,    0.1850,    0.1960,    0.1980,    0.2050,    0.2220,    0.2550,    0.2730,    0.2740,    0.2760,    0.3350,    0.3410,    0.3800,    0.4430,    0.4680,    0.4740,    0.5140,    0.5340,    0.5440,    0.5510,    0.5530,    0.5640,    0.5860,    0.6000,    0.6180]
, 'o', color='pink', label='GOP1', markersize=5)
plt.plot(range(1,34), [0.1130,    0.1140,    0.1370,    0.1430,    0.1500,    0.1520,    0.1670,    0.1680,    0.1820,    0.1850,    0.1960,    0.1980,    0.2050,    0.2310,    0.2550,    0.2730,    0.2760,    0.2920,    0.3350,    0.3410,    0.3800,   0.4430,    0.4680,    0.4740,    0.5140,    0.5340,    0.5440,   0.5510,    0.5530,    0.5640,    0.5730,    0.5860,    0.6180]
, 'o', color = 'purple', label='GOP2', markersize=5)
plt.plot(range(1,34), [0.1360,    0.1370,    0.1480,    0.1510,    0.1530,    0.1570,    0.1590,    0.1640,    0.1650,    0.2020,    0.2060,    0.2100,    0.2100,    0.2370,    0.2620,    0.2720,    0.2780,    0.2820,    0.2970,    0.3350,    0.4680,    0.4740,    0.4840,    0.4940,    0.5140,    0.5180,    0.5220,    0.5270,    0.5290,    0.5350,    0.5450,    0.5540,    0.5730]
, 'o', color = 'green', label='GOP3', markersize=5)


plt.ylim([0,.85])
plt.axvline(4.5,color='gray',linestyle='--')
plt.axvline(8.5,color='gray',linestyle='--')
plt.axvline(17.5,color='gray',linestyle='--')
plt.axvline(21.5,color='gray',linestyle='--')
ax1.text(1,.86,"4 Districts")
ax1.text(5.25,.86,"4 Districts")
ax1.text(11.5,.86,"9 Districts")
ax1.text(18.25,.86,"4 Districts")
ax1.text(26,.86,"12 Districts")
plt.legend()
plt.ylabel("BVAP%")
plt.xlabel("Indexed Districts")
#plt.savefig(newdir+"bvapbox99g.png")
#fig = plt.gcf()
#fig.set_size_inches((11,8.5), forward=False)
#fig.savefig(newdir+"bvapbox992g.png", dpi=500)

plt.savefig(newdir+"9nvmre4.png")
fig = plt.gcf()
fig.set_size_inches((12,6), forward=False) #maybe try 6 by 2?
fig.savefig(newdir+"9nvmre42.png", dpi=600)

plt.show()

#plt.close()

asgbads

#fvbas
# plt.boxplot(a,whis=[10,90])
# #plt.plot(range(1,34), a[0,:], 'ro')
# plt.plot(range(1,34), [0.07253105784916551, 0.10824003731840597, 0.13398271190814087, 0.13546485835604286, 0.13711169698855355, 0.15123053901747907, 0.16064167834079338, 0.1671916890080429, 0.1714120178778348, 0.18436445635035012, 0.18601774940250362, 0.18926480993117642, 0.19611679964912873, 0.2102159841056207, 0.2258110938774205, 0.24239331194711772, 0.2456163350922618, 0.2514435871257134, 0.27596109603820584, 0.2945835079944907, 0.33525600505689, 0.5518884518212926, 0.5534953948361769, 0.5542911182914335, 0.5545930898968396, 0.5629610159189105, 0.5636955706345689, 0.5658926317188226, 0.5723899599854493, 0.5877664632354213, 0.5952869519900984, 0.5997255028212211, 0.6071539251985842]
# , 'ro', label='Enacted')
# plt.plot(range(1,34),[0.11285994764397905, 0.11923800918605526, 0.13897052649256864, 0.15476480623933708, 0.16074647274535397, 0.16448098456572177, 0.1924158221641059, 0.20748078731476377, 0.2389974186557889, 0.247833944163894, 0.2492809364548495, 0.24964654261802227, 0.26311193301484564, 0.26698328522521314, 0.3289734116249918, 0.32909409158231023, 0.3425087866629343, 0.3499765322802531, 0.3698742706878133, 0.38867736303932165, 0.40328054298642535, 0.4191690178691388, 0.43597163215468504, 0.4438127358869349, 0.4490251331585034, 0.451499388004896, 0.463070511068598, 0.46434859154929575, 0.4681934272618101, 0.49059480627868907, 0.5000960491771788, 0.5379312500977005, 0.570986567004151]
# , 'bo', label='Princeton')
# plt.plot(range(1,34), [0.10824003731840597, 0.13539411689800077, 0.13711169698855355, 0.1485726789200835, 0.15400372121605244, 0.15964176113233544, 0.16692439297229716, 0.1714120178778348, 0.17672291013890518, 0.2112792472024415, 0.21340934034432488, 0.2258110938774205, 0.22767239760290928, 0.24239331194711772, 0.25123302994864494, 0.2732269699021939, 0.2802270884022709, 0.3047803894000061, 0.3342634208283905, 0.33525600505689, 0.4240456445754232, 0.4797818705628151, 0.4936303619414126, 0.5012558819788885, 0.5085824894818511, 0.514421058943455, 0.5180834320390713, 0.5225580889610064, 0.5269443588037711, 0.5294892751109184, 0.5353813664186369, 0.5542911182914335, 0.5726470920201874]
# , 'yo', label='Democratic')
# plt.plot([0,34], [.55, .55], 'g')
# plt.plot([0,34], [.37, .37], 'g')
#
# plt.title("BVAP%")
# plt.legend()
# plt.savefig(newdir+"bvapbox.png")
# fig = plt.gcf()
# fig.set_size_inches((11,8.5), forward=False)
# fig.savefig(newdir+"bvapbox2.png", dpi=500)
#
# plt.close()
medianprops = dict( color='green')
#linestyle='-', linewidth=1.5,
fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
ax1.add_patch(patches.Rectangle((0, .37), 35, .18,color='lightgreen'))
plt.boxplot(a,whis=[1,99], medianprops=medianprops)
#plt.plot(range(1,34), a[0,:], 'ro')
plt.plot(range(1,34), [0.07253105784916551, 0.10824003731840597, 0.13398271190814087, 0.13546485835604286, 0.13711169698855355, 0.15123053901747907, 0.16064167834079338, 0.1671916890080429, 0.1714120178778348, 0.18436445635035012, 0.18601774940250362, 0.18926480993117642, 0.19611679964912873, 0.2102159841056207, 0.2258110938774205, 0.24239331194711772, 0.2456163350922618, 0.2514435871257134, 0.27596109603820584, 0.2945835079944907, 0.33525600505689, 0.5518884518212926, 0.5534953948361769, 0.5542911182914335, 0.5545930898968396, 0.5629610159189105, 0.5636955706345689, 0.5658926317188226, 0.5723899599854493, 0.5877664632354213, 0.5952869519900984, 0.5997255028212211, 0.6071539251985842]
, 'o', color = 'red', label='Enacted')
plt.plot(range(1,34),[0.11285994764397905, 0.11923800918605526, 0.13897052649256864, 0.15476480623933708, 0.16074647274535397, 0.16448098456572177, 0.1924158221641059, 0.20748078731476377, 0.2389974186557889, 0.247833944163894, 0.2492809364548495, 0.24964654261802227, 0.26311193301484564, 0.26698328522521314, 0.3289734116249918, 0.32909409158231023, 0.3425087866629343, 0.3499765322802531, 0.3698742706878133, 0.38867736303932165, 0.40328054298642535, 0.4191690178691388, 0.43597163215468504, 0.4438127358869349, 0.4490251331585034, 0.451499388004896, 0.463070511068598, 0.46434859154929575, 0.4681934272618101, 0.49059480627868907, 0.5000960491771788, 0.5379312500977005, 0.570986567004151]
, 'o', color='orange', label='Princeton')
plt.plot(range(1,34), [0.10824003731840597, 0.13539411689800077, 0.13711169698855355, 0.1485726789200835, 0.15400372121605244, 0.15964176113233544, 0.16692439297229716, 0.1714120178778348, 0.17672291013890518, 0.2112792472024415, 0.21340934034432488, 0.2258110938774205, 0.22767239760290928, 0.24239331194711772, 0.25123302994864494, 0.2732269699021939, 0.2802270884022709, 0.3047803894000061, 0.3342634208283905, 0.33525600505689, 0.4240456445754232, 0.4797818705628151, 0.4936303619414126, 0.5012558819788885, 0.5085824894818511, 0.514421058943455, 0.5180834320390713, 0.5225580889610064, 0.5269443588037711, 0.5294892751109184, 0.5353813664186369, 0.5542911182914335, 0.5726470920201874]
, 'o', color = 'blue', label='Democratic')
plt.plot([0,34], [.55, .55], 'g')
plt.plot([0,34], [.37, .37], 'g')

plt.title("BVAP%")
plt.legend()
plt.savefig(newdir+"bvapbox99.png")
fig = plt.gcf()
fig.set_size_inches((11,8.5), forward=False)
fig.savefig(newdir+"bvapbox992.png", dpi=500)

plt.close()
fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
ax1.add_patch(patches.Rectangle((0, .37), 35, .18,color='lightgreen'))
plt.boxplot(a,whis=[.1,99.9], medianprops=medianprops)
#plt.plot(range(1,34), a[0,:], 'ro')
plt.plot(range(1,34), [0.07253105784916551, 0.10824003731840597, 0.13398271190814087, 0.13546485835604286, 0.13711169698855355, 0.15123053901747907, 0.16064167834079338, 0.1671916890080429, 0.1714120178778348, 0.18436445635035012, 0.18601774940250362, 0.18926480993117642, 0.19611679964912873, 0.2102159841056207, 0.2258110938774205, 0.24239331194711772, 0.2456163350922618, 0.2514435871257134, 0.27596109603820584, 0.2945835079944907, 0.33525600505689, 0.5518884518212926, 0.5534953948361769, 0.5542911182914335, 0.5545930898968396, 0.5629610159189105, 0.5636955706345689, 0.5658926317188226, 0.5723899599854493, 0.5877664632354213, 0.5952869519900984, 0.5997255028212211, 0.6071539251985842]
, 'o', color = 'red', label='Enacted')
plt.plot(range(1,34),[0.11285994764397905, 0.11923800918605526, 0.13897052649256864, 0.15476480623933708, 0.16074647274535397, 0.16448098456572177, 0.1924158221641059, 0.20748078731476377, 0.2389974186557889, 0.247833944163894, 0.2492809364548495, 0.24964654261802227, 0.26311193301484564, 0.26698328522521314, 0.3289734116249918, 0.32909409158231023, 0.3425087866629343, 0.3499765322802531, 0.3698742706878133, 0.38867736303932165, 0.40328054298642535, 0.4191690178691388, 0.43597163215468504, 0.4438127358869349, 0.4490251331585034, 0.451499388004896, 0.463070511068598, 0.46434859154929575, 0.4681934272618101, 0.49059480627868907, 0.5000960491771788, 0.5379312500977005, 0.570986567004151]
, 'o', color='orange', label='Princeton')
plt.plot(range(1,34), [0.10824003731840597, 0.13539411689800077, 0.13711169698855355, 0.1485726789200835, 0.15400372121605244, 0.15964176113233544, 0.16692439297229716, 0.1714120178778348, 0.17672291013890518, 0.2112792472024415, 0.21340934034432488, 0.2258110938774205, 0.22767239760290928, 0.24239331194711772, 0.25123302994864494, 0.2732269699021939, 0.2802270884022709, 0.3047803894000061, 0.3342634208283905, 0.33525600505689, 0.4240456445754232, 0.4797818705628151, 0.4936303619414126, 0.5012558819788885, 0.5085824894818511, 0.514421058943455, 0.5180834320390713, 0.5225580889610064, 0.5269443588037711, 0.5294892751109184, 0.5353813664186369, 0.5542911182914335, 0.5726470920201874]
, 'o', color = 'blue', label='Democratic')
plt.plot([0,34], [.55, .55], 'g')
plt.plot([0,34], [.37, .37], 'g')

plt.title("BVAP%")
plt.legend()
plt.savefig(newdir+"bvapbox999.png")
fig = plt.gcf()
fig.set_size_inches((11,8.5), forward=False)
fig.savefig(newdir+"bvapbox9992.png", dpi=500)

plt.close()
fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
ax1.add_patch(patches.Rectangle((0, .37), 35, .18,color='lightgreen'))
plt.boxplot(a,whis=[.01,99.99], medianprops=medianprops)
#plt.plot(range(1,34), a[0,:], 'ro')
plt.plot(range(1,34), [0.07253105784916551, 0.10824003731840597, 0.13398271190814087, 0.13546485835604286, 0.13711169698855355, 0.15123053901747907, 0.16064167834079338, 0.1671916890080429, 0.1714120178778348, 0.18436445635035012, 0.18601774940250362, 0.18926480993117642, 0.19611679964912873, 0.2102159841056207, 0.2258110938774205, 0.24239331194711772, 0.2456163350922618, 0.2514435871257134, 0.27596109603820584, 0.2945835079944907, 0.33525600505689, 0.5518884518212926, 0.5534953948361769, 0.5542911182914335, 0.5545930898968396, 0.5629610159189105, 0.5636955706345689, 0.5658926317188226, 0.5723899599854493, 0.5877664632354213, 0.5952869519900984, 0.5997255028212211, 0.6071539251985842]
, 'o', color = 'red', label='Enacted')
plt.plot(range(1,34),[0.11285994764397905, 0.11923800918605526, 0.13897052649256864, 0.15476480623933708, 0.16074647274535397, 0.16448098456572177, 0.1924158221641059, 0.20748078731476377, 0.2389974186557889, 0.247833944163894, 0.2492809364548495, 0.24964654261802227, 0.26311193301484564, 0.26698328522521314, 0.3289734116249918, 0.32909409158231023, 0.3425087866629343, 0.3499765322802531, 0.3698742706878133, 0.38867736303932165, 0.40328054298642535, 0.4191690178691388, 0.43597163215468504, 0.4438127358869349, 0.4490251331585034, 0.451499388004896, 0.463070511068598, 0.46434859154929575, 0.4681934272618101, 0.49059480627868907, 0.5000960491771788, 0.5379312500977005, 0.570986567004151]
, 'o', color='orange', label='Princeton')
plt.plot(range(1,34), [0.10824003731840597, 0.13539411689800077, 0.13711169698855355, 0.1485726789200835, 0.15400372121605244, 0.15964176113233544, 0.16692439297229716, 0.1714120178778348, 0.17672291013890518, 0.2112792472024415, 0.21340934034432488, 0.2258110938774205, 0.22767239760290928, 0.24239331194711772, 0.25123302994864494, 0.2732269699021939, 0.2802270884022709, 0.3047803894000061, 0.3342634208283905, 0.33525600505689, 0.4240456445754232, 0.4797818705628151, 0.4936303619414126, 0.5012558819788885, 0.5085824894818511, 0.514421058943455, 0.5180834320390713, 0.5225580889610064, 0.5269443588037711, 0.5294892751109184, 0.5353813664186369, 0.5542911182914335, 0.5726470920201874]
, 'o', color = 'blue', label='Democratic')
plt.plot([0,34], [.55, .55], 'g')
plt.plot([0,34], [.37, .37], 'g')

plt.title("BVAP%")
plt.legend()
plt.savefig(newdir+"bvapbox9999.png")
fig = plt.gcf()
fig.set_size_inches((11,8.5), forward=False)
fig.savefig(newdir+"bvapbox99992.png", dpi=500)

plt.close()



fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
ax1.add_patch(patches.Rectangle((0, .37), 35, .18,color='lightgreen'))
plt.boxplot(a, whis=[1,99], medianprops=medianprops)
#plt.plot(range(1,34), a[0,:], 'ro')
plt.plot(range(1,34), [0.1080,    0.1350,    0.1370,    0.1490,    0.1540,    0.1600,    0.1670,    0.1710,    0.1770,    0.2110,    0.2130,    0.2260,    0.2280,    0.2420,    0.2510,    0.2730,    0.2800,    0.3050,    0.3340,    0.3350,    0.4240,    0.4800,    0.4940,    0.5010,    0.5090,    0.5140,    0.5180,    0.5230,    0.5270,    0.5290,    0.5350,    0.5540,    0.5730]
, 'o', color = 'purple', label='HB7001')
plt.plot(range(1,34),[0.1130,    0.1140,    0.1370,    0.1430,    0.1500,    0.1520,    0.1670,    0.1680,    0.1820,    0.1850,    0.1960,    0.1980,    0.2050,    0.2220,    0.2550,    0.2730,    0.2740,    0.2760,    0.3350,    0.3410,    0.3800,    0.4430,    0.4680,    0.4740,    0.5140,    0.5340,    0.5440,    0.5510,    0.5530,    0.5640,    0.5860,    0.6000,    0.6180]
, 'o', color='orange', label='HB7002')
plt.plot(range(1,34), [0.1130,    0.1140,    0.1370,    0.1430,    0.1500,    0.1520,    0.1670,    0.1680,    0.1820,    0.1850,    0.1960,    0.1980,    0.2050,    0.2310,    0.2550,    0.2730,    0.2760,    0.2920,    0.3350,    0.3410,    0.3800,   0.4430,    0.4680,    0.4740,    0.5140,    0.5340,    0.5440,   0.5510,    0.5530,    0.5640,    0.5730,    0.5860,    0.6180]
, 'o', color = 'pink', label='HB7002SUB')
plt.plot(range(1,34), [0.1360,    0.1370,    0.1480,    0.1510,    0.1530,    0.1570,    0.1590,    0.1640,    0.1650,    0.2020,    0.2060,    0.2100,    0.2100,    0.2370,    0.2620,    0.2720,    0.2780,    0.2820,    0.2970,    0.3350,    0.4680,    0.4740,    0.4840,    0.4940,    0.5140,    0.5180,    0.5220,    0.5270,    0.5290,    0.5350,    0.5450,    0.5540,    0.5730]
, 'o', color = 'yellow', label='HB7003')
plt.plot([0,34], [.55, .55], 'g')
plt.plot([0,34], [.37, .37], 'g')

plt.title("BVAP%")
plt.legend()
plt.savefig(newdir+"bvapbox99g.png")
fig = plt.gcf()
fig.set_size_inches((11,8.5), forward=False)
fig.savefig(newdir+"bvapbox992g.png", dpi=500)

plt.close()
fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
ax1.add_patch(patches.Rectangle((0, .37), 35, .18,color='lightgreen'))
plt.boxplot(a,whis=[.1,99.9], medianprops=medianprops)
#plt.plot(range(1,34), a[0,:], 'ro')
plt.plot(range(1,34), [0.1080,    0.1350,    0.1370,    0.1490,    0.1540,    0.1600,    0.1670,    0.1710,    0.1770,    0.2110,    0.2130,    0.2260,    0.2280,    0.2420,    0.2510,    0.2730,    0.2800,    0.3050,    0.3340,    0.3350,    0.4240,    0.4800,    0.4940,    0.5010,    0.5090,    0.5140,    0.5180,    0.5230,    0.5270,    0.5290,    0.5350,    0.5540,    0.5730]
, 'o', color = 'purple', label='HB7001')
plt.plot(range(1,34),[0.1130,    0.1140,    0.1370,    0.1430,    0.1500,    0.1520,    0.1670,    0.1680,    0.1820,    0.1850,    0.1960,    0.1980,    0.2050,    0.2220,    0.2550,    0.2730,    0.2740,    0.2760,    0.3350,    0.3410,    0.3800,    0.4430,    0.4680,    0.4740,    0.5140,    0.5340,    0.5440,    0.5510,    0.5530,    0.5640,    0.5860,    0.6000,    0.6180]
, 'o', color='orange', label='HB7002')
plt.plot(range(1,34), [0.1130,    0.1140,    0.1370,    0.1430,    0.1500,    0.1520,    0.1670,    0.1680,    0.1820,    0.1850,    0.1960,    0.1980,    0.2050,    0.2310,    0.2550,    0.2730,    0.2760,    0.2920,    0.3350,    0.3410,    0.3800,   0.4430,    0.4680,    0.4740,    0.5140,    0.5340,    0.5440,   0.5510,    0.5530,    0.5640,    0.5730,    0.5860,    0.6180]
, 'o', color = 'pink', label='HB7002SUB')
plt.plot(range(1,34), [0.1360,    0.1370,    0.1480,    0.1510,    0.1530,    0.1570,    0.1590,    0.1640,    0.1650,    0.2020,    0.2060,    0.2100,    0.2100,    0.2370,    0.2620,    0.2720,    0.2780,    0.2820,    0.2970,    0.3350,    0.4680,    0.4740,    0.4840,    0.4940,    0.5140,    0.5180,    0.5220,    0.5270,    0.5290,    0.5350,    0.5450,    0.5540,    0.5730]
, 'o', color = 'yellow', label='HB7003')
plt.plot([0,34], [.55, .55], 'g')
plt.plot([0,34], [.37, .37], 'g')

plt.title("BVAP%")
plt.legend()
plt.savefig(newdir+"bvapbox999g.png")
fig = plt.gcf()
fig.set_size_inches((11,8.5), forward=False)
fig.savefig(newdir+"bvapbox9992g.png", dpi=500)

plt.close()
fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
ax1.add_patch(patches.Rectangle((0, .37), 35, .18,color='lightgreen'))
plt.boxplot(a,whis=[.01,99.99], medianprops=medianprops)
#plt.plot(range(1,34), a[0,:], 'ro')
plt.plot(range(1,34), [0.1080,    0.1350,    0.1370,    0.1490,    0.1540,    0.1600,    0.1670,    0.1710,    0.1770,    0.2110,    0.2130,    0.2260,    0.2280,    0.2420,    0.2510,    0.2730,    0.2800,    0.3050,    0.3340,    0.3350,    0.4240,    0.4800,    0.4940,    0.5010,    0.5090,    0.5140,    0.5180,    0.5230,    0.5270,    0.5290,    0.5350,    0.5540,    0.5730]
, 'o', color = 'purple', label='HB7001')
plt.plot(range(1,34),[0.1130,    0.1140,    0.1370,    0.1430,    0.1500,    0.1520,    0.1670,    0.1680,    0.1820,    0.1850,    0.1960,    0.1980,    0.2050,    0.2220,    0.2550,    0.2730,    0.2740,    0.2760,    0.3350,    0.3410,    0.3800,    0.4430,    0.4680,    0.4740,    0.5140,    0.5340,    0.5440,    0.5510,    0.5530,    0.5640,    0.5860,    0.6000,    0.6180]
, 'o', color='orange', label='HB7002')
plt.plot(range(1,34), [0.1130,    0.1140,    0.1370,    0.1430,    0.1500,    0.1520,    0.1670,    0.1680,    0.1820,    0.1850,    0.1960,    0.1980,    0.2050,    0.2310,    0.2550,    0.2730,    0.2760,    0.2920,    0.3350,    0.3410,    0.3800,   0.4430,    0.4680,    0.4740,    0.5140,    0.5340,    0.5440,   0.5510,    0.5530,    0.5640,    0.5730,    0.5860,    0.6180]
, 'o', color = 'pink', label='HB7002SUB')
plt.plot(range(1,34), [0.1360,    0.1370,    0.1480,    0.1510,    0.1530,    0.1570,    0.1590,    0.1640,    0.1650,    0.2020,    0.2060,    0.2100,    0.2100,    0.2370,    0.2620,    0.2720,    0.2780,    0.2820,    0.2970,    0.3350,    0.4680,    0.4740,    0.4840,    0.4940,    0.5140,    0.5180,    0.5220,    0.5270,    0.5290,    0.5350,    0.5450,    0.5540,    0.5730]
, 'o', color = 'yellow', label='HB7003')
plt.plot([0,34], [.55, .55], 'g')
plt.plot([0,34], [.37, .37], 'g')

plt.title("BVAP%")
plt.legend()
plt.savefig(newdir+"bvapbox9999g.png")
fig = plt.gcf()
fig.set_size_inches((11,8.5), forward=False)
fig.savefig(newdir+"bvapbox99992g.png", dpi=500)

plt.close()



fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
ax1.add_patch(patches.Rectangle((0, .37), 35, .18,color='lightgreen'))
plt.boxplot(a,whis=[1,99], medianprops=medianprops)
#plt.plot(range(1,34), a[0,:], 'ro')
plt.plot(range(1,34), [0.07253105784916551, 0.10824003731840597, 0.13398271190814087, 0.13546485835604286, 0.13711169698855355, 0.15123053901747907, 0.16064167834079338, 0.1671916890080429, 0.1714120178778348, 0.18436445635035012, 0.18601774940250362, 0.18926480993117642, 0.19611679964912873, 0.2102159841056207, 0.2258110938774205, 0.24239331194711772, 0.2456163350922618, 0.2514435871257134, 0.27596109603820584, 0.2945835079944907, 0.33525600505689, 0.5518884518212926, 0.5534953948361769, 0.5542911182914335, 0.5545930898968396, 0.5629610159189105, 0.5636955706345689, 0.5658926317188226, 0.5723899599854493, 0.5877664632354213, 0.5952869519900984, 0.5997255028212211, 0.6071539251985842]
, 'o', color = 'red', label='Enacted')
plt.plot(range(1,34), [0.1080,    0.1350,    0.1370,    0.1490,    0.1540,    0.1600,    0.1670,    0.1710,    0.1770,    0.2110,    0.2130,    0.2260,    0.2280,    0.2420,    0.2510,    0.2730,    0.2800,    0.3050,    0.3340,    0.3350,    0.4240,    0.4800,    0.4940,    0.5010,    0.5090,    0.5140,    0.5180,    0.5230,    0.5270,    0.5290,    0.5350,    0.5540,    0.5730]
, 'o', color = 'gray', label='HB7001')
plt.plot(range(1,34),[0.1130,    0.1140,    0.1370,    0.1430,    0.1500,    0.1520,    0.1670,    0.1680,    0.1820,    0.1850,    0.1960,    0.1980,    0.2050,    0.2220,    0.2550,    0.2730,    0.2740,    0.2760,    0.3350,    0.3410,    0.3800,    0.4430,    0.4680,    0.4740,    0.5140,    0.5340,    0.5440,    0.5510,    0.5530,    0.5640,    0.5860,    0.6000,    0.6180]
, 'o', color='gray', label='HB7002')
plt.plot(range(1,34), [0.1130,    0.1140,    0.1370,    0.1430,    0.1500,    0.1520,    0.1670,    0.1680,    0.1820,    0.1850,    0.1960,    0.1980,    0.2050,    0.2310,    0.2550,    0.2730,    0.2760,    0.2920,    0.3350,    0.3410,    0.3800,   0.4430,    0.4680,    0.4740,    0.5140,    0.5340,    0.5440,   0.5510,    0.5530,    0.5640,    0.5730,    0.5860,    0.6180]
, 'o', color = 'gray', label='HB7002SUB')
plt.plot(range(1,34), [0.1360,    0.1370,    0.1480,    0.1510,    0.1530,    0.1570,    0.1590,    0.1640,    0.1650,    0.2020,    0.2060,    0.2100,    0.2100,    0.2370,    0.2620,    0.2720,    0.2780,    0.2820,    0.2970,    0.3350,    0.4680,    0.4740,    0.4840,    0.4940,    0.5140,    0.5180,    0.5220,    0.5270,    0.5290,    0.5350,    0.5450,    0.5540,    0.5730]
, 'o', color = 'gray', label='HB7003')
plt.plot([0,34], [.55, .55], 'g')
plt.plot([0,34], [.37, .37], 'g')

plt.title("BVAP%")
plt.legend()
plt.savefig(newdir+"bvapbox99gb.png")
fig = plt.gcf()
fig.set_size_inches((11,8.5), forward=False)
fig.savefig(newdir+"bvapbox992gb.png", dpi=500)

plt.close()
fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
ax1.add_patch(patches.Rectangle((0, .37), 35, .18,color='lightgreen'))
plt.boxplot(a,whis=[.1,99.9], medianprops=medianprops)
#plt.plot(range(1,34), a[0,:], 'ro')
plt.plot(range(1,34), [0.07253105784916551, 0.10824003731840597, 0.13398271190814087, 0.13546485835604286, 0.13711169698855355, 0.15123053901747907, 0.16064167834079338, 0.1671916890080429, 0.1714120178778348, 0.18436445635035012, 0.18601774940250362, 0.18926480993117642, 0.19611679964912873, 0.2102159841056207, 0.2258110938774205, 0.24239331194711772, 0.2456163350922618, 0.2514435871257134, 0.27596109603820584, 0.2945835079944907, 0.33525600505689, 0.5518884518212926, 0.5534953948361769, 0.5542911182914335, 0.5545930898968396, 0.5629610159189105, 0.5636955706345689, 0.5658926317188226, 0.5723899599854493, 0.5877664632354213, 0.5952869519900984, 0.5997255028212211, 0.6071539251985842]
, 'o', color = 'red', label='Enacted')
plt.plot(range(1,34), [0.1080,    0.1350,    0.1370,    0.1490,    0.1540,    0.1600,    0.1670,    0.1710,    0.1770,    0.2110,    0.2130,    0.2260,    0.2280,    0.2420,    0.2510,    0.2730,    0.2800,    0.3050,    0.3340,    0.3350,    0.4240,    0.4800,    0.4940,    0.5010,    0.5090,    0.5140,    0.5180,    0.5230,    0.5270,    0.5290,    0.5350,    0.5540,    0.5730]
, 'o', color = 'gray', label='HB7001')
plt.plot(range(1,34),[0.1130,    0.1140,    0.1370,    0.1430,    0.1500,    0.1520,    0.1670,    0.1680,    0.1820,    0.1850,    0.1960,    0.1980,    0.2050,    0.2220,    0.2550,    0.2730,    0.2740,    0.2760,    0.3350,    0.3410,    0.3800,    0.4430,    0.4680,    0.4740,    0.5140,    0.5340,    0.5440,    0.5510,    0.5530,    0.5640,    0.5860,    0.6000,    0.6180]
, 'o', color='gray', label='HB7002')
plt.plot(range(1,34), [0.1130,    0.1140,    0.1370,    0.1430,    0.1500,    0.1520,    0.1670,    0.1680,    0.1820,    0.1850,    0.1960,    0.1980,    0.2050,    0.2310,    0.2550,    0.2730,    0.2760,    0.2920,    0.3350,    0.3410,    0.3800,   0.4430,    0.4680,    0.4740,    0.5140,    0.5340,    0.5440,   0.5510,    0.5530,    0.5640,    0.5730,    0.5860,    0.6180]
, 'o', color = 'gray', label='HB7002SUB')
plt.plot(range(1,34), [0.1360,    0.1370,    0.1480,    0.1510,    0.1530,    0.1570,    0.1590,    0.1640,    0.1650,    0.2020,    0.2060,    0.2100,    0.2100,    0.2370,    0.2620,    0.2720,    0.2780,    0.2820,    0.2970,    0.3350,    0.4680,    0.4740,    0.4840,    0.4940,    0.5140,    0.5180,    0.5220,    0.5270,    0.5290,    0.5350,    0.5450,    0.5540,    0.5730]
, 'o', color = 'gray', label='HB7003')
plt.plot([0,34], [.55, .55], 'g')
plt.plot([0,34], [.37, .37], 'g')

plt.title("BVAP%")
plt.legend()
plt.savefig(newdir+"bvapbox999gb.png")
fig = plt.gcf()
fig.set_size_inches((11,8.5), forward=False)
fig.savefig(newdir+"bvapbox9992gb.png", dpi=500)

plt.close()
fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
ax1.add_patch(patches.Rectangle((0, .37), 35, .18,color='lightgreen'))
plt.boxplot(a,whis=[.01,99.99], medianprops=medianprops)
#plt.plot(range(1,34), a[0,:], 'ro')
plt.plot(range(1,34), [0.07253105784916551, 0.10824003731840597, 0.13398271190814087, 0.13546485835604286, 0.13711169698855355, 0.15123053901747907, 0.16064167834079338, 0.1671916890080429, 0.1714120178778348, 0.18436445635035012, 0.18601774940250362, 0.18926480993117642, 0.19611679964912873, 0.2102159841056207, 0.2258110938774205, 0.24239331194711772, 0.2456163350922618, 0.2514435871257134, 0.27596109603820584, 0.2945835079944907, 0.33525600505689, 0.5518884518212926, 0.5534953948361769, 0.5542911182914335, 0.5545930898968396, 0.5629610159189105, 0.5636955706345689, 0.5658926317188226, 0.5723899599854493, 0.5877664632354213, 0.5952869519900984, 0.5997255028212211, 0.6071539251985842]
, 'o', color = 'red', label='Enacted')
plt.plot(range(1,34), [0.1080,    0.1350,    0.1370,    0.1490,    0.1540,    0.1600,    0.1670,    0.1710,    0.1770,    0.2110,    0.2130,    0.2260,    0.2280,    0.2420,    0.2510,    0.2730,    0.2800,    0.3050,    0.3340,    0.3350,    0.4240,    0.4800,    0.4940,    0.5010,    0.5090,    0.5140,    0.5180,    0.5230,    0.5270,    0.5290,    0.5350,    0.5540,    0.5730]
, 'o', color = 'gray', label='HB7001')
plt.plot(range(1,34),[0.1130,    0.1140,    0.1370,    0.1430,    0.1500,    0.1520,    0.1670,    0.1680,    0.1820,    0.1850,    0.1960,    0.1980,    0.2050,    0.2220,    0.2550,    0.2730,    0.2740,    0.2760,    0.3350,    0.3410,    0.3800,    0.4430,    0.4680,    0.4740,    0.5140,    0.5340,    0.5440,    0.5510,    0.5530,    0.5640,    0.5860,    0.6000,    0.6180]
, 'o', color='gray', label='HB7002')
plt.plot(range(1,34), [0.1130,    0.1140,    0.1370,    0.1430,    0.1500,    0.1520,    0.1670,    0.1680,    0.1820,    0.1850,    0.1960,    0.1980,    0.2050,    0.2310,    0.2550,    0.2730,    0.2760,    0.2920,    0.3350,    0.3410,    0.3800,   0.4430,    0.4680,    0.4740,    0.5140,    0.5340,    0.5440,   0.5510,    0.5530,    0.5640,    0.5730,    0.5860,    0.6180]
, 'o', color = 'gray', label='HB7002SUB')
plt.plot(range(1,34), [0.1360,    0.1370,    0.1480,    0.1510,    0.1530,    0.1570,    0.1590,    0.1640,    0.1650,    0.2020,    0.2060,    0.2100,    0.2100,    0.2370,    0.2620,    0.2720,    0.2780,    0.2820,    0.2970,    0.3350,    0.4680,    0.4740,    0.4840,    0.4940,    0.5140,    0.5180,    0.5220,    0.5270,    0.5290,    0.5350,    0.5450,    0.5540,    0.5730]
, 'o', color = 'gray', label='HB7003')
plt.plot([0,34], [.55, .55], 'g')
plt.plot([0,34], [.37, .37], 'g')

plt.title("BVAP%")
plt.legend()
plt.savefig(newdir+"bvapbox9999gb.png")
fig = plt.gcf()
fig.set_size_inches((11,8.5), forward=False)
fig.savefig(newdir+"bvapbox99992gb.png", dpi=500)

plt.close()
a=None



# a=np.zeros([max_steps,33])
#
# for t in ts:
# 	temp=np.loadtxt(datadir+"bpop"+str(t)+".csv", delimiter=',')
# 	a[t-step_size:t,:]=temp
#
# plt.boxplot(a,whis=[10,90])
# plt.plot(range(1,34), a[0,:], 'ro')
# plt.plot([0,32], [.55, .55], 'g')
# plt.plot([0,32], [.37, .37], 'g')
#
# plt.title("BPOP%")
# plt.savefig(newdir+"bpopbox.png")
# fig = plt.gcf()
# fig.set_size_inches((11,8.5), forward=False)
# fig.savefig(newdir+"bpopbox2.png", dpi=500)
#
# plt.close()
a=None

# a=np.zeros([max_steps,33])
#
# for t in ts:
# 	 temp=np.loadtxt(datadir+"pop"+str(t)+".csv", delimiter=',')
# 	 a[t-step_size:t,:]=temp
#
# plt.boxplot(a,whis=[.1,99.9])
# plt.plot(range(1,34), a[0,:], 'ro')
#  #plt.plot([0,32], [.55, .55], 'g')
#  #plt.plot([0,32], [.37, .37], 'g')
#
# plt.title("Population")
# plt.savefig(newdir+"popbox.png")
# fig = plt.gcf()
# fig.set_size_inches((11,8.5), forward=False)
# fig.savefig(newdir+"popbox2.png", dpi=500)
#
# plt.close()
#
#
#
#
# plt.plot(a[:,32])
# plt.plot([0,max_steps],[a[0,32],a[0,32]],color='r')
#
# plt.title("Largest Population")
# plt.savefig(newdir+"lgpop.png")
# plt.close()
#
#
# plt.hist(a[:,32])
# plt.title("Largest Population")
# plt.axvline(x=a[0,32],color='r')
# plt.savefig(newdir+"lgpophist.png")
# plt.close()
#
# plt.plot(a[:,0])
# plt.plot([0,max_steps],[a[0,0],a[0,0]],color='r')
#
# plt.title("Smallest Population")
# plt.savefig(newdir+"smpop.png")
# plt.close()
#
#
# plt.hist(a[:,0])
# plt.title("Smallest Population")
# plt.axvline(x=a[0,0],color='r')
# plt.savefig(newdir+"smpophist.png")
# plt.close()
#
#
# a=None
# a= np.zeros([max_steps,3])
#
# for t in ts:
# 	temp=np.loadtxt(datadir+"bvaptriple"+str(t)+".csv", delimiter=',')
# 	a[t-step_size:t,:]=temp
#
#
# plt.boxplot(a,whis=[10,90])
# plt.plot([1,2,3],a[0,:],'ro')
#
# plt.title("BVAP Thirdians")
#
# plt.savefig(newdir+"bvapthirds.png")
# fig = plt.gcf()
# fig.set_size_inches((8.5, 11), forward=False)
# fig.savefig(newdir+"bvapthirds2.png", dpi=500)
#
# plt.close()
#
# a=None
#
# a= np.zeros([max_steps,3])
#
# for t in ts:
# 	temp=np.loadtxt(datadir+"bpoptriple"+str(t)+".csv", delimiter=',')
# 	a[t-step_size:t,:]=temp
#
#
# plt.boxplot(a,whis=[10,90])
# plt.plot([1,2,3],a[0,:],'ro')
#
# plt.title("BPOP Thirdians")
#
# plt.savefig(newdir+"bpopthirds.png")
# fig = plt.gcf()
# fig.set_size_inches((8.5, 11), forward=False)
# fig.savefig(newdir+"bpopthirds2.png", dpi=500)
#
# plt.close()
#
#
#

a=None
#
# a=np.zeros([max_steps,33])
#
# for t in ts:
# 	temp=np.loadtxt(datadir+"bvap"+str(t)+".csv", delimiter=',')
# 	a[t-step_size:t,:]=temp
#
# medians = np.median(a, axis=0)
#
# l2s=[]
# l1s=[]
#
# for i in range(max_steps):
# 	l2s.append(np.linalg.norm(a[i,:]-medians))
# 	temp=0
# 	for j in range(33):
# 		temp+=abs(a[i,j]-medians[j])
# 	l1s.append(temp)
#
# plt.plot(l2s)
# plt.plot([0,max_steps],[l2s[0],l2s[0]],color='r')
# plt.title("BVAP% L2 Deviation")
# plt.savefig(newdir+"bvapl2trace.png")
# plt.close()
#
# plt.plot(l1s)
# plt.plot([0,max_steps],[l1s[0],l1s[0]],color='r')
# plt.title("BVAP% L1 Deviation")
# plt.savefig(newdir+"bvapl1trace.png")
# plt.close()
#
# plt.hist(l2s,bins=1000)
# plt.axvline(x=np.linalg.norm(np.array(a[0,:])-medians),color='r')
#
# plt.title("BVAP% L2 Deviation")
# plt.savefig(newdir+"bvapl2.png")
# fig = plt.gcf()
# fig.set_size_inches((11,8.5), forward=False)
# fig.savefig(newdir+"bvapl22.png", dpi=500)
#
# plt.close()
#
# plt.hist(l1s,bins=1000)
# plt.axvline(x=sum([abs(a[0,x]-medians[x]) for x in range(33)]),color='r')
#
# plt.title("BVAP% L1 Deviation")
# plt.savefig(newdir+"bvapl1.png")
# fig = plt.gcf()
# fig.set_size_inches((11,8.5), forward=False)
# fig.savefig(newdir+"bvapl12.png", dpi=500)
#
# plt.close()
#
# l2sa=np.array(l2s)
#
# import seaborn as sns
#
# sns.set_style('darkgrid')
# sns.distplot(l2sa)
# plt.axvline(x=sum([abs(a[0,x]-medians[x]) for x in range(33)]),color='r')
#
# plt.show()
#
#
#
# a=None
#
# a=np.zeros([max_steps,33])
#
# for t in ts:
# 	temp=np.loadtxt(datadir+"bpop"+str(t)+".csv", delimiter=',')
# 	a[t-step_size:t,:]=temp
#
# medians = np.median(a, axis=0)
#
# l2s=[]
# l1s=[]
#
# for i in range(max_steps):
# 	l2s.append(np.linalg.norm(a[i,:]-medians))
# 	temp=0
# 	for j in range(33):
# 		temp+=abs(a[i,j]-medians[j])
# 	l1s.append(temp)
#
# plt.plot(l2s)
# plt.plot([0,max_steps],[l2s[0],l2s[0]],color='r')
# plt.title("BPOP% L2 Deviation")
# plt.savefig(newdir+"bpopl2trace.png")
# plt.close()
#
# plt.plot(l1s)
# plt.plot([0,max_steps],[l1s[0],l1s[0]],color='r')
# plt.title("BPOP% L1 Deviation")
# plt.savefig(newdir+"bpopl1trace.png")
# plt.close()
# plt.hist(l2s,bins=1000)
# plt.axvline(x=np.linalg.norm(np.array(a[0,:])-medians),color='r')
#
# plt.title("BPOP% L2 Deviation")
# plt.savefig(newdir+"bpopl2.png")
# fig = plt.gcf()
# fig.set_size_inches((11,8.5), forward=False)
# fig.savefig(newdir+"bpopl22.png", dpi=500)
#
# plt.close()
#
# plt.hist(l1s,bins=1000)
# plt.axvline(x=sum([abs(a[0,x]-medians[x]) for x in range(33)]),color='r')
#
# plt.title("BPOP% L1 Deviation")
# plt.savefig(newdir+"bpopl1.png")
# fig = plt.gcf()
# fig.set_size_inches((11,8.5), forward=False)
# fig.savefig(newdir+"bpopl12.png", dpi=500)
#
# plt.close()

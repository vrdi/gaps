# Import for I/O

import os
import random
import json
import geopandas as gp
import pandas as pd
import functools
import datetime
import matplotlib.pyplot as plt
import numpy as np
import csv
from networkx.readwrite import json_graph

# Imports for RunDMCMC components
# You can look at the list of available functions in each
# corresponding .py file.

from tree_proposal_VA_MUNI import *

from rundmcmc.accept import always_accept

from rundmcmc.chain import MarkovChain

from rundmcmc.make_graph import (construct_graph,
                                 get_assignment_dict_from_graph,add_data_to_graph)

from rundmcmc.partition import Partition

from rundmcmc.proposals import propose_random_flip

from rundmcmc.updaters import (Tally, boundary_nodes, cut_edges,
                               cut_edges_by_part, exterior_boundaries,
                               perimeters, polsby_popper,
                               votes_updaters,
                               interior_boundaries,
                               CountySplit,county_splits)

from rundmcmc.validity import (L_minus_1_polsby_popper,
                               L1_reciprocal_polsby_popper,
                               Validator, single_flip_contiguous,
                               within_percent_of_ideal_population,
                               SelfConfiguringLowerBound,
                               LowerBound, UpperBound, refuse_new_splits,
							   non_bool_where, proposed_changes_still_contiguous)

from rundmcmc.scores import (efficiency_gap, mean_median,
                             mean_thirdian, how_many_seats_value,
                             number_cut_edges, worst_pop,
                             L2_pop_dev,
                             worst_pp, best_pp,
                             node_flipped, flipped_to, bvap_vector)

from rundmcmc.output import (p_value_report, hist_of_table_scores,
                             trace_of_table_scores, pipe_to_table)


# Here is where you have to input a few things again

# Set Random Seed
random.seed(1769) #1852) #1769) #1861

# Type the name of your state
state_name = "VA_MUNI_ALL_CON_Neutral" #

# Input the path to the JSON graph and the GEOJSON for plotting
graph_path = "./Outputs/VA_MUNI_SEEDS/VA_PREC_ALL.json"
plot_path = "./Data/VA_MUNI/va_precincts_all.shp"
cd_path = "./Outputs/VA_MUNI_SEEDS/VA_PREC_ALL1_CON.json"

# Names of graph columns go here
unique_label = "id"
pop_col = "TOTPOP"
#district_col = "TREE"
#county_col =  "COUNTYFP10"
#area_col = "areas"

def num_splits(partition):

    df["current"] = df.index.map(partition.assignment)
    splits = sum(df.groupby('locality')['current'].nunique() >1)
    #print("current" in df.columns)
    #df = df.drop("current",1)
    
    return splits
    
    
def split_accept(partition):
    
    bound = 1
    if partition.parent is not None:
        if num_splits(partition) > num_splits(partition.parent):
            bound = 0 
            
    return random.random() < bound

def R_accept(partition):
    
    bound = 1
    if partition.parent is not None:
        if how_many_seats_value(partition, col1="G17RATG", col2="G17DATG") < how_many_seats_value(partition.parent, col1="G17RATG",col2="G17DATG"):
            bound = 0 
        
        #bound = min(1, (how_many_seats_value(partition, col1="G17RATG",
         #col2="G17DATG")/how_many_seats_value(partition.parent, col1="G17RATG",
         #col2="G17DATG"))**2  ) #for some states/elections probably want to add 1 to denominator so you don't divide by zero


    return random.random() < bound
    
    
def D_accept(partition):
    
    bound = 1
    if partition.parent is not None:
        if how_many_seats_value(partition, col1="G17DATG", col2="G17RATG") < how_many_seats_value(partition.parent, col1="G17DATG",col2="G17RATG"):
            bound = 0 
        
        #bound = min(1, (how_many_seats_value(partition, col1="G17RATG",
         #col2="G17DATG")/how_many_seats_value(partition.parent, col1="G17RATG",
         #col2="G17DATG"))**2  ) #for some states/elections probably want to add 1 to denominator so you don't divide by zero


    return random.random() < bound


# Type the number of elections here


# Type the names of the elections here
num_elections = 7
election_names= ["DLSBVAP","DOJBVAP","SEN18","GOV18","LTG17","ATG17","PRS16"]
election_columns=[["DLS_BVAP","DLS_NONB"],["DOJ_BVAP","DOJ_NONB"],["G18DSEN","G18RSEN"],
["G17DGOV","G17RGOV"],["G17DLTG","G17RLTG"],["G17DATG","G17RATG"],["G16DPRS","G16RPRS"]]


# Choose a proposal from proposals.py
proposal_method = propose_merge2_tree#merge_mixed_proposal#propose_random_flip#propose_random_flip

# Choose an acceptance method from accept.py
acceptance_method = always_accept#always_accept#D_accept#split_accept

# Choose how many steps to run the chain
steps = 100000


# That was (almost) everything!
# The code below constructs and runs the Markov chain
# You may want to adjust the binary constraints -
# they are located below in the section labelled ``Validators''


# Make a folder for the output
current = datetime.datetime.now()
newdir = "./Outputs/VA_MUNI/for_UVA/" + state_name + "_merge/"

os.makedirs(os.path.dirname(newdir + "init.txt"), exist_ok=True)
with open(newdir + "init.txt", "w") as f:
    f.write("Created Folder")


# This builds a graph
graph = construct_graph(graph_path, id_col=unique_label, 
                        pop_col=pop_col, #district_col=district_col,
                        data_cols=[] + [cols for pair in election_columns for cols in pair],
                        data_source_type="json") #fiona



df = gp.read_file(plot_path)


with open(newdir+'VA_MUNI.json', 'w') as outfile:
    json.dump(json_graph.adjacency_data(graph), outfile)

print("saved_graph")

# Get assignment dictionary
with open(cd_path) as f:
    assignment = json.load(f)
    



# Necessary updaters go here
updaters = {'population': Tally('population'),
  #          'perimeters': perimeters,
            'exterior_boundaries': exterior_boundaries,
            'interior_boundaries': interior_boundaries,
            'boundary_nodes': boundary_nodes,
            'cut_edges': cut_edges,
 #           'areas': Tally('areas'),
  #          'polsby_popper': polsby_popper,
            'cut_edges_by_part': cut_edges_by_part,
   #         'County_Splits': county_splits('County_Splits',county_col)
   }


# Add the vote updaters for multiple plans
for i in range(num_elections):
    updaters = {**updaters, **votes_updaters(election_columns[i], election_names[i])}


print(assignment['518'])
for node in graph.nodes():
    if node == '518':
        print("hooray")

for i in list(assignment.keys()):
    assignment[int(i)]=assignment[i]
    assignment.pop(i)

# This builds the partition object
initial_partition = Partition(graph, assignment, updaters)



# Choose which binary constraints to enforce
# Options are in validity.py

#non_bool_where(initial_partition)
print(bvap_vector(initial_partition, "population"))
pop_limit = .02#was .1 for enacted and non congressional
population_constraint = within_percent_of_ideal_population(initial_partition, pop_limit)


edge_constraint = UpperBound(number_cut_edges, 3*len(initial_partition["cut_edges"]))

#county_constraint = refuse_new_splits("County_Splits")

validator = Validator([population_constraint])#,county_constraint])#edge_constraint])
#Validator([])#

#validator = Validator([single_flip_contiguous, population_constraint,
#                       edge_constraint])#,county_constraint])#edge_constraint])

# Names of validators for output
# Necessary since bounds don't have __name__'s
list_of_validators = [number_cut_edges,population_constraint]

# Geojson for plotting
#df_plot = gp.read_file(plot_path)
#df_plot["NCD"]=df["NCD"]
#df_plot["initial"] = df_plot[unique_label].map(assignment)
#df_plot.plot(column="initial", cmap='tab20')
#plt.axis('off')
#plt.savefig(newdir + district_col + "_initial.png")
#plt.close()

print("setup chain")

# This builds the chain object for us to iterate over
chain = MarkovChain(proposal_method, validator, acceptance_method,
                    initial_partition, total_steps=steps)

print("built chain")

bvap_vec=[]
bpop_vec=[]
pop_vec=[]
cut_vec=[]
bvap_triple = []
bpop_triple = []
mmg=[]
mmlg=[]
mmag=[]
mmp=[]
egg=[]
eglg=[]
egag=[]
egp=[]


#print(initial_partition["VABVAP%"])


num_dists=len(initial_partition["DLS_BVAP"])

#plt.close()




initial_cut = len(initial_partition["cut_edges"])
#initial_votes = bvap_vector(initial_partition,"ATG12D")
initial_pop = bvap_vector(initial_partition, "population")
initial_assignment = assignment.copy()


with open(newdir + "Start_Values.txt", "w") as f:
    f.write("Values for Starting Plan: RECURSIVE TREE \n\n")
    f.write("Initial Cut: "+ str(initial_cut))
    f.write("\n")
    f.write("\n")
    f.write("Inital Pop: "+ str(initial_pop))
    f.write("\n")
    f.write("\n")
    for elect in range(num_elections):
        f.write(election_names[elect] + "District Percentages" + str(bvap_vector(initial_partition,election_columns[elect][0]+"%")))
        f.write("\n")
        f.write("\n")

        f.write(election_names[elect] + "Mean-Median :"+ str(mean_median(initial_partition, election_columns[elect][0]+"%")))
        
        f.write("\n")
        f.write("\n")
        
        f.write(election_names[elect] + "Efficiency Gap :" + str(efficiency_gap(initial_partition, col1=election_columns[elect][0],
         col2=election_columns[elect][1])))
        
        f.write("\n")
        f.write("\n")
        
        f.write(election_names[elect] + "How Many Seats :" + str(how_many_seats_value(initial_partition, col1=election_columns[elect][0],
         col2=election_columns[elect][1])))
         
        f.write("\n")
        f.write("\n")
        
    

votes=[[] for x in range(num_elections)]
mms=[]
egs=[]
hmss=[]
split_vec = []

print("finished_initial_plot")
#p = plt.plot(range(num_dists), initial_bvap, 'ro')

#print(initial_bvap)
t=0
count=0
df=gp.read_file(plot_path)
df["START"]=df.index.map(assignment)

df.plot(column="START",cmap="tab20")

plt.savefig(newdir+"initial_plot.png")

plt.close()

for part in chain:


    pop_vec.append(bvap_vector(part,"population"))
    cut_vec.append(len(part["cut_edges"]))
    split_vec.append(num_splits(part))
    mms.append([])
    egs.append([])
    hmss.append([])

    for elect in range(num_elections):
        votes[elect].append(bvap_vector(part,election_columns[elect][0]+"%"))
        mms[-1].append(mean_median(part, election_columns[elect][0]+"%"))
        egs[-1].append(efficiency_gap(part, col1=election_columns[elect][0],
         col2=election_columns[elect][1]))
        hmss[-1].append(how_many_seats_value(part, col1=election_columns[elect][0],
         col2=election_columns[elect][1]))
        
    t+=1
    if t%2000==0:
        print(t)
        with open(newdir+"mms"+str(t)+".csv",'w') as tf1:
            writer = csv.writer(tf1,lineterminator="\n")
            writer.writerows(mms)
			
        with open(newdir+"egs"+str(t)+".csv",'w') as tf1:
            writer = csv.writer(tf1,lineterminator="\n")
            writer.writerows(egs)
			
        with open(newdir+"hmss"+str(t)+".csv",'w') as tf1:
            writer = csv.writer(tf1,lineterminator="\n")
            writer.writerows(hmss)
			
        with open(newdir+"pop"+str(t)+".csv",'w') as tf1:
            writer = csv.writer(tf1,lineterminator="\n")
            writer.writerows(pop_vec)
	
        with open(newdir+"cuts"+str(t)+".csv",'w') as tf1:
            writer = csv.writer(tf1,lineterminator="\n")
            writer.writerows([cut_vec])
            
        with open(newdir+"splits"+str(t)+".csv",'w') as tf1:
            writer = csv.writer(tf1,lineterminator="\n")
            writer.writerows([split_vec])

        with open(newdir+"assignment"+str(t)+".json", 'w') as jf1:
            json.dump(part.assignment, jf1)
			
			
        for elect in range(num_elections):
            with open(newdir+election_names[elect]+"_"+str(t)+".csv",'w') as tf1:
                writer = csv.writer(tf1,lineterminator="\n")
                writer.writerows(votes[elect])

        df["plot"+str(t)]=df.index.map(part.assignment)
        df.plot(column="plot"+str(t),cmap="tab20")
        plt.savefig(newdir+"plot"+str(t)+".png")
        plt.close()		    

        votes=[[] for x in range(num_elections)]
        mms=[]
        egs=[]
        hmss=[]
        pop_vec=[]
        cut_vec=[]
        split_vec=[]

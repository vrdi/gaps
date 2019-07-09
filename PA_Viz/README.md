# Visualization Data for MCMC runs on PA precincts

This repo contains a small snapshot of ensemble data for the state of Pennsylvania for testing visualization techniques. There is one 100k step ensembles presented here, for the eighteen Congressional districts. For each ensemble we have recorded a variety of metrics for each plan, described in more detail below. The ensembles were generated with the GerryChain software: <https://github.com/mggg/gerrychain>. Precinct data was gathered by MGGG project: <https://github.com/mggg-states/Wisconsin> and preprocessed with <https://github.com/mggg/maup>. 

The procedure for generating the data was to form a Markov chain on the set of districting partitions of Pennsylvania precincts using the Recombination step described here: <https://mggg.org/VA-report.pdf>. At each step of the chain (i.e. each obsevered districting plan) the statistics described below were measured and every 2000 steps the full set of observations was written to file. Thus, the data files are indexed by 2000*t where t runs from 1 to 50. 

The metrics are separated into three main categories:

1. **Global plan metrics**

   These statistics are properties of the entire plan at once. Each file contains a comma separated list of values describing the property of the current plan in the ensemble. 

  * **cuts**: Number of cut edges between the districts in the current plan

2. **Partisan Metrics**

   The full state partisan metrics are reported by election for each plan. Thus, each file consists of a collection of rows of five comma separated entries, one for each of the elections described below. 

  * **egs**: Efficiency Gap of the current plan
  * **mms**: Mean-Median of the current plan
  * **hmss**: # of seats won by the Dem party in the current plan

3. **District statistics**

   The statistics presented at the district level are arranged into rows of k comma separated values, where k is the number of districts in the plan (11 for Congress and 40 for the Senate). The values in each entry for the election data are the expected percentage of Democratic vote share in each district while the values in the population files are the number of individuals who live in each district
  * **ATG12**: 2012 Attorney General Election
  * **ATG16**: 2016 Attorney General Election 
  * **GOV10**: 2012 Gubenatorial Election
  * **GOV14**: 2012 Gubenatorial Election
  * **PRES12**: 2012 Presidential Election
  * **PRES16**: 2016 Presidential Election
  * **SEN10**: 2010 US Senate Election
  * **SEN12**: 2012 Senatorial Election
  * **SEN16**: 2016 Senatorial Election
  * **SENW1012**: Turnout weighted combination of 2010 and 2012 Senate Elections
  * **SENW1016**: Turnout weighted combination of 2010 and 2016 Senate Elections
  * **SENW1216**: Turnout weighted combination of 2012 and 2016 Senate Elections
  * **SENW101216**: Turnout weighted combination of 2010, 2012, and 2016 Senate Elections

  * **pop**: Population of each district in the plan


In addition to the metrics, there are also **assignment** files which are .json dictionaries mapping the precinct labels to their district number for each snapshot of the ensemble and a collection of **.pngs** showing colorful maps of the snapshot plans. 

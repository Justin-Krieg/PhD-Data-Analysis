# Radial Arm Maze Analysis
Author: Justin Krieg
Year: 2023

## About
This script is based off of analysis done on the radial arm maze. Here animals are placed in a large decagon with 10 arms protruding from it. Each arm was labelled 0-9 and had a reward in it. There were two arms however that lacked the reward and were labelled as non-baited arm 1 and 2. The sequence of entries was manually recorded for each subject across each trial. __ie. 018374829475638__. This happened over the course of a 3 minute period. Data was collated into a CSV file as below.

| Animal\_ID | Trial | Sequence | Non\_Baited\_Arm\_1 | Non\_Baited\_Arm\_2 |
| :--- | :--- | :--- | :--- | :--- |
| JK064 | T1 | 268405124836702145 | 4 | 0 |
| JK057 | T5 | 61738269405 | 6 | 4 |
| JK082 | T1 | 8927105308518674 | 3 | 6 |
| JK082 | T2 | 89748185250 | 3 | 6 |
| JK071 | T4 | 1865075169408327139 | 2 | 5 |
| JK055 | T5 | 8424196730375 | 1 | 6 |
| JK071 | T2 | 82737283827109640615 | 2 | 5 |
| JK080 | T4 | 639140735290121 | 6 | 0 |
| JK069 | T4 | 607154810895420 | 5 | 9 |
| JK059 | T4 | 1520838492 | 1 | 9 |

The script provided here processes the sequence and looks for various parameters:
**Total Arms**: The total number of arms entered.
**Working memory errors**: The total number of times an animal re-enters an arm. This is calculated by the counting any numbers that appear more than once. 
**Reference memory errors**: The total number of times an animal enters once of the arms in the non-baited arms column
**Best reference memory**: The highest count of numbers inbetween two reference memory errors (entering a non baited arm)
**Best working memory**: Similarly, the highest count of numbers between two working memory errors. 
**Best xx memory %**: Standardising these measures to the total number of arms entered
Best xx %**: Standardising working and reference memory errors to the total arms entered.

These parameters were based on the work done in this study:
> Tarantino IS, Sharp RF, Geyer MA, et al. Working memory span capacity improved by a D2 but not D1 receptor family agonist. Behav Brain Res 2011;219(2):181–188; doi: 10.1016/j.bbr.2010.12.037.


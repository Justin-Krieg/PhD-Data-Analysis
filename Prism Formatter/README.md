# MySQL to Prism
Author: Justin Krieg
Year: 2023

## About
This script was inspired by graphpad prisms unusual means of storing data. Here each subject is stored as a column, and experimental groups are seperated by X number of columns. This makes transposition errors easy through the paste transpose function, particularly with uneven group numbers and missing data. Rows are also added as different timepoints or regions of interest, often requiring to be stacked to allow for repeated measures. This script aimed to transform data into a prism ready format.


Consider this data format:
| Animal\_ID | Animal\_Group | ROI | Fractional\_Anisotrophy | Axial\_Diffusivity |
| :--- | :--- | :--- | :--- | :--- |
| JK051 | 22J | Hypothalamus | 0.20028 | 0.13528 |
| JK051 | 22J | Internal Capsule | 0.5648 | 0.14004 |
| JK051 | 22J | Hippo | 0.17979 | 0.16608 |
| JK051 | 22J | Thalamus | 0.24454 | 0.16964 |
| JK058 | Sham | Hypothalamus | 0.21806 | 0.17987 |
| JK048 | Sham | Hypothalamus | 0.22129 | 0.18143 |
| JK049 | 22J | Hypothalamus | 0.20249 | 0.1886 |
| JK077 | 22J | Hypothalamus | 0.22793 | 0.19226 |
| JK067 | 22J | Hypothalamus | 0.24415 | 0.19298 |
| JK058 | Sham | Internal Capsule | 0.64206 | 0.1994 |


Here we have an individual subject as Animal_ID, experienmental groups as Animal_Group, Animal_Study as different timepoints and a few MRI parameters. The desired output is to have a new data table for each of these MRI parameters. Here we can point the script to a CSV output of our mySQL query and set our parameters for group_factor, subject and row factor accordingly.

This will output two new files: Fractional Anisotrophy.csv and Axial Diffusivity.csv. These will contain the data formatted appropriate for Prism's Grouped data table:
|                       | 22J     | 22J     | 22J     | 22J     | 22J     | 22J     | 22J     | Sham    | Sham    | Sham    | Sham    | Sham    | Sham | Sham |
|-----------------------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|------|------|
|                       | JK049   | JK051   | JK061   | JK067   | JK073   | JK076   | JK077   | JK048   | JK058   | JK065   | JK072   | JK079   | nan  | nan  |
| Caudate               | 0.25186 | 0.21785 | 0.26878 | 0.23212 | 0.26562 | 0.2562  | 0.24371 | 0.2322  | 0.28151 | 0.26457 | 0.25881 | 0.2651  |      |      |
| Cingulum              | 0.33428 | 0.26553 | 0.32656 | 0.32034 | 0.34007 | 0.31379 | 0.31989 | 0.30542 | 0.33346 | 0.34027 | 0.33323 | 0.32609 |      |      |
| Corpus Callosum       | 0.27733 | 0.20552 | 0.32289 | 0.274   | 0.30802 | 0.31831 | 0.24984 | 0.26214 | 0.37136 | 0.3052  | 0.31408 | 0.30841 |      |      |
| Cortical White Matter | 0.26996 | 0.21426 | 0.27559 | 0.26693 | 0.29107 | 0.26264 | 0.26904 | 0.24884 | 0.27838 | 0.27298 | 0.28799 | 0.27185 |      |      |
| Fornix                | 0.32019 | 0.25574 | 0.36451 | 0.29796 | 0.34832 | 0.4119  | 0.36187 | 0.30137 | 0.49905 | 0.33464 | 0.36303 | 0.34944 |      |      |

Note the nan's on the sham group, used to keep all experimental groups balanced. It is recommended to turn off the "Enter one set of subcolumn titles for all datasets" option in prism to ensure all subject ID's are properly displayed. 



# VALIS Implementation
Author: Justin Krieg
Year: 2023/2024

## Background
This script is a custom implementation of the excellent work done by @mathonco with their software package VALIS. This is a custom implementation of their package to run VALIS in series with a large dataset of images. 

## Impelmentation
Four files are used to interface with VALIS. “File.txt” has a list of all the sections identifications that requires stitching. The second is a CSV file (“setup.csv”) which contains a column for each round in the mIF panel and each row as the channel name for each round. Here you would define exactly how each channel should be labelled in order of scanning, ie. 488nm, 555nm then 647nm or according to scanner program output. The header of each column should implement the naming scheme used in the folder to delineate the various rounds. Here the string “{Image_ID}” acts as a placeholder for any section identification within the “files.txt” file. Hence {Image_ID}_R1.czi with the section identification of Animal_1 would be interpolated as Animal_1_R1.czi. This ultimately provides flexibility with naming schemes. Next the “init.py” should be modified to direct VALIS to the folder with all the images in it and run in a python instance to begin stitching images. The final script (Runner.py) runs each VALIS instance, interpolating file names from the ‘file.txt’ (Script 1) and ‘setup.csv’, defining the channel names and implementing VALIS itself. This outputs an OME-TIFF file. This new file is still significantly larger than the sum of all the input files as this compression is not as efficient as the proprietary CZI compression. Hence to combat this, the new file does not contain repeated DAPI channels.

### Notes
Please see file.txt and setup.csv which is already populated with data. This was last tested on version 1.0.4 of VALIS. 

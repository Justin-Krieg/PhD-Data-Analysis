import pandas as pd
import numpy as np
import os
from valis import registration, valtils, slide_io
import shutil
import argparse
import os
"""
Author: Justin Krieg
Year: 2023/2024
Working with Valis 1.0.4
Init.py. This python script is meant to be run by the user. This script requires one variable change: Slide directory, which must be set to the location where the scans are being stored on the user’s computer. This script reads all the necessary files and passes variables to the final runner.py. This method allows for valis to be run as an independent python session meaning the stitching process can continue if one section fails. 
"""

# Create an argument parser
parser = argparse.ArgumentParser(description="Script to run Valis")
parser.add_argument("name_list_0", type=str, help="Value from column 0")
parser.add_argument("slide_src_dir", type=str, help="Value from column 1")

args = parser.parse_args()
name_list = args.name_list_0
slide_src_dir = os.path.abspath(args.slide_src_dir)

# Set up variables
csv_file = os.path.join(slide_src_dir, "setup.csv")
df = pd.read_csv(csv_file)
df.columns = [header.replace('{Image_ID}', f'{name_list}') for header in df.columns]
channel_name_dict_defined = df.replace({np.nan: None}).to_dict(orient='list')

# Filter out 'None' values from the lists in the dictionary
channel_name_dict_defined = {k: [item for item in v if item is not None] for k, v in channel_name_dict_defined.items()}

print(channel_name_dict_defined)

img_list = df.columns.tolist()
img_list_path = [os.path.join(slide_src_dir, ls) for ls in img_list]
name_list_Stitched = os.path.join(slide_src_dir, f"{name_list}.3Rounds.test2.stitched.ome.tiff")
results_dir = os.path.join (slide_src_dir,"output", name_list, "")
print(results_dir)
# Run Valis
registrar = registration.Valis(slide_src_dir,  results_dir, img_list = img_list_path, crop="overlap", series=0)

rigid_registrar, non_rigid_registrar, error_df = registrar.register()
registrar.register_micro(max_non_rigid_registration_dim_px=2000)
registrar.warp_and_merge_slides(name_list_Stitched, channel_name_dict=channel_name_dict_defined, drop_duplicates=True, compression="lzw", Q=85)

"""
try:
    shutil.rmtree(results_dir)
except Exception as e:
    print(name_list + ": Error removing files")
"""
import pandas as pd
from valis import registration
import os
import subprocess

"""
Author: Justin Krieg
Year: 2023/2024
Working with Valis 1.0.4
Runner.py is the individual instance of VALIS that runs the stitching. This reads the setup.csv file, interpolates the filename, generates the channel name list to pass to VALIS and runs the stitching process. It then removes any analysis files. 
"""


# Set this to where the slide files are located, along with the file.txt and setup.csv. MUST USE forward slashes / not backslashes \
Slide_Directory = "B:/R1R3/"

# Intial variables and paths

slide_src_dir = os.path.abspath(Slide_Directory)
if os.path.exists(slide_src_dir) and os.path.isdir(slide_src_dir):
    file_txt_dir = os.path.join(slide_src_dir, "file.txt")
    setup_csv = os.path.join(slide_src_dir, "setup.csv")
    runner_path = os.path.join (os.path.dirname(__file__), "Runner.py")
    # Check files exist
    if os.path.exists(runner_path):
        if os.path.exists(file_txt_dir) and os.path.exists(setup_csv):
            if __name__ == '__main__':
                with open(file_txt_dir, "r") as file:
                    values = file.readlines()
                # run for loop for each line in the file.txt
                for row in values:
                    row = row.strip()
                    valis_command = ["python", runner_path, row, slide_src_dir]
                    print(valis_command)
                    # run Runner.py for this row value
                    try:
                        subprocess.run(valis_command, check=True)
                    except subprocess.CalledProcessError as e:
                        print("Valis process returned an error")
                        continue
                # Valis Cleanup
                registration.kill_jvm()
        else:
            print("Missing either File.txt or setup.csv in slide dir")
    else:
        print("Missing Runner.py")
else:
    print("Slide Source Directory does not exist!")

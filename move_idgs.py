##----purpose of this script is to walk into each pyrome folder for the 2022 National FSim runs and extract all of the IDGs
import os
import shutil

# input folder
fsim_inputs = r"C:\Users\Charlie\Desktop\ArcGIS\data\NatFSim\NatFSim2022\FinalRuns"
# output folder
idg_outputs = r"C:\Users\Charlie\Desktop\ArcGIS\data\NatFSim\NatFSim2022\FSim_inputs\idg"
#print(fsim_inputs)

# walk through folders and extract all ignition density tifs
idgs = [
    os.path.join(root, file)
    for root, dirs, files in os.walk(fsim_inputs, topdown=True)
    for file in files
    if "idg" in file
]

# copy files to the IDG outputs folder
for file_path in idgs:
    shutil.copy(file_path, idg_outputs)
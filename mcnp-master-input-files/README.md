# MCNP master input files
***
Because the geometry is very complex and there are a lot  of surfaces included, scripts are needed to compute all the positions; e.g., location of the pipes, thickness of the gap, lattice size, etc. These are found in the scripts repository. 

Files in the archive directory were the original input files created by Seth Dustin. These just had the fuel as a block, surrounded by the cooling plates and welds. This model was limited to two cooling loops per plate. 

The current directory contains the cask designs used for the IGEM cask modeling and simulation. The fuel is modeled as an  assembly (lattice) surrounded by a gas gap; air, He, etc. This increases the length, width of the cooling plates. This master file does not include material cards for used fuel and boron-loading.

The corresponding scripts compute all the positions of the surfaces and accounts for the addition of cooling pipes per plate. Use the script file to make changes to the geometry. It will produce an output file with the surface IDs, types, and positions. If geometry changes are made, make a new master file and include it here. 

Do NOT edit the master input files in this directory once the geometry has been computed. Copy them to the simulation directories and add the material cards for the specific problem.

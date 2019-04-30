These are the master MCNP input files for the cask design.

Parent directory is plate thickness.  
Add more parent directories for new plate thickness. 

Subdirectories are concrete container thickness. 

In the plate thickness folder

If there is a new wt% of B10 or B4C add them to the files here and just comment out. 

If there is new material to add except for used fuel then add here and comment out. 

Copy these files to the ZZZZ-burnup/N-XXYY/submaster-inp directory and append the filename to single.assembly_NNNN.inp, where NNNN is the age of the fuel of interest. 

Add the correct fuel material to the files in the submaster-inp directories.

Then, uncomment the B10 M1 card for the desired wt% and uncomment the desired B4C wt% (don't forget cell cards - 10 of them) and copy that file into the appropriate simulation directory. 

See the README there for simulation directory structure. 

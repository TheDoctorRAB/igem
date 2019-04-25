Top level directory is for bare cask and container
---

**Bare cask directory**
Directory MMM - backfill material
Directory XXwt - weight percent of boron 10 in the total boron  
Directory XXwt - weight percent of boron carbide in the aluminum    
Directory NNcm plate thickness

Example - air/5wt/10wt/3cm/inp/mcnpfile  

Read - mcnpfile for 3 cm plate thickness 10wt% boron carbide-90wt% aluminum in the plate with 5wt% boron 10 of the total boron

---

**Container directory**
Directory MMM - backfill material
Directory NNcm - container thickness
Directory XXwt - weight percent of boron 10 in the total boron  
Directory XXwt - weight percent of boron carbide in the aluminum    
Directory NNcm plate thickness

Example - air/5cm/5wt/10wt/3cm/inp/mcnpfile  

Read - mcnpfile for 3 cm plate thickness 10wt% boron carbide-90wt% aluminum in the plate with 5wt% boron 10 of the total boron with a 5cm thick container

---

mkdir for B4C-Al wt% with the bash script

From the material backfill directory, copy the submaster-mcnpfiles to the subdirectories  
The mcnpfile in the submaster-inp directory should have all the cooling plate cell cards and B10wt%/B4C wt% in the materials cards commented out   
So copy the files into the subdirectories and then uncomment the relevant cards

Copy files using echo with the bash script

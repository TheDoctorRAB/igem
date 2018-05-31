########################################################################
# @TheDoctorRAB
########################################################################
# This script edits the surface cards for the igem single assembly cask.
# The number of spaces is important because MCNP is FORTRAN.
########################################################################
#
#
####### imports
from sys import argv
import numpy
script,mcnp_input=argv
#######
#
#######
# inputs and calulations
# units in cm
###
fuel_width=21.318
fuel_length=fuel_width
fuel_height=400
###
gap_thickness=5 #thickness of gap around assembly, also vertical
###
plate_thickness=1.5
plate_width=fuel_width+2*gap_thickness
plate_length=plate_width
plate_height=410
###
torus_height=7.6
pipe_height=plate_height-torus_height #Sakae design constraint
pipe_ID=0.25 #also fluid diameter
pipe_OD=0.30
###
pipe_half_distance=(plate_width-plate_thickness)/8 #halfdistrance between pipes, used for torus radii
pipe_distance=2*pipe_half_distance #distance between pipes
pipe_plane=0.5*plate_thickness #pipe is located in the midplane of the plate
###
# x,y positions on plate where pipes are located
# first position - left to right, bottom to top
# calculate south plate 1, north plate 1; south plate 2, north plate 2, etc.
# then calculate west plate 1, east plate 1, and so on
# the number is the pipe number
###
pipes_per_plate=4
total_plates=4
pipe_position=numpy.zeros((pipes_per_plate*total_plates*2,3)) #factor of 2 because surface is needed for ID and another for OD
###
# DESCRIBE PIPE POSITION
###
for i in range (0,(pipes_per_plate*total_plates*2)):
  if (i%2)==0:
    pipe_position[i,2]=pipe_ID
  else:
    pipe_position[i,2]=pipe_OD

# pipe_1=pipe_half_distance+plate_thickness ###

print 'fuel dimensions',fuel_width,fuel_length,fuel_height
print 'gap',gap_thickness
print 'plate dimensions',plate_thickness,plate_width,plate_length,plate_height
print 'pipe dimensions',pipe_height,pipe_ID,pipe_OD
print 'pipe distance',pipe_distance,pipe_half_distance,pipe_plane
print 'pipe position'
print pipe_position
####### Set up first part of line
#NPS_header='NPS    '
#######
#
####### Get the NPS
#NPS_history=open('nps.inp','r').read()
#######
#
####### Combine the header and history strings
#NPS_new=NPS_header+NPS_history+'\n'
#######
#
####### open mcnp input file
#mcnp_infile=open(mcnp_input,'r')
#######
#
####### Find the original NPS
#for line in mcnp_infile:
#  if 'NPS' in line:
#    NPS_old=line
# endif
# end line
#######
#
####### Close the mcnp input file
#mcnp_infile.close()
#######
#
####### Open the mcnp input file and read
# This is ok because the input files for mcnp are small for memory
#mcnp_tempfile=open(mcnp_input,'r').read()
#######
#
####### Replace the NPS
#mcnp_tempfile=mcnp_tempfile.replace(NPS_old,NPS_new)
#######
#
####### Write the file
#open(mcnp_input,'w').write(mcnp_tempfile)
#######
#
#
########################################################################
#      EOF
########################################################################

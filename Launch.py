#Author: Van Eylen code modified by Prajwal Niraula
#Institution: Wesleyan University
#Last Updated: March 1, 2017


#Aperture system is given by the old van eylen method

from __future__ import division
import matplotlib
matplotlib.use('Qt4Agg')

import os


from run_pipeline import run
from glob import glob
import re

import warnings
warnings.filterwarnings("ignore") #To suppress the warning. Comment this to see the range of warning.


inputpath = '/home/prajwal/Downloads/PhaseCurves/*.fits'
#SubFolder = 'PhaseCurves' #for loading the apertures
outputpath = 'Campaign15'

#Create the folder if it does not exc_list
if not(os.path.exists(outputpath)):
    os.system('mkdir %s' %(outputpath))

filepaths = glob(inputpath)

for FILE in filepaths:
  EPIC_ID = re.search('[0-9]{9}',FILE).group(0)
  print "Now running::",EPIC_ID
  try:
      chunksize = 150
      Campaign = re.search('c[0-9]{2}',FILE).group(0)
      Campaign = str(int(Campaign[1:]))
      run(filepath=FILE,outputpath=outputpath,chunksize=chunksize,method ='SFF')
  except Exception as inst:
      print inst
print 'Completed the task'

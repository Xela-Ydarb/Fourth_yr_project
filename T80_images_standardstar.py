# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# import necessary packages
from astropy import units as u
import ccdproc
from astropy.io import fits
from astropy.nddata import CCDData

# bring the bias frames into python 
bias1 = fits.getdata('C:/Users/abrady/OneDrive - Maynooth University/Thesis/T80 Frames/bias001.fit')
bias2 = fits.getdata('C:/Users/abrady/OneDrive - Maynooth University/Thesis/T80 Frames/bias002.fit')
bias3 = fits.getdata('C:/Users/abrady/OneDrive - Maynooth University/Thesis/T80 Frames/bias003.fit')

bias1 = CCDData(bias1, unit='adu')
bias2 = CCDData(bias2, unit='adu')
bias3 = CCDData(bias3, unit='adu')

# create a list of the bias frames for the master bias function
bias_list = [bias1,bias2,bias3]

# Combine bias frames to get the median and save it as a fits file
MasterBias = ccdproc.combine(bias_list, 'MasterBias80.fit', 'median')

# bring the flat frames into python
flat1B = fits.getdata('C:/Users/abrady/OneDrive - Maynooth University/Thesis/T80 Frames/flat001B.fit')
flat2B = fits.getdata('C:/Users/abrady/OneDrive - Maynooth University/Thesis/T80 Frames/flat002B.fit')
flat3B = fits.getdata('C:/Users/abrady/OneDrive - Maynooth University/Thesis/T80 Frames/flat003B.fit')

flat1B = CCDData(flat1B, unit ='adu')
flat2B = CCDData(flat2B, unit ='adu')
flat3B = CCDData(flat3B, unit ='adu')

# Create a list of flat frames and combine them to get the median
flatB_list = [flat1B , flat2B, flat3B]
MasterFlatB = ccdproc.combine(flatB_list,\
'MasterFlatB_80.fit', 'median')

#This process is repeated for red flat frames
flat1R = fits.getdata('C:/Users/abrady/OneDrive - Maynooth University/Thesis/T80 Frames/flat001R.fit')
flat2R = fits.getdata('C:/Users/abrady/OneDrive - Maynooth University/Thesis/T80 Frames/flat002R.fit')
flat3R = fits.getdata('C:/Users/abrady/OneDrive - Maynooth University/Thesis/T80 Frames/flat003R.fit')


flat1R = CCDData(flat1R, unit ='adu')
flat2R = CCDData(flat2R, unit ='adu')
flat3R = CCDData(flat3R, unit ='adu')


flatR_list = [flat1R , flat2R, flat3R]
MasterFlatR = ccdproc.combine(flatR_list,\
'MasterFlatR_80.fit', 'median')

#The process is repeated for green flat frames
flat1V = fits.getdata('C:/Users/abrady/OneDrive - Maynooth University/Thesis/T80 Frames/flat001V.fit')
flat2V = fits.getdata('C:/Users/abrady/OneDrive - Maynooth University/Thesis/T80 Frames/flat002V.fit')
flat3V = fits.getdata('C:/Users/abrady/OneDrive - Maynooth University/Thesis/T80 Frames/flat003V.fit')


flat1V = CCDData(flat1V, unit ='adu')
flat2V = CCDData(flat2V, unit ='adu')
flat3V = CCDData(flat3V, unit ='adu')



flatV_list = [flat1V , flat2V, flat3V]
MasterFlatV = ccdproc.combine(flatV_list,\
'MasterFlatV_80.fit', 'median')

# Bring the darks in python 
dark1 = fits.getdata('C:/Users/abrady/OneDrive - Maynooth University/Thesis/T80 Frames/dark_30s_001.fit')
dark2 = fits.getdata('C:/Users/abrady/OneDrive - Maynooth University/Thesis/T80 Frames/dark_30s_002.fit')
dark3 = fits.getdata('C:/Users/abrady/OneDrive - Maynooth University/Thesis/T80 Frames/dark_30s_003.fit')
    
dark1 = CCDData(dark1, unit = 'adu')
dark2 = CCDData(dark2, unit = 'adu')
dark3 = CCDData(dark3, unit = 'adu')

# Create a lsit of darks and combine them to get the median 
dark_30_list = [dark1, dark2, dark3]
MasterDark = ccdproc.combine(dark_30_list, \
'MasterDark30s_80.fit', 'median')

#Bring the science images into python
sci1 = fits.getdata('C:/Users/abrady/OneDrive - Maynooth University/Thesis/T80 Standard Star/ThetaPegasusStandard-0001V.fit')
sci2 = fits.getdata('C:/Users/abrady/OneDrive - Maynooth University/Thesis/T80 Standard Star/ThetaPegasusStandard-0002V.fit')
sci3 = fits.getdata('C:/Users/abrady/OneDrive - Maynooth University/Thesis/T80 Standard Star/ThetaPegasusStandard-0003V.fit')
sci4 = fits.getdata('C:/Users/abrady/OneDrive - Maynooth University/Thesis/T80 Standard Star/ThetaPegasusStandard-0004V.fit')
sci5 = fits.getdata('C:/Users/abrady/OneDrive - Maynooth University/Thesis/T80 Standard Star/ThetaPegasusStandard-0005V.fit')

sci1 = CCDData(sci1, unit = 'adu')
sci2 = CCDData(sci2, unit = 'adu')
sci3 = CCDData(sci3, unit = 'adu')
sci4 = CCDData(sci4, unit = 'adu')
sci5 = CCDData(sci5, unit = 'adu')


# subtract the dark frames from the bias
BiasSubDark = ccdproc.subtract_bias(MasterDark, MasterBias)

#Subtract the flat frame for a given colour from the bias
BiasSubFlat = ccdproc.subtract_bias(MasterFlatV, MasterBias)

# Subtract  each image from the bias
BiasSubSci1 = ccdproc.subtract_bias(sci1, MasterBias)
BiasSubSci2 = ccdproc.subtract_bias(sci2, MasterBias)
BiasSubSci3 = ccdproc.subtract_bias(sci3, MasterBias)
BiasSubSci4 = ccdproc.subtract_bias(sci4, MasterBias)
BiasSubSci5 = ccdproc.subtract_bias(sci5, MasterBias)

# subtract the flat from the dark
DarkSubFlat = ccdproc.subtract_dark(BiasSubFlat, BiasSubDark,
  dark_exposure = (30.0 * u.second),\
data_exposure = (1.0 * u.second),
 scale = True)
    
#create a dark without the science image
DarkSubSci1 = ccdproc.subtract_dark(BiasSubSci1, BiasSubDark,  dark_exposure = (30.0 * u.second),\
data_exposure = (8.0 * u.second),
 scale = True)
DarkSubSci2 = ccdproc.subtract_dark(BiasSubSci2, BiasSubDark,  dark_exposure = (30.0 * u.second),\
data_exposure = (8.0 * u.second),
 scale = True)
DarkSubSci3 = ccdproc.subtract_dark(BiasSubSci3, BiasSubDark,  dark_exposure = (30.0 * u.second),\
data_exposure = (8.0 * u.second),
 scale = True)
DarkSubSci4 = ccdproc.subtract_dark(BiasSubSci4, BiasSubDark,  dark_exposure = (30.0 * u.second),\
data_exposure = (8.0 * u.second),
 scale = True)
DarkSubSci5 = ccdproc.subtract_dark(BiasSubSci5, BiasSubDark,  dark_exposure = (30.0 * u.second),\
data_exposure = (8.0 * u.second),
 scale = True)


#Preform the final image reduction with the dark and flat frames
# The bias has already been subtracted from all frames used
FinalSci1 = ccdproc.flat_correct(DarkSubSci1, DarkSubFlat)
FinalSci2 = ccdproc.flat_correct(DarkSubSci2, DarkSubFlat)
FinalSci3 = ccdproc.flat_correct(DarkSubSci3, DarkSubFlat)
FinalSci4 = ccdproc.flat_correct(DarkSubSci4, DarkSubFlat)
FinalSci5 = ccdproc.flat_correct(DarkSubSci5, DarkSubFlat)


FinalSci1 = CCDData(FinalSci1, unit = 'adu')
FinalSci2 = CCDData(FinalSci2, unit = 'adu')
FinalSci3 = CCDData(FinalSci3, unit = 'adu')
FinalSci4 = CCDData(FinalSci3, unit = 'adu')
FinalSci3 = CCDData(FinalSci3, unit = 'adu')


# Combine all science images to get the final master image for a given colour filter
MasterSci = ccdproc.combine([FinalSci1, FinalSci2, FinalSci3 ], \
'MasterMedianR_star80.fits',\
'median')



    

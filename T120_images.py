# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from astropy import units as u
import numpy as np
import ccdproc
from astropy.io import fits
from astropy.nddata import CCDData
import matplotlib.pyplot as plt
from scipy.ndimage import zoom


bias1 = fits.getdata('C:/Users/abrady/OneDrive - Maynooth University/Thesis/T120 Frames/BIAS2-0001.fits')
bias2 = fits.getdata('C:/Users/abrady/OneDrive - Maynooth University/Thesis/T120 Frames/BIAS2-0002.fits')
bias3 = fits.getdata('C:/Users/abrady/OneDrive - Maynooth University/Thesis/T120 Frames/BIAS2-0003.fits')
bias4 = fits.getdata('C:/Users/abrady/OneDrive - Maynooth University/Thesis/T120 Frames/BIAS2-0004.fits')
bias5 = fits.getdata('C:/Users/abrady/OneDrive - Maynooth University/Thesis/T120 Frames/BIAS2-0005.fits')
bias6 = fits.getdata('C:/Users/abrady/OneDrive - Maynooth University/Thesis/T120 Frames/BIAS2-0006.fits')
bias7 = fits.getdata('C:/Users/abrady/OneDrive - Maynooth University/Thesis/T120 Frames/BIAS2-0007.fits')
bias8 = fits.getdata('C:/Users/abrady/OneDrive - Maynooth University/Thesis/T120 Frames/BIAS2-0008.fits')
bias9 = fits.getdata('C:/Users/abrady/OneDrive - Maynooth University/Thesis/T120 Frames/BIAS2-0009.fits')
bias10 = fits.getdata('C:/Users/abrady/OneDrive - Maynooth University/Thesis/T120 Frames/BIAS2-0010.fits')



bias1 = CCDData(bias1, unit='adu')
bias2 = CCDData(bias2, unit='adu')
bias3 = CCDData(bias3, unit='adu')
bias4 = CCDData(bias4, unit='adu')
bias5 = CCDData(bias5, unit='adu')
bias6 = CCDData(bias6, unit='adu')
bias7 = CCDData(bias7, unit='adu')
bias8 = CCDData(bias8, unit='adu')
bias9 = CCDData(bias9, unit='adu')
bias10 = CCDData(bias10, unit='adu')


bias_list = [bias1,bias2,bias3,bias4,bias5,bias6, bias7, bias8, bias9,bias10]
MasterBias = ccdproc.combine(bias_list, 'MasterBias120.fit', 'median', )

flat1B = fits.getdata('C:/Users/abrady/OneDrive - Maynooth University/Thesis/T120 Frames/flat_dome-0001B.fits')
flat2B = fits.getdata('C:/Users/abrady/OneDrive - Maynooth University/Thesis/T120 Frames/flat_dome-0002B.fits')
flat3B = fits.getdata('C:/Users/abrady/OneDrive - Maynooth University/Thesis/T120 Frames/flat_dome-0003B.fits')
flat4B = fits.getdata('C:/Users/abrady/OneDrive - Maynooth University/Thesis/T120 Frames/flat_dome-0004B.fits')
flat5B = fits.getdata('C:/Users/abrady/OneDrive - Maynooth University/Thesis/T120 Frames/flat_dome-0005B.fits')
flat6B = fits.getdata('C:/Users/abrady/OneDrive - Maynooth University/Thesis/T120 Frames/flat_dome-0006B.fits')
flat7B = fits.getdata('C:/Users/abrady/OneDrive - Maynooth University/Thesis/T120 Frames/flat_dome-0007B.fits')
flat8B = fits.getdata('C:/Users/abrady/OneDrive - Maynooth University/Thesis/T120 Frames/flat_dome-0008B.fits')
flat9B = fits.getdata('C:/Users/abrady/OneDrive - Maynooth University/Thesis/T120 Frames/flat_dome-0009B.fits')
flat10B = fits.getdata('C:/Users/abrady/OneDrive - Maynooth University/Thesis/T120 Frames/flat_dome-0010B.fits')

flat1B = CCDData(flat1B, unit ='adu')
flat2B = CCDData(flat2B, unit ='adu')
flat3B = CCDData(flat3B, unit ='adu')
flat4B = CCDData(flat4B, unit ='adu')
flat5B = CCDData(flat5B, unit ='adu')
flat6B = CCDData(flat6B, unit ='adu')
flat7B = CCDData(flat7B, unit ='adu')
flat8B = CCDData(flat8B, unit ='adu')
flat9B = CCDData(flat9B, unit ='adu')
flat10B = CCDData(flat10B, unit ='adu')

flatB_list = [flat1B , flat2B, flat3B, flat4B, flat5B, flat6B, flat7B, flat8B,flat9B, flat10B]
MasterFlatB = ccdproc.combine(flatB_list, 'MasterFlatcopyB_120.fit', 'average', overwrite = True)

flat1R = fits.getdata('C:/Users/abrady/OneDrive - Maynooth University/Thesis/T120 Frames/flat_dome-0001R.fits')
flat2R = fits.getdata('C:/Users/abrady/OneDrive - Maynooth University/Thesis/T120 Frames/flat_dome-0002R.fits')
flat3R = fits.getdata('C:/Users/abrady/OneDrive - Maynooth University/Thesis/T120 Frames/flat_dome-0003R.fits')
flat4R = fits.getdata('C:/Users/abrady/OneDrive - Maynooth University/Thesis/T120 Frames/flat_dome-0004R.fits')
flat5R = fits.getdata('C:/Users/abrady/OneDrive - Maynooth University/Thesis/T120 Frames/flat_dome-0005R.fits')
flat6R = fits.getdata('C:/Users/abrady/OneDrive - Maynooth University/Thesis/T120 Frames/flat_dome-0006R.fits')
flat7R = fits.getdata('C:/Users/abrady/OneDrive - Maynooth University/Thesis/T120 Frames/flat_dome-0007R.fits')
flat8R = fits.getdata('C:/Users/abrady/OneDrive - Maynooth University/Thesis/T120 Frames/flat_dome-0008R.fits')
flat9R = fits.getdata('C:/Users/abrady/OneDrive - Maynooth University/Thesis/T120 Frames/flat_dome-0009R.fits')
flat10R = fits.getdata('C:/Users/abrady/OneDrive - Maynooth University/Thesis/T120 Frames/flat_dome-0010R.fits')

flat1R = CCDData(flat1R, unit ='adu')
flat2R = CCDData(flat2R, unit ='adu')
flat3R = CCDData(flat3R, unit ='adu')
flat4R = CCDData(flat4R, unit ='adu')
flat5R = CCDData(flat5R, unit ='adu')
flat6R = CCDData(flat6R, unit ='adu')
flat7R = CCDData(flat7R, unit ='adu')
flat8R = CCDData(flat8R, unit ='adu')
flat9R = CCDData(flat9R, unit ='adu')
flat10R = CCDData(flat10R, unit ='adu')

flatR_list = [flat1R , flat2R, flat3R, flat4R, flat5R, flat6R, flat7R, flat8R, flat9R, flat10R]
MasterFlatR = ccdproc.combine(flatR_list,\
'MasterFlatR_120.fit', 'meadian', overwrite = True)

flat1V = fits.getdata('C:/Users/abrady/OneDrive - Maynooth University/Thesis/T120 Frames/flat_dome-0001V.fits')
flat2V = fits.getdata('C:/Users/abrady/OneDrive - Maynooth University/Thesis/T120 Frames/flat_dome-0002V.fits')
flat3V = fits.getdata('C:/Users/abrady/OneDrive - Maynooth University/Thesis/T120 Frames/flat_dome-0003V.fits')
flat4V = fits.getdata('C:/Users/abrady/OneDrive - Maynooth University/Thesis/T120 Frames/flat_dome-0004V.fits')
flat5V = fits.getdata('C:/Users/abrady/OneDrive - Maynooth University/Thesis/T120 Frames/flat_dome-0005V.fits')
flat6V = fits.getdata('C:/Users/abrady/OneDrive - Maynooth University/Thesis/T120 Frames/flat_dome-0006V.fits')
flat7V = fits.getdata('C:/Users/abrady/OneDrive - Maynooth University/Thesis/T120 Frames/flat_dome-0007V.fits')
flat8V = fits.getdata('C:/Users/abrady/OneDrive - Maynooth University/Thesis/T120 Frames/flat_dome-0008V.fits')
flat9V = fits.getdata('C:/Users/abrady/OneDrive - Maynooth University/Thesis/T120 Frames/flat_dome-0009V.fits')
flat10V = fits.getdata('C:/Users/abrady/OneDrive - Maynooth University/Thesis/T120 Frames/flat_dome-0010V.fits')

flat1V = CCDData(flat1V, unit ='adu')
flat2V = CCDData(flat2V, unit ='adu')
flat3V = CCDData(flat3V, unit ='adu')
flat4V = CCDData(flat4V, unit ='adu')
flat5V = CCDData(flat5V, unit ='adu')
flat6V = CCDData(flat6V, unit ='adu')
flat7V = CCDData(flat7V, unit ='adu')
flat8V = CCDData(flat8V, unit ='adu')
flat9V = CCDData(flat9V, unit ='adu')
flat10V = CCDData(flat10V, unit ='adu')

flatV_list = [flat1V , flat2V, flat3V, flat4V, flat5V, flat6V, flat7V, flat8V,flat9V, flat10V]
MasterFlatV = ccdproc.combine(flatV_list,\
'MasterFlatV_120.fit', 'median', overwrite = True)

dark1 = fits.getdata('C:/Users/abrady/OneDrive - Maynooth University/Thesis/T120 Frames/Dark60s-0001.fits')
dark2 = fits.getdata('C:/Users/abrady/OneDrive - Maynooth University/Thesis/T120 Frames/Dark60s-0002.fits')
    
dark1 = CCDData(dark1, unit = 'adu')
dark2 = CCDData(dark2, unit = 'adu')

dark_list = [dark1, dark2]
MasterDark = ccdproc.combine(dark_list, \
'MasterDark_120.fit', 'median', overwrite = True)
    
sci1 = fits.getdata('C:/Users/abrady/OneDrive - Maynooth University/Thesis/SA92 249/SA249-0001R.fits')
sci2 = fits.getdata('C:/Users/abrady/OneDrive - Maynooth University/Thesis/SA92 249/SA249-0002R.fits')
sci3 = fits.getdata('C:/Users/abrady/OneDrive - Maynooth University/Thesis/SA92 249/SA249-0003R.fits')

sci1 = CCDData(sci1, unit = 'adu')
sci2 = CCDData(sci2, unit = 'adu')
sci3 = CCDData(sci3, unit = 'adu')


BiasSubDark = ccdproc.subtract_bias(MasterDark, MasterBias)
BiasSubFlat = ccdproc.subtract_bias(MasterFlatR, MasterBias)
BiasSubSci1 = ccdproc.subtract_bias(sci1, MasterBias)
BiasSubSci2 = ccdproc.subtract_bias(sci2, MasterBias)
BiasSubSci3 = ccdproc.subtract_bias(sci3, MasterBias)


DarkSubFlat = ccdproc.subtract_dark(BiasSubFlat, BiasSubDark,
  dark_exposure = (60.0 * u.second),\
data_exposure = (1.0 * u.second),
 scale = True)
DarkSubSci1 = ccdproc.subtract_dark(BiasSubSci1, BiasSubDark,  dark_exposure = (60.0 * u.second),\
data_exposure = (180.0 * u.second),
 scale = True)
DarkSubSci2 = ccdproc.subtract_dark(BiasSubSci2, BiasSubDark,  dark_exposure = (60.0 * u.second),\
data_exposure = (180.0 * u.second),
 scale = True)
DarkSubSci3 = ccdproc.subtract_dark(BiasSubSci3, BiasSubDark,  dark_exposure = (60.0 * u.second),\
data_exposure = (180.0 * u.second),
 scale = True)



FinalSci1 = ccdproc.flat_correct(DarkSubSci1, DarkSubFlat)
FinalSci2 = ccdproc.flat_correct(DarkSubSci2, DarkSubFlat)
FinalSci3 = ccdproc.flat_correct(DarkSubSci3, DarkSubFlat)


FinalSci1 = CCDData(FinalSci1, unit = 'adu')
FinalSci2 = CCDData(FinalSci2, unit = 'adu')
FinalSci3 = CCDData(FinalSci3, unit = 'adu')


MasterSci = ccdproc.combine([FinalSci1, FinalSci2, FinalSci3 ] ,\
'MasterMedian120R.fits',\
'median')

im


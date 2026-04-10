# -*- coding: utf-8 -*-
"""
Created on Tue Dec  2 16:09:48 2025

@author: alex

Description: Create a cutout of the same region for a given filter image
"""
# import necessary packages
from astropy.io import fits
from astropy.wcs import WCS
from astropy.coordinates import SkyCoord
from astropy.nddata import Cutout2D
import astropy.units as u

# Open a given fits image and get the data from the file
hdul = fits.open('C:/Users/abrady/OneDrive - Maynooth University/Thesis/Orion FInal/Orion_R_wcs.fits')
data = hdul[0].data
# and get the world co-ordinates from the header of the file
wcs = WCS(hdul[0].header)

# using the cutout2D function means we need to specify center position in WSC
# These were taken from the centre of the red filter image
position = SkyCoord(83.8401478977*u.deg, -5.39618775612*u.deg, frame='icrs')

# Size of end image is specified as pixel by pixel length
size = (700, 700)

# Use cutout function from astropy
cutout = Cutout2D(data, position, size, wcs=wcs)

# Save the cutout as a fits image
hdu = fits.PrimaryHDU(cutout.data, header=cutout.wcs.to_header())
hdu.writeto("cutout_1000pxR.fits", overwrite=True)

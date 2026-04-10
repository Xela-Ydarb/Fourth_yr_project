# -*- coding: utf-8 -*-
"""
Created on Mon Dec  1 15:49:16 2025

@author: abrady
"""

from astropy.io import fits
from astropy.wcs import WCS
from astropy.coordinates import SkyCoord
from astropy.nddata import Cutout2D
import astropy.units as u

# -----------------------------
# Load the FITS image + WCS
# -----------------------------
hdul = fits.open('C:/Users/abrady/OneDrive - Maynooth University/Thesis/Orion FInal/Orion_R_wcs.fits')
data = hdul[0].data
wcs = WCS(hdul[0].header)

# -----------------------------
# Define the sky position (RA, Dec)
# Example: RA=150.114°, Dec=2.205°
# -----------------------------
position = SkyCoord(83.8401478977*u.deg, -5.39618775612*u.deg, frame='icrs')

# -----------------------------
# Define size of the cutout
# 1000 x 1000 pixels
# -----------------------------
size = (700, 700) # (ny, nx)

# -----------------------------
# Create the cutout using Cutout2D
# -----------------------------
cutout = Cutout2D(data, position, size, wcs=wcs)

# -----------------------------
# Save the cutout as a new FITS file
# -----------------------------
hdu = fits.PrimaryHDU(cutout.data, header=cutout.wcs.to_header())
hdu.writeto("cutout_1000pxR.fits", overwrite=True)

print("Saved cutout as cutout_1000pxR.fits")

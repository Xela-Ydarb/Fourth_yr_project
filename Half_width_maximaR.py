# -*- coding: utf-8 -*-
"""
Created on Wed Feb  4 16:10:42 2026

@author: abrady
"""

# import needed packages
import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits
from astropy.modeling import models, fitting

# Bring in the fits image data
image_file = "C:/Users/abrady/OneDrive - Maynooth University/Thesis/T80 Standard Star Final/MasterMedianR_star80.fits"

hdu_list = fits.open(image_file)

image_data = hdu_list[0].data

# Create a box around the star
x , y = 897, 507
r = 6

sub = image_data[y - r: y+r , x-r:x+r]

# Map the values of the star onto a gaussian curve
yg, xg= np.mgrid[:sub.shape[0], :sub.shape[1]]

print(image_data.max())
g_init = models.Gaussian2D(amplitude = image_data.max(), x_mean = r, y_mean=r, x_stddev = 2, y_stddev = 2)
fit_p = fitting.LevMarLSQFitter()
g_fit = fit_p(g_init, xg, yg, sub)

#Calculate full width half maxima for x and y then average
# 2.355 = 2 sqrt(2ln(2))
fwhm_x = 2.355 * g_fit.x_stddev.value
fwhm_y = 2.355 * g_fit.y_stddev.value
fwhm = 0.5 * (fwhm_x + fwhm_y)

print(fwhm)

#get the median of the image as the background and subtract it from the data
mean, median = np.mean(image_data), np.median(image_data), 
data_bg = image_data - median


# Find the max intensity of the data
i0 = np.max(data_bg)


# For a telescope the gain is 1.47
gain = 1.47 # electrons per adu count

# Use the full width half max to calculate flux
# Convert adu flux to electon flux
flux_adu = 2 * (np.pi/(4*np.log(2))) * i0 * fwhm**2
flux_e = flux_adu  /1.47

c_flux = flux_e/ np.pi
c_adu = flux_adu/ np.pi

print(f"Total flux: {flux_adu:.1f} ADU")
print(f"Total flux for circular aperature: {c_adu:.1f} ADU")
print(f"Total electron: {flux_e:.1f} ")
print(f"Total electron for Circular Aperature: {c_flux:.1f} ")

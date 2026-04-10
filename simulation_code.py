# -*- coding: utf-8 -*-
"""
Created on Wed Feb  4 15:13:49 2026

@author: abrady
"""

#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from math import pi

# -------------------------------------------------------
# Physical constants
# -------------------------------------------------------
h = 6.62607015e-34       # Planck constant (J s)
c = 2.99792458e8         # Speed of light (m/s)
k_B = 1.380649e-23       # Boltzmann constant (J/K)
sigma = 5.670374419e-8   # Stefan-Boltzmann constant (W/m^2/K^4)

# Solar, Earth, AU, parsec
R_sun   = 6.957e8
R_earth = 6.371e6
AU      = 1.495978707e11
pc      = 3.085677581491367e16


# -------------------------------------------------------
# 1: Planck function
# -------------------------------------------------------
def planck_lambda(wavelength_m, T):
    """Planck spectral radiance B_lambda (W m^-2 sr^-1 m^-1)."""
    lam = wavelength_m
    a = 2*h*c**2 / lam**5
    b = np.exp(h*c/(lam*k_B*T)) - 1.0
    return a / b


# -------------------------------------------------------
# 2: Stellar spectral flux at distance r
# -------------------------------------------------------
def stellar_flux_at_distance(wavelength_m, T_star, R_star_m, distance_m):
    """Flux from star at distance r (W m^-2 m^-1)."""
    return pi * planck_lambda(wavelength_m, T_star) * (R_star_m**2 / distance_m**2)


# -------------------------------------------------------
# 3: Stellar flux at Earth
# -------------------------------------------------------
def stellar_spectral_flux_at_earth(wavelength_m, T_star, R_star_m, D_star_m):
    return stellar_flux_at_distance(wavelength_m, T_star, R_star_m, D_star_m)


# -------------------------------------------------------
# 4: Planet reflected light
# -------------------------------------------------------
def planet_reflected_spectral_flux_at_earth(wavelength_m, T_star, R_star_m, a_m, R_p_m, A_g, D_star_m):
    F_star_planet = stellar_flux_at_distance(wavelength_m, T_star, R_star_m, a_m)
    power_intercepted = F_star_planet * pi * R_p_m**2
    power_reflected   = A_g * power_intercepted
    return power_reflected / (4 * pi * D_star_m**2)


# -------------------------------------------------------
# 5: Planet thermal emission
# -------------------------------------------------------
def planet_thermal_spectral_flux_at_earth(wavelength_m, T_p, R_p_m, D_star_m):
    return pi * planck_lambda(wavelength_m, T_p) * (R_p_m**2 / D_star_m**2)


# -------------------------------------------------------
# 6: Planet equilibrium temperature
# -------------------------------------------------------
def equilibrium_temperature(T_star, R_star_m, a_m, A_bond=0.3, f=1.0):
    return T_star * (R_star_m/(2*a_m))**0.5 * ((1 - A_bond)/f)**0.25


# -------------------------------------------------------
# 7: Simple top-hat filter
# -------------------------------------------------------
def top_hat_transmission(wavelength_m, center_m, width_m):
    half = width_m / 2
    return np.where((wavelength_m > center_m - half) &
                    (wavelength_m < center_m + half), 1.0, 0.0)


# -------------------------------------------------------
# 8: Convert spectral flux to photon rate
# -------------------------------------------------------
def photons_per_second(telescope_diameter_m, wavelengths_m, spectral_flux_W_m2_m, transmission, qe=0.9):
    E_photon = h * c / wavelengths_m
    photon_flux_density = spectral_flux_W_m2_m / E_photon
    collected_per_m2 = np.trapz(photon_flux_density * transmission * qe, wavelengths_m)
    area = pi * (telescope_diameter_m/2)**2
    return area * collected_per_m2


# -------------------------------------------------------
# 9: Return contrast ratio only
# -------------------------------------------------------
def contrast_ratio(N_planet, N_star):
    if N_star <= 0:
        return 0
    return N_planet / N_star


# -------------------------------------------------------
# Filters (simple top-hat approximations)
# -------------------------------------------------------
filters = {
    'B': {'center_m': 450e-9, 'width_m': 90e-9},
    'G': {'center_m': 550e-9, 'width_m': 100e-9},
    'R': {'center_m': 650e-9, 'width_m': 150e-9},
    'J': {'center_m': 1.25e-6, 'width_m': 0.30e-6},
    'H': {'center_m': 1.65e-6, 'width_m': 0.35e-6},
}


# -------------------------------------------------------
# USER PARAMETERS
# -------------------------------------------------------
params = {
    'T_star': 7915.0,
    'R_star_Rsun': 2.6,
    'distance_star_pc': 28.3,

    'a_AU': 0.05,
    'R_p_Rearth': 286.4,     # Planet radius in EARTH radii âœ”

    'albedo': 0.3,
    'telescope_diameter_m': 0.8,
    'qe': 0.9
}


# -------------------------------------------------------
# Main computation
# -------------------------------------------------------
wavelengths = np.linspace(0.3e-6, 3.0e-6, 5000)

# Convert parameters
T_star = params['T_star']
R_star = params['R_star_Rsun'] * R_sun
D_star = params['distance_star_pc'] * pc
a      = params['a_AU'] * AU
R_p    = params['R_p_Rearth'] * R_earth
A_g    = params['albedo']
D_t    = params['telescope_diameter_m']
qe     = params['qe']

# Planet temperature
T_p = equilibrium_temperature(T_star, R_star, a, A_bond=A_g)

# Fluxes
F_ref  = planet_reflected_spectral_flux_at_earth(wavelengths, T_star, R_star, a, R_p, A_g, D_star)
F_therm = planet_thermal_spectral_flux_at_earth(wavelengths, T_p, R_p, D_star)
F_planet = F_ref + F_therm

F_star = stellar_spectral_flux_at_earth(wavelengths, T_star, R_star, D_star)

# Results table
results = []
for name, f in filters.items():
    T_filt = top_hat_transmission(wavelengths, f['center_m'], f['width_m'])

    N_planet = photons_per_second(D_t, wavelengths, F_planet, T_filt, qe=qe)
    N_star   = photons_per_second(D_t, wavelengths, F_star,   T_filt, qe=qe)

    C = contrast_ratio(N_planet, N_star)

    results.append({
        'filter': name,
        'planet_photons_per_s': N_planet,
        'star_photons_per_s': N_star,
        'contrast': C
    })

df = pd.DataFrame(results).set_index('filter')
print(df)


# -------------------------------------------------------
# Plot star vs planet spectral flux (converted to photons)
# -------------------------------------------------------
plt.figure(figsize=(9,5))
E_photon = h*c / wavelengths

planet_phot_rate = F_planet / E_photon
star_phot_rate   = F_star   / E_photon

plt.loglog(wavelengths*1e6, star_phot_rate,   label="Star photon spectrum")
plt.loglog(wavelengths*1e6, planet_phot_rate, label="Planet photon spectrum")
plt.xlabel("Wavelength (Âµm)")
plt.ylabel("Photon flux density (photons/s/mÂ²/m)")
plt.title("Star vs Planet Photon Spectra")
plt.legend()
plt.grid(True, which="both", ls="--", alpha=0.4)
plt.tight_layout()
plt.show()

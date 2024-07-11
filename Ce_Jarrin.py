#This code fits a curve to the data provided in GLASSBRENNER paper for electronic specific heat using a similar formula to the one proposed by Jarrin, 2020.
#Still under development

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Define the provided fitting function (Jarrin 2020)
def ce_function(x, B, xf):
    A = 1.5e-5
    E = 1e-6
    return 0.5 * (A - E) * (1 + np.tanh(B * (x - xf))) + E

# K_e data for Silicon converted to C_e (Temperature in K and C_e in eV/K). Source: GLASSBRENNER
temperature_data = np.array([0,800, 1000, 1200, 1400, 1600, 1681])
ce_data = np.array([0,8.738094e17, 4.056972e18, 1.104745e19, 2.209490e19, 3.620068e19, 4.231734e19]) / 10**25

# Prepare data for fitting
x_data = temperature_data / 1000
y_data = ce_data

# Assign higher weights to lower temperature points using a power-law weighting scheme (optional, does not work)
weights = 1 / (x_data**2 + 1e-6)

# Fit
initial_guess = [1, 1]  # Initial guesses for B and xf
popt, _ = curve_fit(ce_function, x_data, y_data, p0=initial_guess, sigma=weights, maxfev=10000)

# Extract the optimal coefficients
B_opt, xf_opt = popt

# Generate fitted curve
Te = np.linspace(0, 2000, 100)  # Te in Kelvin
x = Te / 1000  # x variable for the horizontal axis
ce_fit = ce_function(x, B_opt, xf_opt)

# Plotting the fitted curve with data points
plt.figure(figsize=(10, 6))
plt.plot(x, ce_fit, label=f'Fitted Curve (B={B_opt:.4f}, xf={xf_opt:.4f})', color='blue')
plt.scatter(x_data, y_data, color='red', label='K_e data points')
plt.xlabel('$T_e / 1000$ (K)')
plt.ylabel('$C_e$ (eV/K)')
plt.title('Fit with Provided Expression for Si C_e')
plt.legend()
plt.grid(True)
plt.show()

popt

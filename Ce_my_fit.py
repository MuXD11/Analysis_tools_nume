import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Define the power law fitting function
def power_law_function(x, a, b):
    return a * np.power(x, b)

# Define the original fitting function with fixed A and E
def ce_function_fit(x, B, xf):
    A = 1.5 * 1e-5
    E = 1e-6
    return 0.5 * (A - E) * (1 + np.tanh(B * (x - xf))) + E

# K_e data for Silicon converted to C_e (Temperature in K and C_e in eV/K). Source: GLASSBRENNER. More info: Glassenberg_Ce_Ke_data.txt
temperature_data = np.array([800, 1000, 1200, 1400, 1600, 1681])
ce_data = np.array([8.738094e17, 4.056972e18, 1.104745e19, 2.209490e19, 3.620068e19, 4.231734e19]) / 10**25

# Add a point close to (0, 0) to the dataset to ensure the fit starts near the origin
#temperature_data = np.insert(temperature_data, 0, 0.1)
#ce_data = np.insert(ce_data, 0, 2.2e-7)

# Prepare data for fitting
x_data = temperature_data / 1000
y_data = ce_data

# Fit the power law curve
popt_power_law, _ = curve_fit(power_law_function, x_data, y_data)

# Print the fitted parameters
a, b = popt_power_law
print(f'Fitted power law function: y = {a:.4e} * x^{b:.4f}')

# Generate fitted power law curve
Te = np.linspace(0, 2000, 100)  # Te in Kelvin
x = Te / 1000  # x variable for the horizontal axis
power_law_fit = power_law_function(x, *popt_power_law)

# Constants for plotting
k_B = 8.617333262145e-5  # Boltzmann constant in eV/K
y_line = (3/2) * k_B  # 3/2 * k_B

# Plotting power law fit
plt.figure(figsize=(10, 6))
plt.plot(x, power_law_fit, label=f'Power Law Fit', color='blue')
#plt.axhline(y=y_line, color='green', linestyle='--', label='$\\frac{3}{2}k_B$')
plt.scatter(x_data, y_data, color='red', label='C_e data points')

plt.xlabel('$T_e / 1000$ (K)')
plt.ylabel('$C_e$ (eV/K)')
plt.title('Power Law Fit for Si C_e as a Function of Temperature')
plt.legend()
plt.grid(True)
plt.show()

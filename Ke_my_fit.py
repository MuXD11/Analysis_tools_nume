
# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.optimize import curve_fit

# # Define the polynomial fitting function
# def poly_function(x, u, a, b, c):
#     return u * x**3 + a * x**2 + b * x + c
# # Define the exponential fitting function
# def exp_function(x, a, b, c):
#     return a * np.exp(b * x) + c

# # K_e data for Silicon (Temperature in K and K_e in eV/K*ang*ps). Source: GLASSBRENNER. More info: Glassenberg_Ce_Ke_data.txt
# temperature_data = np.array([800, 1000, 1200, 1400, 1600, 1681])
# ke_data = np.array([8.738094e17, 4.056972e18, 1.104745e19, 2.209490e19, 3.620068e19, 4.231734e19]) / 10**22

# # Prepare data for fitting
# x_data = temperature_data / 1000
# y_data = ke_data

# # Fit the polynomial curve
# popt_poly, _ = curve_fit(poly_function, x_data, y_data)
# popt_exp, _  = curve_fit(exp_function, x_data, y_data)
# # Generate fitted polynomial curve
# Te = np.linspace(000, 2000, 100)  # Te in Kelvin
# x = Te / 1000  # x variable for the horizontal axis
# poly_fit = poly_function(x, *popt_poly)
# exp_fit = exp_function(x, *popt_exp)

# # Constants for plotting
# k_B = 8.617333262145e-5  # Boltzmann constant in eV/K
# y_line = (3/2) * k_B  # 3/2 * k_B

# # Plotting polynomial fit
# plt.figure(figsize=(10, 6))
# plt.plot(x, poly_fit, label=f'Polynomial Fit', color='blue')
# #plt.plot(x, exp_fit, label=f'Polynomial Fit', color='blue')

# #plt.axhline(y=y_line, color='green', linestyle='--', label='$\\frac{3}{2}k_B$')
# plt.scatter(x_data, y_data, color='red', label='K_e data points')

# plt.xlabel('$T_e / 1000$ (K)')
# plt.ylabel('$K_e$ (eV/K*ps*ang)')
# plt.title('Polynomial Fit for Si K_e as a Function of Temperature')
# plt.legend()
# plt.grid(True)
# plt.show()

#############################################################################################################################################################

# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.optimize import curve_fit

# # Define the power law fitting function
# def power_law_function(x, a, b):
#     return a * np.power(x, b)

# # K_e data for Silicon (Temperature in K and K_e in eV/K*ang*ps). Source: GLASSBRENNER. More info: Glassenberg_Ce_Ke_data.txt
# temperature_data = np.array([800, 1000, 1200, 1400, 1600, 1681])
# ke_data = np.array([8.738094e17, 4.056972e18, 1.104745e19, 2.209490e19, 3.620068e19, 4.231734e19]) / 10**22

# # Add a point close to (0, 0) to the dataset to ensure the fit starts near the origin
# #temperature_data = np.insert(temperature_data, 0, 0.1)
# #ke_data = np.insert(ke_data, 0, 0.1)

# # Prepare data for fitting
# x_data = temperature_data / 1000
# y_data = ke_data

# # Fit the power law curve
# popt_power_law, _ = curve_fit(power_law_function, x_data, y_data)

# # Generate fitted power law curve
# Te = np.linspace(0, 2000, 100)  # Te in Kelvin
# x = Te / 1000  # x variable for the horizontal axis
# power_law_fit = power_law_function(x, *popt_power_law)

# # Constants for plotting
# k_B = 8.617333262145e-5  # Boltzmann constant in eV/K
# y_line = (3/2) * k_B  # 3/2 * k_B

# # Plotting power law fit
# plt.figure(figsize=(10, 6))
# plt.plot(x, power_law_fit, label=f'Power Law Fit', color='blue')
# #plt.axhline(y=y_line, color='green', linestyle='--', label='$\\frac{3}{2}k_B$')
# plt.scatter(x_data, y_data, color='red', label='K_e data points')

# plt.xlabel('$T_e / 1000$ (K)')
# plt.ylabel('$K_e$ (eV/K*ps*ang)')
# plt.title('Power Law Fit for Si K_e as a Function of Temperature')
# plt.legend()
# plt.grid(True)
# plt.show()

#############################################################################################################################################################

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Define the power law fitting function
def power_law_function(x, a, b):
    return a * np.power(x, b)

# K_e data for Silicon (Temperature in K and K_e in eV/K*ang*ps). Source: GLASSBRENNER. More info: Glassenberg_Ce_Ke_data.txt
temperature_data = np.array([800, 1000, 1200, 1400, 1600, 1681])
ke_data = np.array([8.738094e17, 4.056972e18, 1.104745e19, 2.209490e19, 3.620068e19, 4.231734e19]) / 10**22

# Add a point close to (0, 0) to the dataset to ensure the fit starts near the origin
#temperature_data = np.insert(temperature_data, 0, 0.1)
#ke_data = np.insert(ke_data, 0, 2.2e-7)

# Prepare data for fitting
x_data = temperature_data / 1000
y_data = ke_data

# Fit the power law curve
popt_power_law, _ = curve_fit(power_law_function, x_data, y_data)

# Generate fitted power law curve
Te = np.linspace(0, 2000, 100)  # Te in Kelvin
x = Te / 1000  # x variable for the horizontal axis
power_law_fit = power_law_function(x, *popt_power_law)

# Constants for plotting
k_B = 8.617333262145e-5  # Boltzmann constant in eV/K
y_line = (3/2) * k_B  # 3/2 * k_B

a, b = popt_power_law
print(f'Fitted power law function: y = {a:.4e} * x^{b:.4f}')

# Plotting power law fit
plt.figure(figsize=(10, 6))
plt.plot(x, power_law_fit, label=f'Power Law Fit', color='blue')
#plt.axhline(y=y_line, color='green', linestyle='--', label='$\\frac{3}{2}k_B$')
plt.scatter(x_data, y_data, color='red', label='K_e data points')

plt.xlabel('$T_e / 1000$ (K)')
plt.ylabel('$K_e$ (eV/K*ps*ang)')
plt.title('Power Law Fit for Si K_e as a Function of Temperature')
plt.legend()
plt.grid(True)
plt.show()

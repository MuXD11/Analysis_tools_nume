# #This file plots specific eletronic heat from different models (NRL, DFTB, ...)

# import matplotlib.pyplot as plt

# # Data for each model
# kwon_data = {
#     300.0: 9.1451e-11, 400.0: 6.4703e-10, 500.0: 2.0650e-09, 600.0: 4.6105e-09, 700.0: 8.3760e-09,
#     800.0: 1.3388e-08, 900.0: 1.9674e-08, 1000.0: 2.7302e-08, 1100.0: 3.6381e-08, 1200.0: 4.7049e-08,
#     1300.0: 5.9448e-08, 1400.0: 7.3712e-08, 1500.0: 8.9954e-08, 1600.0: 1.0826e-07, 1700.0: 1.2868e-07,
#     1800.0: 1.5125e-07, 1900.0: 1.7598e-07, 2000.0: 2.0290e-07, 2100.0: 2.3200e-07, 2200.0: 2.6328e-07,
#     2300.0: 2.9677e-07
# }

# dftb_data = {
#     300.0: -3.9456e-15, 400.0: 3.7785e-16, 500.0: 1.2853e-14, 600.0: 3.6569e-13, 700.0: 4.0444e-12,
#     800.0: 2.4657e-11, 900.0: 1.0122e-10, 1000.0: 3.1509e-10, 1100.0: 8.0229e-10, 1200.0: 1.7572e-09,
#     1300.0: 3.4283e-09, 1400.0: 6.1077e-09, 1500.0: 1.0119e-08, 1600.0: 1.5806e-08, 1700.0: 2.3519e-08,
#     1800.0: 3.3609e-08, 1900.0: 4.6418e-08, 2000.0: 6.2274e-08, 2100.0: 8.1488e-08, 2200.0: 1.0435e-07,
#     2300.0: 1.3111e-07
# }

# nrl_data = {
#     300.0: 2.910629e-09, 400.0: 5.661950e-09, 500.0: 9.548684e-09, 600.0: 1.511413e-08, 700.0: 2.285631e-08,
#     800.0: 3.303906e-08, 900.0: 4.572865e-08, 1000.0: 6.087640e-08, 1100.0: 7.837945e-08, 1200.0: 9.811339e-08,
#     1300.0: 1.199466e-07, 1400.0: 1.437453e-07, 1500.0: 1.693762e-07, 1600.0: 1.967090e-07, 1700.0: 2.256201e-07,
#     1800.0: 2.559987e-07, 1900.0: 2.877523e-07, 2000.0: 3.208114e-07, 2100.0: 3.551316e-07
# }

# # Ensure common temperature range
# common_temps = sorted(set(kwon_data.keys()) & set(dftb_data.keys()) & set(nrl_data.keys()))
# kwon_values = [kwon_data[temp] for temp in common_temps]
# dftb_values = [dftb_data[temp] for temp in common_temps]
# nrl_values = [nrl_data[temp] for temp in common_temps]

# # Plotting
# plt.figure(figsize=(10, 6))
# plt.plot(common_temps, kwon_values, label='KWON', marker='o')
# plt.plot(common_temps, dftb_values, label='DFTB', marker='x')
# plt.plot(common_temps, nrl_values, label='NRL', marker='s')

# plt.xlabel('Temperature (K)')
# plt.ylabel('Specific Electronic Heat (eV/ang³*K)')
# plt.title('Specific Electronic Heat vs Temperature')
# plt.legend()
# plt.grid(True)
# plt.yscale('log')  # Using log scale for better visibility of small values
# plt.show()


#################################################################### EXPERIMENTAL DATA DIVIDED BY 5.43³ ####################################################################

import numpy as np
import matplotlib.pyplot as plt

# Data for each model
kwon_data = {
    300.0: 9.1451e-11, 400.0: 6.4703e-10, 500.0: 2.0650e-09, 600.0: 4.6105e-09, 700.0: 8.3760e-09,
    800.0: 1.3388e-08, 900.0: 1.9674e-08, 1000.0: 2.7302e-08, 1100.0: 3.6381e-08, 1200.0: 4.7049e-08,
    1300.0: 5.9448e-08, 1400.0: 7.3712e-08, 1500.0: 8.9954e-08, 1600.0: 1.0826e-07, 1700.0: 1.2868e-07,
    1800.0: 1.5125e-07, 1900.0: 1.7598e-07, 2000.0: 2.0290e-07, 2100.0: 2.3200e-07, 2200.0: 2.6328e-07,
    2300.0: 2.9677e-07
}

dftb_data = {
    300.0: -3.9456e-15, 400.0: 3.7785e-16, 500.0: 1.2853e-14, 600.0: 3.6569e-13, 700.0: 4.0444e-12,
    800.0: 2.4657e-11, 900.0: 1.0122e-10, 1000.0: 3.1509e-10, 1100.0: 8.0229e-10, 1200.0: 1.7572e-09,
    1300.0: 3.4283e-09, 1400.0: 6.1077e-09, 1500.0: 1.0119e-08, 1600.0: 1.5806e-08, 1700.0: 2.3519e-08,
    1800.0: 3.3609e-08, 1900.0: 4.6418e-08, 2000.0: 6.2274e-08, 2100.0: 8.1488e-08, 2200.0: 1.0435e-07,
    2300.0: 1.3111e-07
}

nrl_data = {
    300.0: 2.910629e-09, 400.0: 5.661950e-09, 500.0: 9.548684e-09, 600.0: 1.511413e-08, 700.0: 2.285631e-08,
    800.0: 3.303906e-08, 900.0: 4.572865e-08, 1000.0: 6.087640e-08, 1100.0: 7.837945e-08, 1200.0: 9.811339e-08,
    1300.0: 1.199466e-07, 1400.0: 1.437453e-07, 1500.0: 1.693762e-07, 1600.0: 1.967090e-07, 1700.0: 2.256201e-07,
    1800.0: 2.559987e-07, 1900.0: 2.877523e-07, 2000.0: 3.208114e-07, 2100.0: 3.551316e-07
}

# Experimental data
exp_data = {
    800: 8.738094e-08,
    1000: 4.056972e-07,
    1200: 1.104745e-06,
    1400: 2.20949e-06,
    1600: 3.620068e-06,
    1681: 4.231734e-06
}

# Convert experimental data from eV/K to eV/ang³*K
lattice_constant = 5.43  # angstroms
conversion_factor = lattice_constant ** 3
#conversion_factor = conversion_factor/8
exp_data_converted = {k: v / conversion_factor for k, v in exp_data.items()}

# Ensure common temperature range
common_temps = sorted(set(kwon_data.keys()) & set(dftb_data.keys()) & set(nrl_data.keys()))
kwon_values = [kwon_data[temp] for temp in common_temps]
dftb_values = [dftb_data[temp] for temp in common_temps]
nrl_values = [nrl_data[temp] for temp in common_temps]

# Prepare experimental data for plotting
exp_temps = sorted(exp_data_converted.keys())
exp_values = [exp_data_converted[temp] for temp in exp_temps]

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(common_temps, kwon_values, label='KWON', marker='o')
plt.plot(common_temps, dftb_values, label='DFTB', marker='x')
plt.plot(common_temps, nrl_values, label='NRL', marker='s')
plt.plot(exp_temps, exp_values, label='Experimental', marker='d', linestyle='--')

plt.xlabel('Temperature (K)')
plt.ylabel('Specific Electronic Heat (eV/ang³*K)')
plt.title('Specific Electronic Heat vs Temperature')
plt.legend()
plt.grid(True)
#plt.yscale('log')  # Using log scale for better visibility of small values
plt.show()

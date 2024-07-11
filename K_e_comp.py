import numpy as np
import matplotlib.pyplot as plt

# This code compares experimental K_e data with NRL and DFTB models for low temperatures

# Experimental data provided (ev/K*ps*ang)
temperature_data = np.array([800, 1000, 1200, 1400, 1600, 1681])
ke_data_exp = np.array([8.738094e17, 4.056972e18, 1.104745e19, 2.209490e19, 3.620068e19, 4.231734e19]) / 10**22

# NRL model data (ev/K*ps*ang)
NRL_data = np.array([
    [300.0, 9.852139e-05],
    [400.0, 2.891985e-04],
    [500.0, 9.300954e-04],
    [600.0, 2.297865e-03],
    [700.0, 4.528635e-03],
    [800.0, 7.636431e-03],
    [900.0, 1.156618e-02],
    [1000.0, 1.623096e-02],
    [1100.0, 2.153661e-02],
    [1200.0, 2.739464e-02],
    [1300.0, 3.372407e-02],
    [1400.0, 4.046901e-02],
    [1500.0, 4.757959e-02],
    [1600.0, 5.501925e-02],
    [1700.0, 6.271832e-02],
    [1800.0, 7.077627e-02],
    [1900.0, 7.913675e-02],
    [2000.0, 8.781108e-02],
    [2100.0, 9.656873e-02]
])

DFTB_data = np.array([
    [300.0, 2.2053e-14],
    [400.0, 2.4924e-12],
    [500.0, 1.9298e-09],
    [600.0, 5.9430e-08],
    [700.0, 6.8980e-07],
    [800.0, 4.3739e-06],
    [900.0, 1.8559e-05],
    [1000.0, 5.9465e-05],
    [1100.0, 1.5533e-04],
    [1200.0, 3.4806e-04],
    [1300.0, 6.9295e-04],
    [1400.0, 1.2567e-03],
    [1500.0, 2.1148e-03],
    [1600.0, 3.3480e-03],
    [1700.0, 5.0381e-03],
    [1800.0, 7.2682e-03],
    [1900.0, 1.0114e-02],
    [2000.0, 1.3648e-02],
    [2100.0, 1.7914e-02],
    [2200.0, 2.2978e-02]
])

KWON_data = np.array([
    [300.0, 5.9465e-23],
    [400.0, 2.3279e-16],
    [500.0, 1.9111e-12],
    [600.0, 7.3498e-10],
    [700.0, 4.9841e-08],
    [800.0, 1.1403e-06],
    [900.0, 1.2350e-05],
    [1000.0, 7.7161e-05],
    [1100.0, 3.1290e-04],
    [1200.0, 8.8539e-04],
    [1300.0, 1.9264e-03],
    [1400.0, 3.4887e-03],
    [1500.0, 5.5619e-03],
    [1600.0, 8.1460e-03],
    [1700.0, 1.1235e-02],
    [1800.0, 1.4857e-02],
    [1900.0, 1.9003e-02],
    [2000.0, 2.3686e-02]
])

# Extract temperature and ke data
temperature_NRL = NRL_data[:, 0]
ke_data_NRL = NRL_data[:, 1]

temperature_DFTB = DFTB_data[:, 0]
ke_data_DFTB = DFTB_data[:, 1]

temperature_KWON = KWON_data[:, 0]
ke_data_KWON = KWON_data[:, 1]

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(temperature_data, ke_data_exp, 'o-', label='Experimental KE Data')
plt.plot(temperature_NRL, ke_data_NRL, 's-', label='NRL KE Data')
plt.plot(temperature_DFTB, ke_data_DFTB, 'd-', label='DFTB KE Data')
plt.plot(temperature_KWON, ke_data_KWON, '^-', label='KWON KE Data')
plt.xlabel('Temperature (K)')
plt.ylabel('K_e (ev/K*ps*ang)')
plt.title('Comparison of electronic conductivity Data')
plt.legend()
plt.grid(True)

# Adjust this to visualize better the axis scale
#plt.ylim(0, 0.0)
plt.show()

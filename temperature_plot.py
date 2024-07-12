import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Define the base path and subdirectory names
base_path = '/home/carlos/Desktop/transfer_local_local/results16'
subdirs = ['sim1', 'sim2', 'sim3', 'sim4', 'sim5', 'sim21', 'sim22', 'sim23', 'sim24', 'sim25']

# Initialize lists to store all time points and temperatures for averaging
all_time_points = []
all_temperatures = []
all_eph_time_points = []
all_T_e = []

# Figure 1: Multiple Temperature Plots
plt.figure(figsize=(10, 6))
for subdir in subdirs:
    file_path = f'{base_path}/{subdir}/thermo.log'
    
    # Load the data
    data = pd.read_csv(file_path, delim_whitespace=True, comment='#', header=0, names=['Step', 'Time', 'Temperature', 'E_kin', 'E_pot', 'Pressure'])
    
    # Append the time points and temperatures to the lists for averaging
    all_time_points.extend(data['Time'])
    all_temperatures.extend(data['Temperature'])
    
    # Plot Temperature vs Time for each subdirectory
    plt.plot(data['Time'], data['Temperature'], marker='o', markersize=0.5, label=subdir)

plt.xlabel('Time')
plt.ylabel('Temperature')
plt.title('Ionic Temperature vs Time for Multiple Simulations')
plt.grid(True)
plt.legend()
plt.show(block=False)  # Non-blocking show

# Data processing for the average temperature plot
# Create a DataFrame from the collected time points and temperatures
df = pd.DataFrame({'Time': all_time_points, 'Temperature': all_temperatures})

# Round the time points to the nearest common timestep (e.g., nearest 0.1 fs)
df['Rounded_Time'] = df['Time'].round(decimals=1)

# Group by the rounded time points and compute the mean temperature
grouped = df.groupby('Rounded_Time').mean()

# Figure 2: Average Temperature Plot
plt.figure(figsize=(10, 6))
plt.plot(grouped.index, grouped['Temperature'], marker='o', markersize=0.5, label='Mean Temperature')
plt.xlabel('Time')
plt.ylabel('Temperature')
plt.title('Average Ionic Temperature vs Time')
plt.grid(True)
plt.legend()
plt.show(block=False)  # Non-blocking show

# Figure 3: Multiple T_e Plots
plt.figure(figsize=(10, 6))
for subdir in subdirs:
    file_path = f'{base_path}/{subdir}/eph-EnergySharingData.txt'
    
    # Load the data
    columns = ["Time (fs)", "E_fric(eV)", "E_rand(eV)", "E_net_cum(eV)", "T_e (K)", "T_a (K)", "Kin.E_a (eV)", "Pot.E_a (eV)"]
    data = pd.read_csv(file_path, delim_whitespace=True, skiprows=1, names=columns)
    
    # Append the time points and T_e to the lists for averaging
    all_eph_time_points.extend(data['Time (fs)'])
    all_T_e.extend(data['T_e (K)'])
    
    # Plot T_e vs Time for each subdirectory
    plt.plot(data['Time (fs)'], data['T_e (K)'], marker='o', markersize=0.5, label=subdir)

plt.xlabel('Time (fs)')
plt.ylabel('T_e (K)')
plt.title('Electronic Temperature vs Time for Multiple Simulations')
plt.grid(True)
plt.legend()
plt.show(block=False)  # Non-blocking show

# Data processing for the average T_e plot
# Create a DataFrame from the collected time points and T_e
df_eph = pd.DataFrame({'Time': all_eph_time_points, 'T_e': all_T_e})

# Round the time points to the nearest common timestep (e.g., nearest 1 fs)
df_eph['Rounded_Time'] = df_eph['Time'].round(decimals=1)

# Group by the rounded time points and compute the mean T_e
grouped_eph = df_eph.groupby('Rounded_Time').mean()

# Figure 4: Average T_e Plot
plt.figure(figsize=(10, 6))
plt.plot(grouped_eph.index, grouped_eph['T_e'], marker='o', markersize=0.5, label='Mean T_e')
plt.xlabel('Time (fs)')
plt.ylabel('T_e (K)')
plt.title('Average Electronic Temperature vs Time')
plt.grid(True)
plt.legend()
plt.show()

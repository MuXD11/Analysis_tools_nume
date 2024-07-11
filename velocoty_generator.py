import numpy as np

# This code  generates random 3D velocity vectors for a given energy

# Constants
energy_eV_100 = 100  # eV
energy_eV_200 = 200  # eV
mass_silicon_kg = 4.6637e-26  # kg

# Conversion factors
eV_to_joules = 1.60218e-19  # 1 eV to Joules
meters_to_angstroms = 1e10  # 1 meter to Angstroms
seconds_to_picoseconds = 1e12  # 1 second to picoseconds

# Function to calculate speed in angstroms per femtosecond
def calculate_speed(energy_eV):
    # Convert energy from eV to Joules
    energy_joules = energy_eV * eV_to_joules
    # Calculate velocity in meters per second using E = 0.5 * m * v^2
    velocity_m_per_s = np.sqrt(2 * energy_joules / mass_silicon_kg)
    # Convert velocity to angstroms per picosecond
    velocity_angstroms_per_ps = velocity_m_per_s * meters_to_angstroms / seconds_to_picoseconds
    # Convert velocity to angstroms per femtosecond
    velocity_angstroms_per_fs = velocity_angstroms_per_ps / 1000
    return velocity_angstroms_per_fs

# Function to generate random 3D vectors with a given magnitude
def generate_random_vector(magnitude):
    vector = np.random.normal(size=3)  # Generate a random vector with normal distribution
    unit_vector = vector / np.linalg.norm(vector)  # Normalize the vector to unit length
    scaled_vector = unit_vector * magnitude  # Scale to the desired magnitude
    return scaled_vector

# Calculate speed for 200 eV
speed_200eV = calculate_speed(energy_eV_200)

# Generate 2 random 3D vectors with the calculated speed
vector1 = generate_random_vector(speed_200eV)
vector2 = generate_random_vector(speed_200eV)

# Ensure the vectors have the correct magnitude
magnitude1 = np.linalg.norm(vector1)
magnitude2 = np.linalg.norm(vector2)

# Print results
print(f"The speed of a silicon atom with 200 eV of kinetic energy is approximately {speed_200eV:.3f} angstroms per femtosecond.")
print(f"Generated Vector 1: {vector1}, Magnitude: {magnitude1:.3f} a/fs")
print(f"Generated Vector 2: {vector2}, Magnitude: {magnitude2:.3f} a/fs")





#Generated Vector 1: [-0.35837679 -0.08568952  0.04050254], Magnitude: 0.371 a/fs
#Generated Vector 2: [-0.32396052 -0.17916864 -0.01911149], Magnitude: 0.371 a/fs

import pandas as pd
#This code transforms NRL, DFTB and other models into a file with the correct format


# Define the file path for the input and output files
input_file_path = '/home/carlos/Desktop/RESEARCH INFO/TEMPERATURE DEPENDENT CONDUCTIVITY HEAT CAPACITY/K_Si_Kwon(paper_data).dat'
output_file_path = '/home/carlos/Desktop/RESEARCH INFO/TEMPERATURE DEPENDENT CONDUCTIVITY HEAT CAPACITY/KWONclear.txt'

# Read the input file
data = pd.read_csv(input_file_path, delim_whitespace=True, header=None)

# Clean the data to remove the first two rows of comments and the header row
data_cleaned = data.drop([0, 1]).reset_index(drop=True)

# Rename columns for clarity
data_cleaned.columns = ['Te', 'kappa_tot', 'kappa_e_ph', 'kappa_e_e', 'mu', 'Ce']

# Convert columns to appropriate data types
data_cleaned = data_cleaned.astype({
    'Te': float,
    'kappa_tot': float,
    'kappa_e_ph': float,
    'kappa_e_e': float,
    'mu': float,
    'Ce': float
})

# Extract required columns
Te = data_cleaned['Te']
Ce = data_cleaned['Ce']
Ke = data_cleaned['kappa_tot']

# Apply the correct conversion factors
Ce_converted = Ce * 6.24e-12  # From J/(m^3*K) to eV/K*ang^3
Ke_converted = Ke * 6.24e-4   # From W/(K*m) to eV/K*ps*ang

# Combine the corrected data
Ce_data = pd.DataFrame({'Te': Te, 'Ce_converted': Ce_converted})
Ke_data = pd.DataFrame({'Te': Te, 'Ke_converted': Ke_converted})

# Define N and M
N = len(Ce_data)
M = len(Ke_data)

# Create the output format with corrected values
output_lines = [
    "# First 3 comment lines",
    "# Te-dependent_e-parameters.txt file",
    "# First N C_e(T_e) with T_e, no line gap, then M K_e(T_e) with T_e",
    f"{N}"
]

# Add Ce data
for _, row in Ce_data.iterrows():
    output_lines.append(f"{row['Te']} {row['Ce_converted']:.4e}")

# Add M line
output_lines.append(f"{M}")

# Add Ke data
for _, row in Ke_data.iterrows():
    output_lines.append(f"{row['Te']} {row['Ke_converted']:.4e}")

# Join the lines into the final output string with corrected values
output_text = "\n".join(output_lines)

# Save to a new file with corrected values
with open(output_file_path, 'w') as f:
    f.write(output_text)

print(f"Output saved to {output_file_path}")

# import ovito
# import numpy as np
# import matplotlib
# matplotlib.use('Agg')  # Use the Agg backend for non-GUI environments
# import matplotlib.pyplot as plt
# from ovito.io import import_file
# from ovito.modifiers import ClusterAnalysisModifier, DeleteSelectedModifier, ExpressionSelectionModifier, WignerSeitzAnalysisModifier, InvertSelectionModifier

# # Define the base path and simulation numbers
# base_path = "/home/carlos/Desktop/NuME_codes_sync/NuME_codes/files_turbogap/results/results15/sim"
# reference_path = "/home/carlos/Desktop/NuME_codes_sync/NuME_codes/files_turbogap/auto1/initial_size10_temp300_potenialgap_200ev.xyz"
# num_sims = 24

# # Initialize lists to store the number of surviving defects and simulation numbers
# surviving_defects = []
# sim_numbers = list(range(1, num_sims + 1))

# for sim_number in sim_numbers:
#     # Import the simulation data
#     file_path = f"{base_path}{sim_number}/trajectory_out.xyz"
#     pipeline = import_file(file_path)

#     # Append modifiers to the pipeline
#     pipeline.reference.load(reference_path)
#     pipeline.modifiers.append(WignerSeitzAnalysisModifier(output_displaced=False, reference=pipeline.source))    
#     pipeline.modifiers.append(ExpressionSelectionModifier(expression='Occupancy > 1 || Occupancy == 0'))
#     pipeline.modifiers.append(InvertSelectionModifier())
#     pipeline.modifiers.append(DeleteSelectedModifier())
#     pipeline.modifiers.append(ClusterAnalysisModifier(cluster_coloring=True, cutoff=3.2, only_selected=False, sort_by_size=True))

#     # Initialize lists to store the number of defects and cumulative time per frame
#     num_defects_per_frame = []
#     time_per_frame = []

#     # Process each frame
#     for frame_ in range(pipeline.source.num_frames):
#         data = pipeline.compute(frame_)
        
#         # Calculate the total number of defects in this frame
#         num_defects = np.sum(data.tables['clusters']['Cluster Size'])
#         num_defects_per_frame.append(num_defects)
        
#         # Get the time associated with this frame
#         time = data.attributes['time']
#         time_per_frame.append(time)

#     # Determine the halfway point in time
#     total_simulation_time = time_per_frame[-1]
#     halfway_time = total_simulation_time / 1.5
    
#     # Find the frame closest to the halfway point
#     halfway_index = (np.abs(np.array(time_per_frame) - halfway_time)).argmin()
    
#     # Store the number of defects at the halfway point
#     surviving_defects.append(num_defects_per_frame[halfway_index])

# # Plot the number of surviving defects for each simulation
# plt.plot(sim_numbers, surviving_defects, marker='o')
# plt.xlabel('Simulation Number')
# plt.ylabel('Number of Surviving Defects')
# plt.title('Surviving Defects')
# plt.grid(True)

# # Save the plot to a file instead of displaying it
# plt.savefig('/home/carlos/Desktop/analysis_tools/surviving_defects_vs_sim_number.png')

# print("Plot saved successfully.")

import ovito
import numpy as np
import matplotlib
matplotlib.use('Agg')  # Use the Agg backend for non-GUI environments
import matplotlib.pyplot as plt
from ovito.io import import_file
from ovito.modifiers import ClusterAnalysisModifier, DeleteSelectedModifier, ExpressionSelectionModifier, WignerSeitzAnalysisModifier, InvertSelectionModifier

# Define the base path and simulation numbers
base_path = "/home/carlos/Desktop/NuME_codes_sync/NuME_codes/files_turbogap/results/results15/sim"
reference_path = "/home/carlos/Desktop/NuME_codes_sync/NuME_codes/files_turbogap/auto1/initial_size10_temp300_potenialgap_200ev.xyz"
num_sims = 24

# Initialize lists to store the number of surviving defects and simulation numbers
surviving_defects = []
sim_numbers = list(range(1, num_sims + 1))

# Load the reference configuration
reference_pipeline = import_file(reference_path)
reference_data = reference_pipeline.compute()

for sim_number in sim_numbers:
    # Import the simulation data
    file_path = f"{base_path}{sim_number}/trajectory_out.xyz"
    pipeline = import_file(file_path)

    # Append modifiers to the pipeline
    wigner_seitz_modifier = WignerSeitzAnalysisModifier(output_displaced=False, reference=reference_pipeline.source)
    pipeline.modifiers.append(wigner_seitz_modifier)
    pipeline.modifiers.append(ExpressionSelectionModifier(expression='Occupancy > 1 || Occupancy == 0'))
    pipeline.modifiers.append(InvertSelectionModifier())
    pipeline.modifiers.append(DeleteSelectedModifier())
    pipeline.modifiers.append(ClusterAnalysisModifier(cluster_coloring=True, cutoff=3.2, only_selected=False, sort_by_size=True))

    # Initialize lists to store the number of defects and cumulative time per frame
    num_defects_per_frame = []
    time_per_frame = []

    # Process each frame
    for frame_ in range(pipeline.source.num_frames):
        data = pipeline.compute(frame_)
        
        # Calculate the total number of defects in this frame
        num_defects = np.sum(data.tables['clusters']['Cluster Size'])
        num_defects_per_frame.append(num_defects)
        
        # Get the time associated with this frame
        time = data.attributes['time']
        time_per_frame.append(time)

    # Determine the halfway point in time
    total_simulation_time = time_per_frame[-1]
    halfway_time = total_simulation_time / 1.5
    
    # Find the frame closest to the halfway point
    halfway_index = (np.abs(np.array(time_per_frame) - halfway_time)).argmin()
    
    # Store the number of defects at the halfway point
    surviving_defects.append(num_defects_per_frame[halfway_index])

# Plot the number of surviving defects for each simulation
plt.plot(sim_numbers, surviving_defects, marker='o')
plt.xlabel('Simulation Number')
plt.ylabel('Number of Surviving Defects')
plt.title('Surviving Defects')
plt.grid(True)

# Save the plot to a file instead of displaying it
plt.savefig('/home/carlos/Desktop/analysis_tools/surviving_defects_vs_sim_number.png')

print("Plot saved successfully.")

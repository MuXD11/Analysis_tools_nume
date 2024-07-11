# import ovito
# import scipy
# import numpy as np
# import matplotlib
# matplotlib.use('Agg')  # Use the Agg backend for non-GUI environments
# import matplotlib.pyplot as plt
# from ovito.io import import_file
# from ovito.modifiers import ClusterAnalysisModifier, DeleteSelectedModifier, ExpressionSelectionModifier, WignerSeitzAnalysisModifier, InvertSelectionModifier

# # Import the simulation data
# pipeline = import_file("/home/carlos/Desktop/NuME_codes_sync/NuME_codes/files_turbogap/results/results13/trajectory_out.xyz")
# #pipeline = import_file("/home/carlos/Desktop/NuME_codes_sync/NuME_codes/files_turbogap/results/results14/sim2/trajectory_out.xyz")

# # Append modifiers to the pipeline
# pipeline.modifiers.append(WignerSeitzAnalysisModifier(output_displaced=False, reference=pipeline.source))
# pipeline.modifiers.append(ExpressionSelectionModifier(expression='Occupancy > 1 || Occupancy == 0'))
# pipeline.modifiers.append(InvertSelectionModifier())
# pipeline.modifiers.append(DeleteSelectedModifier())
# pipeline.modifiers.append(ClusterAnalysisModifier(cluster_coloring=True, cutoff=3.2, only_selected=False, sort_by_size=True))

# # Initialize a list to store the number of defects per frame
# num_defects_per_frame = []

# # Process each frame
# for frame_ in range(pipeline.source.num_frames):
#     data = pipeline.compute(frame_)
    
#     # Calculate the total number of defects in this frame
#     num_defects = np.sum(data.tables['clusters']['Cluster Size'])
#     num_defects_per_frame.append(num_defects)

# # Plot the number of defects per frame
# plt.plot(range(pipeline.source.num_frames), num_defects_per_frame, marker='o')
# plt.xlabel('Frame Number')
# plt.ylabel('Number of Defects')
# plt.title('Number of Defects. TD=false. 2x2x2')
# plt.grid(True)

# # Save the plot to a file instead of displaying it
# plt.savefig('/home/carlos/Desktop/ovito_analysis/defects_2x2x2.png')

# # Print the attributes for the first frame to find the temporal information
# data = pipeline.compute(0)
# print("Available attributes in the data collection:")
# for key, value in data.attributes.items():
#     print(f"{key}: {value}")

############################# ctrl shift p 

##This code takes as input file a ".xyz" trajectory file with simulation steps and performs a defect an cluster analysis.
##Still under development


import ovito
import scipy
import numpy as np
import matplotlib
matplotlib.use('Agg')  # Use the Agg backend for non-GUI environments
import matplotlib.pyplot as plt
from ovito.io import import_file
from ovito.modifiers import ClusterAnalysisModifier, DeleteSelectedModifier, ExpressionSelectionModifier, WignerSeitzAnalysisModifier, InvertSelectionModifier

# Import the simulation data
pipeline = import_file("/home/carlos/Desktop/NuME_codes_sync/NuME_codes/files_turbogap/results/results12/trajectory_out.xyz")

# Append modifiers to the pipeline
pipeline.modifiers.append(WignerSeitzAnalysisModifier(output_displaced=False, reference=pipeline.source))
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
    
    # Debugging output for verification
    print(f"Frame: {frame_}, Time: {time}")

# Verify total simulation time
print(f"Total simulation time: {time_per_frame[-1]} fs")

# Plot the number of defects per frame
plt.plot(time_per_frame, num_defects_per_frame, marker='o')
plt.xlabel('Time (fs)')  # Ensure the unit is correctly labeled
plt.ylabel('Number of Defects')
plt.title('Defects vs time. TD=true. 2x2x2')
plt.grid(True)

# Save the plot to a file instead of displaying it
plt.savefig('/home/carlos/Desktop/ovito_analysis/defects_vs_time_2x2x2.png')

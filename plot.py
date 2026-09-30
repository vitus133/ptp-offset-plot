import numpy as np
import matplotlib
matplotlib.use('Agg') 
import matplotlib.pyplot as plt

raw_te = np.loadtxt("raw_offsets.txt")
filtered_te = np.loadtxt("filtered_offsets.txt")

fs = 16.0 
time_axis = np.arange(len(raw_te)) / fs

plt.figure(figsize=(12, 6))

# Plot raw offsets (thin line, transparent)
plt.plot(time_axis, raw_te, color='lightblue', linewidth=1, label='Raw ptp4l Offsets', alpha=0.5)

plt.plot(time_axis, filtered_te, color='darkblue', marker='.', markersize=3, linewidth=1, label='0.1 Hz Filtered Offsets')

# Add +/- 5ns threshold markers
plt.axhline(y=5, color='red', linestyle='--', linewidth=1.5, label='+5ns Threshold')
plt.axhline(y=-5, color='red', linestyle='--', linewidth=1.5, label='-5ns Threshold')

# ZOOM IN: Force the Y-axis to focus on the area around thresholds.
plt.ylim(-15, 15)

# Format the graph
plt.title('PTP Time Offsets')
plt.xlabel('Observation Time (Seconds)')
plt.ylabel('Time Offset (Nanoseconds)')
plt.grid(True, which='both', linestyle=':', linewidth=0.5)

# Move legend outside the plot
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.tight_layout()

# Save the plot
output_filename = 'ptp_offsets.png'
plt.savefig(output_filename, dpi=300)

print(f"Success: Zoomed plot saved to {output_filename}")

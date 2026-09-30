import numpy as np

def apply_itu_filter(raw_offsets, fs=16.0, fc=0.1):
    dt = 1.0 / fs
    rc = 1.0 / (2 * np.pi * fc)
    alpha = dt / (rc + dt)
    
    filtered = np.zeros_like(raw_offsets, dtype=float)
    filtered[0] = raw_offsets[0]
    
    for i in range(1, len(raw_offsets)):
        filtered[i] = alpha * raw_offsets[i] + (1 - alpha) * filtered[i-1]
        
    return filtered

# Load data, filter, and save
raw_offsets = np.loadtxt("raw_offsets.txt")
filtered_offsets = apply_itu_filter(raw_offsets)
np.savetxt("filtered_offsets.txt", filtered_offsets)

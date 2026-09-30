# PTP Offset Filtering and Visualization Tool

> **DISCLAIMER:** This tool is not a formal noise generation measurement. It is a utility for graphically representing the input noise for comparisons between different lab setups. True ITU-T compliance testing requires an external hardware time analyzer measuring the physical 1PPS output.

## Overview

The `filter.py` utility applies an ITU-T standard 0.1 Hz low-pass filter to the raw 1/16 s spaced ptp4l time offsets. 
The `plot.py` generates a plot to visually identify time error variations against a $\pm 5\text{ ns}$ threshold.

## Prerequisites

* OpenShift CLI (`oc`) authenticated to your cluster.
* Python 3.x environment (a virtual environment `venv` is recommended).
* Required Python packages: `numpy`, `matplotlib`.

## Usage Instructions

### 1. Extract the Raw PTP Data

Fetch the logs from the `linuxptp-daemon` DaemonSet and extract the master offset values into a text file.

```bash
oc -n openshift-ptp -c linuxptp-daemon-container logs ds/linuxptp-daemon | grep "master offset" | awk '{print $5}' > raw_offsets.txt

```

### 2. Apply the 0.1 Hz Filter

Activate your Python virtual environment and run the filtering script. This script processes `raw_offsets.txt` and outputs `filtered_offsets.txt`.

```bash
source venv/bin/activate
python filter.py 

```

### 3. Generate the Plot

Run the plotting script to generate a PNG chart comparing the raw and filtered data.

```bash
python plot.py 

```

## Output

The script generates an image file (e.g., `ptp_offsets.png`) in the current directory. 

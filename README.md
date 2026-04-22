# Lab 3 — Synthetic Sensor Plots

One-sentence description

This repository contains code to generate synthetic temperature sensor data and create publication-quality plots (scatter, histogram, and box plot) for an ECE105 lab.

## Installation

1. Activate the course conda environment:

   conda activate ece105

2. Install dependencies with conda or mamba:

   conda install numpy matplotlib
   # or
   mamba install numpy matplotlib

(If you prefer pip, install into the activated environment: pip install numpy matplotlib)

## Usage

Run the script to generate data and (optionally) save quick diagnostics:

    python generate_plots.py

Or import the module from Python to generate data programmatically:

    from generate_plots import generate_data, plot_scatter
    t, a, b = generate_data()

## Example output

The script / notebook produce three primary plot types saved or displayable:

- Scatter plot: timestamps vs. sensor readings for Sensor A and Sensor B with distinct markers and semi-transparent colors to show overlap.
- Histogram: overlaid histograms of both sensors using shared bins to compare distributions.
- Box plot: side-by-side box plots summarizing the median, quartiles, and outliers for each sensor.

## AI tools used and disclosure

I used Claude.AI by Anthropic to help troubleshoot certain setup issues such as activating mamba and installing certain dependencies. Claude helped me navigate. 

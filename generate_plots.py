"""Generate publication-quality sensor data visualizations.

This script creates synthetic temperature sensor data using NumPy
and produces scatter, histogram, and box plot visualizations saved
as PNG files.

Usage
-----
    python generate_plots.py
"""
# Create a function generate_data(seed) that returns sensor_a, sensor_b,
# and timestamps arrays with the same parameters as in the notebook.
# Use NumPy-style docstring with Parameters and Returns sections.

import numpy as np

def generate_data(seed: int | None = 9064):
    """Generate synthetic temperature sensor data.

    Parameters
    ----------
    seed : int or None, optional
        Seed for NumPy's random number generator. If ``None``, the
        generator is initialized without a fixed seed (non-deterministic).
        Default is 9064 for reproducibility.

    Returns
    -------
    t : numpy.ndarray, shape (200,), dtype float64
        Sorted timestamps uniformly sampled from 0 to 10 seconds.

    sensor_a : numpy.ndarray, shape (200,), dtype float64
        Temperature readings for Sensor A. Generated from a normal
        distribution with mean 25.0 and standard deviation 3.0.

    sensor_b : numpy.ndarray, shape (200,), dtype float64
        Temperature readings for Sensor B. Generated from a normal
        distribution with mean 27.0 and standard deviation 4.5.

    Notes
    -----
    The function uses :func:`numpy.random.default_rng` for a modern,
    reproducible random number generator when a seed is provided.
    """
    rng = np.random.default_rng(seed)

    # timestamps sorted so time-series plots are well-ordered
    t = np.sort(rng.uniform(0.0, 10.0, size=200)).astype(np.float64)

    # sensor readings as Gaussian samples; ensure dtype=float64
    sensor_a = rng.normal(loc=25.0, scale=3.0, size=200).astype(np.float64)
    sensor_b = rng.normal(loc=27.0, scale=4.5, size=200).astype(np.float64)

    return t, sensor_a, sensor_b


def plot_scatter(timestamps, sensor_a, sensor_b, ax) -> None:
    """Draw a scatter plot of two sensors against time on an existing Axes.

    Parameters
    ----------
    timestamps : array-like, shape (n,)
        Time values corresponding to the sensor readings (seconds).

    sensor_a : array-like, shape (n,)
        Temperature readings for Sensor A in degrees Celsius.

    sensor_b : array-like, shape (n,)
        Temperature readings for Sensor B in degrees Celsius.

    ax : matplotlib.axes.Axes
        Axes object to draw the scatter plot on. This function modifies
        the Axes in place and returns ``None``.

    Returns
    -------
    None

    Notes
    -----
    The function uses semi-transparent, distinct markers and colors to
    mirror the notebook's style and calls Axes methods so it works when
    embedding plots into larger figures.
    """
    # Convert inputs to numpy arrays for shape checks and numeric operations
    t = np.asarray(timestamps)
    a = np.asarray(sensor_a)
    b = np.asarray(sensor_b)

    if t.shape != a.shape or a.shape != b.shape:
        raise ValueError("timestamps, sensor_a, and sensor_b must have the same shape")

    # Draw scatter points (styles chosen to match the notebook)
    ax.scatter(t, a, s=40, alpha=0.7, c='tab:blue', marker='o', label='Sensor A')
    ax.scatter(t, b, s=40, alpha=0.7, c='tab:orange', marker='x', label='Sensor B')

    # Labels, legend, grid and title mirror the notebook cell
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Temperature (°C)')
    ax.set_title('Sensor readings (scatter)')
    ax.legend()
    ax.grid(True)


if __name__ == "__main__":
    # quick smoke-test when run as a script
    t, a, b = generate_data(9064)
    print("t.shape:", t.shape, "a.shape:", a.shape, "b.shape:", b.shape)
    print(f"Sensor A mean={a.mean():.2f}, std={a.std():.2f}")
    print(f"Sensor B mean={b.mean():.2f}, std={b.std():.2f}")

# Create plot_scatter(sensor_a, sensor_b, timestamps, ax) that draws
# the scatter plot from the notebook onto the given Axes object.
# NumPy-style docstring. Modifies ax in place, returns None.

def plot_scatter(timestamps, sensor_a, sensor_b, ax) -> None:
    """Draw a scatter plot of two sensors against time on an existing Axes.

    Parameters
    ----------
    timestamps : array-like, shape (n,)
        Time values corresponding to the sensor readings (seconds).

    sensor_a : array-like, shape (n,)
        Temperature readings for Sensor A in degrees Celsius.

    sensor_b : array-like, shape (n,)
        Temperature readings for Sensor B in degrees Celsius.

    ax : matplotlib.axes.Axes
        Axes object to draw the scatter plot on. This function modifies
        the Axes in place and returns ``None``.

    Returns
    -------
    None

    Notes
    -----
    The function uses semi-transparent, distinct markers and colors to
    mirror the notebook's style and calls Axes methods so it works when
    embedding plots into larger figures.
    """
    # Convert inputs to numpy arrays for shape checks and numeric operations
    t = np.asarray(timestamps)
    a = np.asarray(sensor_a)
    b = np.asarray(sensor_b)

    if t.shape != a.shape or a.shape != b.shape:
        raise ValueError("timestamps, sensor_a, and sensor_b must have the same shape")

    # Draw scatter points (styles chosen to match the notebook)
    ax.scatter(t, a, s=40, alpha=0.7, c='tab:blue', marker='o', label='Sensor A')
    ax.scatter(t, b, s=40, alpha=0.7, c='tab:orange', marker='x', label='Sensor B')

    # Labels, legend, grid and title mirror the notebook cell
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Temperature (°C)')
    ax.set_title('Sensor readings (scatter)')
    ax.legend()
    ax.grid(True)

# Create plot_histogram(sensor_a, sensor_b, ax) that draws
# the histogram from the notebook onto the given Axes object.
# NumPy-style docstring. Modifies ax in place, returns None.

def plot_histogram(sensor_a, sensor_b, ax):
    """Draw overlapping histograms of sensor temperature distributions.

    Parameters
    ----------
    sensor_a : numpy.ndarray
        Temperature readings for Sensor A.
    sensor_b : numpy.ndarray
        Temperature readings for Sensor B.
    ax : matplotlib.axes.Axes
        Axes object to plot on.

    Returns
    -------
    None
    """
    import numpy as np
    bins = np.linspace(min(np.min(sensor_a), np.min(sensor_b)),
                       max(np.max(sensor_a), np.max(sensor_b)), 20)
    ax.hist(sensor_a, bins=bins, alpha=0.6, color='tab:blue', label='Sensor A', edgecolor='black')
    ax.hist(sensor_b, bins=bins, alpha=0.6, color='tab:orange', label='Sensor B', edgecolor='black')
    ax.set_xlabel('Temperature (°C)')
    ax.set_ylabel('Count')
    ax.set_title('Histogram of sensor temperatures')
    ax.legend()
    ax.grid(axis='y', alpha=0.6)

# Create plot_boxplot(sensor_a, sensor_b, ax) that draws
# the box plot from the notebook onto the given Axes object.
# NumPy-style docstring. Modifies ax in place, returns None.

def plot_boxplot(sensor_a, sensor_b, ax):
    """Draw a side-by-side box plot comparing sensor distributions.

    Parameters
    ----------
    sensor_a : numpy.ndarray
        Temperature readings for Sensor A.
    sensor_b : numpy.ndarray
        Temperature readings for Sensor B.
    ax : matplotlib.axes.Axes
        Axes object to plot on.

    Returns
    -------
    None
    """
    import numpy as np
    ax.boxplot([sensor_a, sensor_b], labels=['Sensor A', 'Sensor B'])
    ax.set_xlabel('Sensor')
    ax.set_ylabel('Temperature (deg C)')
    ax.set_title('Sensor A vs Sensor B Distribution')
    overall_mean = np.mean(np.concatenate([sensor_a, sensor_b]))
    ax.axhline(overall_mean, color='red', linestyle='--', label=f'Overall mean: {overall_mean:.2f}')
    ax.legend()

# Create main() that generates data, creates a 1x3 subplot figure,
# calls each plot function, adjusts layout, and saves as sensor_analysis.png
# at 150 DPI with tight bounding box.

def main():
    """Generate sensor data and save all three plots as sensor_analysis.png.

    Returns
    -------
    None
    """
    import matplotlib.pyplot as plt
    t, sensor_a, sensor_b = generate_data(9064)
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    plot_scatter(sensor_a, sensor_b, t, axes[0])
    plot_histogram(sensor_a, sensor_b, axes[1])
    plot_boxplot(sensor_a, sensor_b, axes[2])
    plt.tight_layout()
    fig.savefig('sensor_analysis.png', dpi=150, bbox_inches='tight')
    print("Saved sensor_analysis.png")

if __name__ == '__main__':
    main()
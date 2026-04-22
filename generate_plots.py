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


if __name__ == "__main__":
    # quick smoke-test when run as a script
    t, a, b = generate_data(9064)
    print("t.shape:", t.shape, "a.shape:", a.shape, "b.shape:", b.shape)
    print(f"Sensor A mean={a.mean():.2f}, std={a.std():.2f}")
    print(f"Sensor B mean={b.mean():.2f}, std={b.std():.2f}")
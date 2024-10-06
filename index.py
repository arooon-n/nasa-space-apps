import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from astropy.io.votable import parse
import astropy.units as u

# Step 1: Load and parse the VOTable
votable = parse('PSCompPars_2024.10.05_11.20.18.votable')
table = votable.get_first_table().to_table()

# Step 2: Extract relevant data (RA, DEC, distance)
ra = np.array(table['ra'])  # Right Ascension in degrees
dec = np.array(table['dec'])  # Declination in degrees
dist = np.array(table['sy_dist'])  # Distance in parsecs

# Step 3: Convert RA/DEC/Distance to Cartesian coordinates
# Convert degrees to radians
ra_rad = np.deg2rad(ra)
dec_rad = np.deg2rad(dec)

# Calculate the Cartesian coordinates
X = dist * np.cos(ra_rad) * np.cos(dec_rad)
Y = dist * np.sin(ra_rad) * np.cos(dec_rad)
Z = dist * np.sin(dec_rad)

# Step 4: Define a characterization metric (for illustration, based on distance)
# You can replace this with the provided characterization equation
char_metric = 1 / (dist + 1)  # Simple example: inversely proportional to distance

# Step 5: Plot the planetary systems in 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the planetary systems with the color based on characterization metric
scatter = ax.scatter(X, Y, Z, c=char_metric, cmap='viridis', s=10)

# Add color bar
cbar = fig.colorbar(scatter, ax=ax, shrink=0.5, aspect=5)
cbar.set_label('Characterization Metric')

# Labels and title
ax.set_xlabel('X (pc)')
ax.set_ylabel('Y (pc)')
ax.set_zlabel('Z (pc)')
plt.title('3D Visualization of Exoplanets')

plt.show()

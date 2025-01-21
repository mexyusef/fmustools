import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

# Population data
countries = ['India', 'China', 'USA', 'Indonesia', 'Pakistan', 'Nigeria', 'Brazil', 'Bangladesh', 'Russia', 'Mexico']
populations = [1428598765, 1425672868, 339992663, 277529799, 240475940, 223793955, 216419321, 172950908, 144445025, 128453827]

# Create x, y, and z values for the chart
x = np.arange(len(countries)) + 1
jumlah_rank = 2
y = np.arange(1, jumlah_rank)
z = np.zeros((len(y), len(x)))

# Assign population values to the z-axis
for i in range(len(countries)):
    z[:, i] = populations[i]

# Create figure and axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create coordinates for each bar
xpos, ypos = np.meshgrid(x, y)
xpos = xpos.flatten()
ypos = ypos.flatten()
zpos = np.zeros_like(xpos)

# Set the height of each bar
dz = z.flatten()

# Create a color map
cmap = cm.get_cmap('Dark2')

# Create the bars with different colors
ax.bar3d(xpos, ypos, zpos, 0.8, 0.8, dz, color=cmap(dz / dz.max()))

# Set labels and title
ax.set_xlabel('Countries')
ax.set_ylabel('Rank')
ax.set_zlabel('Population')
ax.set_title('Top 10 Countries by Population')

# Set ticks and labels for x-axis
ax.set_xticks(x)
ax.set_xticklabels(countries)

# Show the plot
plt.show()

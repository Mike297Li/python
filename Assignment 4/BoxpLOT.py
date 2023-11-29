import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

# Generate random data for demonstration
data = np.random.randn(100, 4)

# Specify the colors for the boxes
box_colors = ['lightcoral', 'lightskyblue', 'lightgreen', 'lightyellow']

# Create a box plot with custom box colors
box_plot = plt.boxplot(data, labels=['A', 'B', 'C', 'D'], patch_artist=True)

# Customize the box colors
for patch, color in zip(box_plot['boxes'], box_colors):
    patch.set_facecolor(color)

# Create colored rectangles for the legend
legend_patches = [mpatches.Patch(color=color, label=f'Category {i+1}') for i, color in enumerate(box_colors)]

# Add labels to the axes
plt.xlabel('Categories')
plt.ylabel('Values')

# Add a title to the plot
plt.title('Box Plot with Custom Box Colors')

# Add a legend
plt.legend(handles=legend_patches, loc='upper right')

# Display the plot
plt.show()

import matplotlib.pyplot as plt
import numpy as np

# Sample data
categories = ['Category A', 'Category B', 'Category C', 'Category D']
values1 = [30, 50, 25, 40]
values2 = [20, 40, 15, 30]

# Create a grouped bar chart
bar_width = 0.35
index = np.arange(len(categories))

plt.bar(index, values1, width=bar_width, label='Group 1', color='green')
plt.bar(index + bar_width, values2, width=bar_width, label='Group 2', color='lightcoral')

# Add labels to the axes
plt.xlabel('Categories')
plt.ylabel('Values')

# Add a title to the plot
plt.title('Grouped Bar Chart')

# Add a legend
plt.legend()

# Display the plot
plt.show()

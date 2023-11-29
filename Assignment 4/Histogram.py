import matplotlib.pyplot as plt
import numpy as np

# Generate random data for demonstration
data = np.random.randn(1000)

# Create a histogram
plt.hist(data, bins=30, color='green', edgecolor='black')

# Add labels to the axes
plt.xlabel('Values')
plt.ylabel('Frequency')

# Add a title to the plot
plt.title('Histogram')

# Display the plot
plt.show()

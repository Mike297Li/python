import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Create a scatter plot
plt.scatter(x, y, color='green', marker='o', label='Scatter Plot')

# Add labels to the axes
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Add a title to the plot
plt.title('Simple Scatter Plot')

# Add a legend
plt.legend()

# Display the plot
plt.show()

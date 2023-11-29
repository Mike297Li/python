import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Create a line graph
plt.plot(x, y, marker='o', linestyle='-', color='green', label='Line Graph')

# Add labels to the axes
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Add a title to the plot
plt.title('Simple Line Graph')

# Add a legend
plt.legend(loc='upper left')

# Display the plot
plt.show()

import matplotlib.pyplot as plt

# Sample data
categories = ['Category A', 'Category B', 'Category C', 'Category D']
values = [30, 50, 25, 40]

# Create a bar graph
plt.bar(categories, values, color='green')

# Add labels to the axes
plt.xlabel('Different Categories')
plt.ylabel('')  # Conceal the Y-axis label

# Add a title to the plot
plt.title('Modified Bar Graph Title')

# Display the plot
plt.show()

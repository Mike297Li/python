import matplotlib.pyplot as plt

# Sample data
labels = ['Category A', 'Category B', 'Category C', 'Category D']
sizes = [25, 30, 20, 25]

# Create a basic pie chart
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=['lightcoral', 'lightskyblue', 'lightgreen', 'lightyellow'])

# Add a title to the plot
plt.title('Basic Pie Chart')

# Display the plot
plt.show()

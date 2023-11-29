import matplotlib.pyplot as plt

# Sample data
labels = ['Category A', 'Category B', 'Category C', 'Category D']
sizes = [25, 30, 20, 25]
explode = (0.1, 0.2, 0, 0)  # Explode the first slice(Category A) and second (Category B)

# Create an exploded pie chart
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, explode=explode,
        colors=['lightcoral', 'lightskyblue', 'lightgreen', 'lightyellow'])

# Add a title to the plot
plt.title('Exploded Pie Chart')

# Display the plot
plt.show()

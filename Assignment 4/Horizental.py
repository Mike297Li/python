import matplotlib.pyplot as plt
import seaborn as sns  # Seaborn is used for applying themes

# Sample data
categories = ['Category A', 'Category B', 'Category C', 'Category D']
values = [30, 50, 25, 40]

# Set Seaborn theme
sns.set_theme()

# Create a horizontal bar graph
plt.barh(categories, values, color='lightgreen')

# Add labels to the axes
plt.xlabel('Values')
plt.ylabel('Categories')

# Add a title to the plot
plt.title('Horizontal Bar Graph with Custom Theme')

# Display the plot
plt.show()

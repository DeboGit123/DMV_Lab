import matplotlib.pyplot as plt
# Data
categories = ['A', 'B', 'C', 'D']
values = [10, 20, 15, 25]
# Create bar plot
plt.bar(categories, values, color='blue')
# Add labels and title
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Plot Example')
# Show plot
plt.show()
import matplotlib.pyplot as plt

# Get user input for categories
categories = input("Enter categories separated by commas: ").split(',')

# Get user input for values
values = input("Enter corresponding values separated by commas: ").split(',')
values = [float(v) for v in values]  # Convert input strings to numbers

# Create bar plot
plt.bar(categories, values, color='blue')

# Add labels and title
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Plot Example')

# Show plot
plt.show()

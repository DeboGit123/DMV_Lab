import matplotlib.pyplot as plt

n = int(input("Enter the number of values : "))

data = []

for i in range(n):
    data.append(float(input("Enter the values : ")))

plt.hist(data, bins = 10, edgecolor = 'black')
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.title("Histogram")
plt.show()
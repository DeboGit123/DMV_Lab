import matplotlib.pyplot as plt

n = int(input("Enter the number of points : "))

x = []
y = []

print("Enter X Values : ")
for i in range(n) : 
    x.append(int(input()))

print("Enter Y Values : ")
for i in range(n) : 
    y.append(int(input()))

plt.scatter(x, y)
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.title("Scatter Plot")

plt.show()
import matplotlib.pyplot as plt

Category = ["Category 1", "Category 2", "Category 3", "Category 4"]
Values = [12, 16, 18, 56]

plt.bar(Category, Values)

plt.xlabel("Category")
plt.ylabel("Values")
plt.title("Category Vs. Values")
plt.show()

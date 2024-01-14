import matplotlib.pyplot as plt

Category = ["Category 1", "Category 2", "Category 3", "Category 4"]
Values = [12, 16, 18, 56]

plt.pie(Values, labels=Category, autopct="%1.1f%%")
plt.title("Pie Chart")

plt.show()

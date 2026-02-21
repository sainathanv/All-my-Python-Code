import pandas as pd
import matplotlib.pyplot as plt

# Create a DataFrame
data = {
    "Student": ["Alice", "Bob", "Charlie", "David"],
    "Marks": [85, 92, 78, 88]
}

df = pd.DataFrame(data)

# Display DataFrame
print(df)

# Plot using Pandas (internally uses Matplotlib)
plt.figure()
df.plot(kind="bar", x="Student", y="Marks", legend=True, color=["grey", "blue", "green", "yellow"])

plt.xlabel("Student")
plt.ylabel("Marks")
plt.title("Student Marks")

# Show plot
plt.show()
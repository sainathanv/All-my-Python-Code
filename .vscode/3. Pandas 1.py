import pandas as pd 

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Marks": [85, 90, 78],
    "Passed": [True, True, True]
}

df = pd.DataFrame(data)

print("DataFrame:")
print(df)

print("\nAverage Marks:", df["Marks"].mean())
print("Maximum Marks:", df["Marks"].max())

# Filtering
print("\nStudents with marks > 80:")
print(df[df["Marks"] > 80])

# Check Pandas version
print("\nPandas version:", pd.__version__)

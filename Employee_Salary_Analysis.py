import pandas as pd

data = {
    'Name': ['Amit', 'Priya', 'Rahul', 'Sneha'],
    'Department': ['IT', 'HR', 'IT', 'Sales'],
    'Salary': [50000, 40000, 60000, 45000]
}

df = pd.DataFrame(data)

print(df)
print("\nAverage Salary:")
print(df.groupby('Department')['Salary'].mean())

print("\nHighest Paid Employee:")
print(df.loc[df['Salary'].idxmax()])

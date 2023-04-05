import pandas as pd

# Create a sample DataFrame
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

# Define a lambda function to apply to columns 'A' and 'B'
formula = lambda x, y: x + y**2

# Apply the function to create a new column 'C'
df['C'] = df.apply(lambda row: formula(row['A'], row['B']), axis=1)

# Print the modified DataFrame
print(df)
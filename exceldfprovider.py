import pandas as pd

# Load the Excel file into a Pandas DataFrame
df = pd.read_excel('path/to/your/excel/file.xlsx', sheet_name='Sheet1')

# Print the first 5 rows of the DataFrame to verify that it loaded correctly
print(df.head())

import pandas as pd

# Load the Excel file
file_path = 'sale.xlsx'  # Replace with the actual file path
df = pd.read_excel(file_path)
# Convert the "date" column to datetime type
df['date'] = pd.to_datetime(df['date'])

# Group the data by date and sum the "netsale" column
result = df.groupby(df['date'].dt.date)['sale'].sum().reset_index()
print(result)
print(type(result))

# Save the result to a new Excel file
result_file = 'result.xlsx'
result.to_excel(result_file, index=False)

print(f"Sum of 'netsale' for each date has been saved to {result_file}")

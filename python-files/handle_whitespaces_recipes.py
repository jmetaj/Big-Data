import pandas as pd

# Load your CSV data into a Pandas DataFrame
df = pd.read_csv('split_recipe_details.csv')

# Clean the 'name' column by replacing multiple spaces with a single space
df['name'] = df['name'].str.replace(r'\s+', ' ', regex=True)

# Save the cleaned data 
df.to_csv('cleaned_recipe_details.csv', index=False)

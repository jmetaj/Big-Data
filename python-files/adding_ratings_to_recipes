import pandas as pd

# Διαβασε το CSV αρχείο 
df = pd.read_csv('RAW_recipes.csv')

# Διαβασε το CSV αρχείο με τη στήλη "average_rating"
average_ratings_df = pd.read_csv('recipe_ratings_with_average.csv')

# Συνδυασε τα δύο DataFrames βάσει της στήλης "id" (recipe_id)
result_df = df.merge(average_ratings_df, left_on='id', right_on='recipe_id', how='inner')

# Αφαιρεσε την επιπλέον στήλη "recipe_id" και "rating"
result_df = result_df.drop(['recipe_id', 'rating'], axis=1)

# Αποθηκευσε το νέο DataFrame σε ένα άλλο CSV αρχείο
result_df.to_csv('recipes.csv', index=False)

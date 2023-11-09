import pandas as pd

# Διαβασε το CSV αρχείο 
df = pd.read_csv('RAW_interactions.csv')

# Διαβασε το CSV αρχείο 
average_ratings_df = pd.read_csv('recipes.csv')

# Συνδυασε τα δύο DataFrames βάσει της στήλης "id" (recipe_id)
result_df = df.merge(average_ratings_df, left_on='recipe_id', right_on='id', how='inner')

# Αφαιρεσε τισ επιπλέον στήλες 
result_df = result_df.drop(['id','minutes','contributor_id','submitted','tags','nutrition','n_steps','steps','description','ingredients','n_ingredients','user_id', 'average_rating', 'review'], axis=1)

# Αποθηκευσε το νέο DataFrame σε ένα άλλο CSV αρχείο
result_df.to_csv('popular_recipes2.csv', index=False)

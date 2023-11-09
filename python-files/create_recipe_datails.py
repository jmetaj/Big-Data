import pandas as pd

# Διαβασε το αρχείο "recipes_with_categories.csv"
df = pd.read_csv('recipes_with_categories.csv')

# Επελεξε τις στήλες που θελετε να διατηρήσετε
selected_columns = ['name', 'id', 'tags', 'nutrition', 'steps', 'description', 'ingredients', 'average_rating' , 'category']

# Δημιουργησε ένα νέο DataFrame με τις επιλεγμένες στήλες
new_df = df[selected_columns]

# Αποθηκευσε το νέο DataFrame σε ένα νέο CSV αρχείο "recipes_details.csv"
new_df.to_csv('recipe_details.csv', index=False)

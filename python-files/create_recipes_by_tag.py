import pandas as pd

# Διαβασε τα δύο αρχεία
tags_df = pd.read_csv('recipes_with_separate_tags.csv')
recipes_df = pd.read_csv('recipes.csv')

# Συγχώνευση των δύο DataFrames με βάση το πεδίο "id"
merged_df = pd.merge(tags_df, recipes_df, left_on='id', right_on='id', how='inner')

# Επελεξε τις στήλες που θέλετε να διατηρήσετε
selected_columns = ['tag','name', 'submitted', 'average_rating']

# Δημιουργία ενός νέου DataFrame με τις επιλεγμένες στήλες
new_df = merged_df[selected_columns]

# Αποθηκευσε το νέο DataFrame σε ένα νέο CSV αρχείο
new_df.to_csv('recipes_by_tag.csv', index=False)

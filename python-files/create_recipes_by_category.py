import pandas as pd

# Διαβασε το αρχείο "recipes_with_categories.csv"
df = pd.read_csv('recipes_with_categories.csv')

# Επελεξε τις στήλες που θέλετε να διατηρήσετε
selected_columns = ['category','average_rating','id','name']

# Δημιουργησε ένα νέο DataFrame με τις επιλεγμένες στήλες
new_df = df[selected_columns]

# Αποθηκευσε το νέο DataFrame σε ένα νέο CSV αρχείο 
new_df.to_csv('recipes_by_category.csv', index=False)

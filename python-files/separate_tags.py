import pandas as pd

# Διαβασε το αρχείο με τις ταινίες
df = pd.read_csv('recipes.csv')

# Χωρισε τη στήλη "tags" σε ξεχωριστές στήλες με τα tags
df['tags'] = df['tags'].apply(eval)  # Μετατροπή των tags από string σε λίστα

# Δημιουργία ενός DataFrame με τα ξεχωριστά tags
tag_df = df['tags'].apply(pd.Series).stack().reset_index(level=1, drop=True).to_frame('tag')

# Επαναλογισμός του αρχικού DataFrame για να συνδυάσουμε τα tags
df = df.drop('tags', axis=1)
df = df.join(tag_df)

# Επελεξε τις στήλες που θέλετε να διατηρήσετε
selected_columns = ['id', 'tag']

# Αποθηκευσε το νέο DataFrame σε ένα νέο CSV αρχείο
df[selected_columns].to_csv('recipes_with_separate_tags.csv', index=False)

import pandas as pd

# Διαβασε το αρχικό CSV αρχείο
df = pd.read_csv('RAW_interactions.csv')

# Ομαδοποιήσε τις τιμές του "rating" ανά "recipe_id" σε λίστες
grouped = df.groupby('recipe_id')['rating'].apply(list).reset_index()

# Μετατρεψε τη στήλη "rating" σε λίστα με float τιμές
grouped['rating'] = grouped['rating'].apply(lambda x: [float(val) for val in x])

# Αποθηκευσε το DataFrame σε ένα νέο CSV αρχείο
grouped.to_csv('recipe_ratings.csv', index=False)

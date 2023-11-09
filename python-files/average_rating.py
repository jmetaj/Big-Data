import pandas as pd
import ast

# Διαβασε το CSV αρχείο σε ένα DataFrame
df = pd.read_csv('recipe_ratings.csv')

# Ορισε μια στήλη που περιέχει τον μέσο όρο των τιμών της στήλης "ratings" για κάθε γραμμή
df['rating'] = df['rating'].apply(lambda x: ast.literal_eval(x))
df['average_rating'] = df['rating'].apply(lambda x: sum(x) / len(x))

# Αποθηκευσε το DataFrame σε ένα νέο CSV αρχείο
df.to_csv('recipe_ratings_with_average.csv', index=False)
import pandas as pd

# Διαβασε το αρχείο με τις συνταγες
df = pd.read_csv('recipes.csv')

# Υπολογισε το σκορ πλήθος_βημάτων x χρόνος_παρασκευής
df['recipe_score'] = df['n_steps'] * df['minutes']

# Καθορισε τα όρια για τις κατηγορίες
low_category_limit = df['recipe_score'].quantile(0.25)
medium_low_category_limit = df['recipe_score'].quantile(0.5)
medium_high_category_limit = df['recipe_score'].quantile(0.75)

# Ορισε μια συνάρτηση για την κατηγοριοποίηση
def categorize_recipe(row):
    if row['recipe_score'] <= low_category_limit:
        return 'low'
    elif row['recipe_score'] <= medium_low_category_limit:
        return 'medium_low'
    elif row['recipe_score'] <= medium_high_category_limit:
        return 'medium_high'
    else:
        return 'high'

# Δημιουργησε τη στήλη "category" με βάση τη συνάρτηση categorize_recipe
df['category'] = df.apply(categorize_recipe, axis=1)

# Αφαιρεσε την επιπλέον στήλη "recipe_score"
df = df.drop('recipe_score', axis=1)

# Αποθηκεύσε το νέο DataFrame σε ένα νέο CSV αρχείο
df.to_csv('recipes_with_categories.csv', index=False)

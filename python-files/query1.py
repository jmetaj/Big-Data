from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from datetime import datetime

cloud_config= {
  'secure_connect_bundle': 'secure-connect-big-data.zip'
}

auth_provider = PlainTextAuthProvider("SiZbFNHCwZqpLJUKuUzPqqLZ", "aLWCZKsmZDBW9f86gltP6nlcMkR1L8A2Z-Mb8sXYOiZXKMuk,b3d2oCqMiMDoAj4ZO4XtsEubgTMC0cg_hDmvqLPrbLhD21hworKC1_lRPJ758Y-goOOoe1WgP6WFQNB")
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect('big_data')

# Define a dictionary to store total ratings and counts for each recipe
recipe_ratings = {}

# Select all rows from the table
query = "SELECT recipe_id, rating FROM popular_recipes WHERE rating_date >= '2012-01-01' AND rating_date <= '2012-05-31' allow filtering;"
rows = session.execute(query)

#  calculate the total ratings and counts for each recipe
for row in rows:
    recipe_id = row.recipe_id
    rating = row.rating

    if recipe_id in recipe_ratings:
        recipe_ratings[recipe_id]["total"] += rating
        recipe_ratings[recipe_id]["count"] += 1
    else:
        recipe_ratings[recipe_id] = {"total": rating, "count": 1}

# Calculate the average ratings for each recipe
average_ratings = {recipe_id: data["total"] / data["count"] for recipe_id, data in recipe_ratings.items()}

# Sort the recipes by their average ratings and select the top 5
top_5_recipes = sorted(average_ratings.items(), key=lambda x: x[1], reverse=True)[:30]

# Print the top 5 recipes and their average ratings
for recipe_id, avg_rating in top_5_recipes:
    print(f"Recipe ID: {recipe_id}, Average Rating: {avg_rating}")

# Close the Cassandra session and cluster connection
session.shutdown()
cluster.shutdown()
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import pandas as pd
from ast import literal_eval


cloud_config= {
  'secure_connect_bundle': 'secure-connect-big-data.zip'
}

auth_provider = PlainTextAuthProvider("SiZbFNHCwZqpLJUKuUzPqqLZ", "aLWCZKsmZDBW9f86gltP6nlcMkR1L8A2Z-Mb8sXYOiZXKMuk,b3d2oCqMiMDoAj4ZO4XtsEubgTMC0cg_hDmvqLPrbLhD21hworKC1_lRPJ758Y-goOOoe1WgP6WFQNB")
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect('big_data')

insert = session.prepare("INSERT INTO recipe_details(name, id, category, average_rating, tags, nutrition, steps, description, ingredients ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)")

df = pd.read_csv (r'cleaned_recipe_details.csv', encoding="utf-8")
df['tags'] = df['tags'].apply(literal_eval)
df['nutrition'] = df['nutrition'].apply(literal_eval)
df['steps'] = df['steps'].apply(literal_eval)
df['ingredients'] = df['ingredients'].apply(literal_eval)


for index,row in df.iterrows():
        name=str(row[0])
        id=int(row[1])
        category=str(row[8])
        average_rating=float(row[7])
        tags = row[2]
        nutrition = row[3]
        steps = row[4]
        description=str(row[5])
        ingredients = row[6]
        session.execute(insert, [name, id, category, average_rating, tags, nutrition, steps, description, ingredients])


# Close the Cassandra session and cluster connection
session.shutdown()
cluster.shutdown()

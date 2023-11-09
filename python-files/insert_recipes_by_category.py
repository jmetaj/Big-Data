from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import pandas as pd

cloud_config= {
  'secure_connect_bundle': 'secure-connect-big-data.zip'
}

auth_provider = PlainTextAuthProvider("SiZbFNHCwZqpLJUKuUzPqqLZ", "aLWCZKsmZDBW9f86gltP6nlcMkR1L8A2Z-Mb8sXYOiZXKMuk,b3d2oCqMiMDoAj4ZO4XtsEubgTMC0cg_hDmvqLPrbLhD21hworKC1_lRPJ758Y-goOOoe1WgP6WFQNB")
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect('big_data')

insert = session.prepare("INSERT INTO recipes_by_category(category, average_rating, recipe_id, name ) VALUES (?, ?, ?, ?)")

df = pd.read_csv (r'split_recipes_by_category.csv', nrows=10, encoding="utf-8")



for index,row in df.iterrows():
        category=str(row[0])
        average_rating=float(row[1])
        recipe_id=int(row[2])
        name=str(row[3])
        
        session.execute(insert, [category, average_rating, recipe_id, name])


# Close the Cassandra session and cluster connection
session.shutdown()
cluster.shutdown()

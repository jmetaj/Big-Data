from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import pandas as pd
from datetime import datetime

cloud_config= {
  'secure_connect_bundle': 'secure-connect-big-data.zip'
}

auth_provider = PlainTextAuthProvider("SiZbFNHCwZqpLJUKuUzPqqLZ", "aLWCZKsmZDBW9f86gltP6nlcMkR1L8A2Z-Mb8sXYOiZXKMuk,b3d2oCqMiMDoAj4ZO4XtsEubgTMC0cg_hDmvqLPrbLhD21hworKC1_lRPJ758Y-goOOoe1WgP6WFQNB")
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect('big_data')

insert = session.prepare("INSERT INTO popular_recipes(recipe_id, rating_date, rating, name ) VALUES (?, ?, ?, ?)")

df = pd.read_csv (r'split_popular_recipes.csv', encoding="utf-8")



for index,row in df.iterrows():
        recipe_id=int(row[0])
        rating_date = datetime.strptime(row[1], '%Y-%m-%d').date()  
        rating=int(row[2])
        name=str(row[3])
        
        session.execute(insert, [recipe_id, rating_date, rating, name])


# Close the Cassandra session and cluster connection
session.shutdown()
cluster.shutdown()

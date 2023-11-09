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

insert = session.prepare("INSERT INTO recipes_by_tags(tag, name, submitted, average_rating)  VALUES (?, ?, ?, ?)")

df = pd.read_csv (r'split_recipes_by_tag.csv', nrows=100, encoding="utf-8")



for index,row in df.iterrows():
        tag=str(row[0])
        name=str(row[1])
        submitted=datetime.strptime(row[2], '%Y-%m-%d').date()  
        average_rating=float(row[3])
        
        session.execute(insert, [tag, name, submitted, average_rating])


# Close the Cassandra session and cluster connection
session.shutdown()
cluster.shutdown()

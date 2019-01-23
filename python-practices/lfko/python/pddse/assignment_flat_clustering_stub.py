'''
    Created on Jan 23, 2019

    @author: fb
'''
import folium
from matplotlib import colors as mcolors
from sklearn.cluster import MiniBatchKMeans, KMeans

import pandas as pd

# some dark colors without gray/grey
colors = [c for c in list(mcolors.CSS4_COLORS.keys()) if 'dark' in c][6:]

df_is = pd.read_csv('data/mietwohnungen.csv').dropna(subset=['lat', 'lng'], how='any')
# some data cleaning
df_is['lat'] = df_is['lat'].str.strip(",").astype(float)
# print(df_is.shape)

# we'll look at 12 clusters - feel free to change that
n_clusters = 12
"""
    KMeans
"""
kmc = KMeans(n_clusters=n_clusters, max_iter=500, n_init=20)
model = kmc.fit(df_is[['lng', 'lat']])

"""
    MiniBatchKMeans
"""

# batch_size controls the number of randomly selected observations in each batch.
# The larger the the size of the batch, the more computationally costly the training process.
km_is = MiniBatchKMeans(n_clusters=n_clusters, random_state=0, batch_size=100)
# model = km_is.fit(df_is[['lng', 'lat']])
df_is['cluster_assignment'] = model.predict(df_is[['lng', 'lat']])  

print(model)

# the initial map, centered at Beuth
m = folium.Map(location=[52.545195, 13.354670], tiles='Stamen Toner', zoom_start=10)

# add the flats and the cluster centers to the map
for cluster_id in range(n_clusters):
    
    this_cluster_idx = df_is['cluster_assignment'] == cluster_id
    this_cluster_lat_lng = df_is.loc[this_cluster_idx, ['lat', 'lng', 'address', 'zip_region_country']].values
    # this_cluster_addresses = df_is.loc[df_is.loc[this_cluster_idx, ['address']].values
    
    # the markers for the flats
    for lat, lng, addr, zip_region_country in this_cluster_lat_lng:
        folium.CircleMarker(location=[lat, lng], radius=3,
                            fill=True,
                            popup=str(addr + zip_region_country),
                            color=colors[cluster_id], fill_opacity=0.7).add_to(m)
    
    # the marker for the cluster center, 
    # should be visually differentiable from the flat markers
    # maybe by different radius
    folium.CircleMarker(location=[lat, lng], radius=8,
                            fill=False,
                            color=colors[cluster_id], fill_opacity=0.2).add_to(m)

m.save('flat_clusters.html')


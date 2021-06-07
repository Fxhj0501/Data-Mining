import joblib
import numpy
from matplotlib import pyplot  as plt
from sklearn.metrics import accuracy_score
import numpy
import seaborn as sns; sns.set()
from sklearn.datasets import make_blobs
patient_idx_lat_lon = joblib.load('/Users/fengzijian/PycharmProjects/DataMiningHW/DataMining/data/patient_idx_lat_lon.pkl')
del patient_idx_lat_lon['52']
lat_lon_info = numpy.empty([0, 2])
for key, val in patient_idx_lat_lon.items():
    temp_lat_lon = numpy.array(val).reshape(1, 2)
    lat_lon_info = numpy.concatenate((lat_lon_info, temp_lat_lon), axis=0)

plt.scatter(lat_lon_info[:,0], lat_lon_info[:, 1], s=50)
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=4)
kmeans.fit(lat_lon_info)
y_kmeans = kmeans.predict(lat_lon_info)
plt.scatter(lat_lon_info[:, 0], lat_lon_info[:, 1], c=y_kmeans, s=50, cmap='viridis')

centers = kmeans.cluster_centers_

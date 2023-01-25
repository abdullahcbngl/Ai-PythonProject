import random

# Generate lists of 50 random x and y coordinates between 0 and 100
a = [random.randint(0, 100) for _ in range(50)]
b = [random.randint(0, 100) for _ in range(50)]
points = list(zip(a, b))
print(points)
from sklearn.cluster import KMeans

# Initialize the K-Means model with 2 clusters
kmeans = KMeans(n_clusters=2)

# Fit the model to the data
kmeans.fit(points)

# Predict the cluster labels for the data
labels = kmeans.predict(points)
print(labels)
import matplotlib.pyplot as plt

# Create a scatter plot of the points, using the cluster labels as the color
plt.scatter(a, b, c=labels)

# Show the plot
plt.show()
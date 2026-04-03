import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

Border = "-"*70

def StudentClustering():

    print(Border)
    print("Student Performance Clustering using K-Means")
    print(Border)

    # Load dataset
    df = pd.read_csv("student-mat.csv", sep=';')

    # Select required features
    data = df[['G1','G2','G3','studytime','failures','absences']]

    print("Selected Data:")
    print(data.head())

    print(Border)

    # Feature Scaling
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data)

    # Apply K-Means (3 clusters)
    kmeans = KMeans(n_clusters=3, random_state=42)
    clusters = kmeans.fit_predict(scaled_data)

    # Add cluster column
    data['Cluster'] = clusters

    print("Clustered Data:")
    print(data.head())

    print(Border)

    # Visualize (G3 vs Studytime)
    plt.scatter(data['G3'], data['studytime'], c=data['Cluster'])
    plt.xlabel("Final Grade (G3)")
    plt.ylabel("Study Time")
    plt.title("Student Clusters")

    plt.show()

    # Cluster Interpretation
    print("\nCluster Summary:")
    print(data.groupby('Cluster').mean())

def main():
    StudentClustering()

if __name__ == "__main__":
    main()

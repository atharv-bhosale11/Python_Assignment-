import numpy as np
from sklearn.preprocessing import StandardScaler
from scipy.spatial.distance import euclidean

def StandardS():
    data = np.array([
        [25,20000],
        [30,40000],
        [35,80000]
    ])

    point1 = data[0]
    point2 = data[1]

    distance_before = euclidean(point1,point2)

    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data)
    
    scaled_point1 = scaled_data[0]
    scaled_point2 = scaled_data[1]

    distance_after = euclidean(scaled_point1,scaled_point2)

    print("Distnace Before Scaling: ",distance_before)
    print("Distance After Scaling: ",distance_after)

def main():
    StandardS()


if __name__ == "__main__":
    main()

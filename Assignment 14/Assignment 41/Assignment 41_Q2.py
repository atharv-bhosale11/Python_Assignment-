#   [A,B,C,D]
# X [1,2,3,6]
# Y [2,3,1,5]
#   [R,R,B,B]

# Predict(2,2)
import math

def EucDistance(P1,P2):

    Ans = math.sqrt((P1['X'] - P2['X']) **2 + (P1['Y'] - P2['Y'])**2)
    return Ans

def KNN():
    Border = "-"*50
    data = [
            {'point' :'A','X':1,'Y':2,'label':'Red'},
            {'point' :'B','X':2,'Y':3,'label':'Red'},
            {'point' :'C','X':3,'Y':1,'label':'Blue'},
            {'point' :'D','X':6,'Y':5,'label':'Blue'}
            ]
    print(Border)
    print("KNN Algorithm")

    for i in data:
        print(i)
    
    new_point = {'X':2, 'Y' : 2}
    print(data[0])
    print(new_point)

    #Calculate the Distnace

    for d in data:
        d['distance'] = EucDistance(d,new_point)
    print(d)
    print(Border)
    print("Calculted Distances are: ")
    print(Border)

    for d in data:
        print(d)

    sorted_data = sorted(data,key=lambda item : item['distance'])

    print(Border)
    print("Sorted Data")
    print(Border)

    for d in sorted_data:
        print(d)
    
    k = 5
    nearest = sorted_data[:k]

    print(Border)
    print("Neares 3 elements are: ")
    print(Border)

    for d in nearest:
        print(d)

    # Now I'll Do Voting

    votes = {}
    
    for neighbour in nearest:
        label = neighbour['label']
        votes[label] = votes.get(label,0)+1

    print(Border)
    print("Voting Resultes are: ")
    print(Border)

    for d in votes:
        print("Name: ",d,"Number of Votes: ",votes[d])

    print(Border)

    predicted_class = max(votes,key=votes.get)

    print("Predicted Class of 2,2: ",predicted_class)
    print(Border)

def main():
    KNN()

if __name__ =="__main__":
    main()
#prediction changes when K increases Because more neighbors participate in voting.

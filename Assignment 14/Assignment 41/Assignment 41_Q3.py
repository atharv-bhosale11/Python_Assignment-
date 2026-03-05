import math

def EucDistance(P1,P2):
    Ans = math.sqrt((P1['Study Hours'] - P2['Study Hours'])**2 +
                    (P1['Attendance'] - P2['Attendance'])**2)
    return Ans

def KNN():

    Border = "-"*50

    data = [
        {'Study Hours':2,'Attendance':60,'Result':'Fail'},
        {'Study Hours':5,'Attendance':80,'Result':'Pass'},
        {'Study Hours':6,'Attendance':85,'Result':'Pass'},
        {'Study Hours':1,'Attendance':50,'Result':'Fail'}
    ]

    print(Border)
    print("KNN Algorithm")
    print(Border)

    for i in data:
        print(i)

    new_point = {'Study Hours':4,'Attendance':70}

    print(Border)
    print("New Point:",new_point)

    # Calculate Distance

    for d in data:
        d['distance'] = EucDistance(d,new_point)

    print(Border)
    print("Calculated Distances")
    print(Border)

    for d in data:
        print(d)

    sorted_data = sorted(data,key=lambda item:item['distance'])

    print(Border)
    print("Sorted Data")
    print(Border)

    for d in sorted_data:
        print(d)

    k = 3
    nearest = sorted_data[:k]

    print(Border)
    print("Nearest 3 elements")
    print(Border)

    for d in nearest:
        print(d)

    votes = {}

    for neighbour in nearest:
        label = neighbour['Result']
        votes[label] = votes.get(label,0) + 1

    print(Border)
    print("Voting Results")
    print(Border)

    for d in votes:
        print("Name:",d,"Votes:",votes[d])

    predicted_class = max(votes,key=votes.get)

    print(Border)
    print("Predicted Class:",predicted_class)
    print(Border)

def main():
    KNN()

if __name__ == "__main__":
    main()

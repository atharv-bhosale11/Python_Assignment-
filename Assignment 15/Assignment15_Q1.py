square = lambda a : a*a

def main():
    Data = [12,23,34,21,6,9,54,23,22,55]
    print("Actual data is: ",Data)

    MData = list(map(square,Data))
    print("List od Data after square is: ",MData)
    

if __name__=="__main__":
    main()

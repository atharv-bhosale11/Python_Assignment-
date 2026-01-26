import threading

def Even():
    print("Even Numbers: ")
    for i in range(0,21):
        if i%2==0:
            print(i)
    
def odd():
    print("Odd Numbers: ")
    for i in range(0,21):
        if i%2!=0:
            print(i)

def main():
    t1=threading.Thread(target=Even,name="Even")
    t2=threading.Thread(target=odd,name="Odd")
    t1.start()
    t1.join()
    t2.start()
    t2.join()

if __name__=="__main__":
    main()

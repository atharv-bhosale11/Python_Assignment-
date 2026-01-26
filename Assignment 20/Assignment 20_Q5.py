import threading

# Function for Thread1
def thread1_task():
    for i in range(1, 51):
        print(f"Thread1: {i}")

# Function for Thread2
def thread2_task():
    for i in range(50, 0, -1):
        print(f"Thread2: {i}")

# Main function
def main():
    # Create threads
    t1 = threading.Thread(target=thread1_task, name="Thread1")
    t2 = threading.Thread(target=thread2_task, name="Thread2")
    
    # Start Thread1
    t1.start()
    
    # Wait for Thread1 to complete before starting Thread2
    t1.join()
    
    # Start Thread2
    t2.start()
    
    # Wait for Thread2 to finish
    t2.join()

if __name__ == "__main__":
    main()

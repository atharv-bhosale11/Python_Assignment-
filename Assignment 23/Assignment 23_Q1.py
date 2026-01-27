class BookStore:
    NoOfBooks=0

    def __init__(self,Name,Author):
        self.Name = Name
        self.Author = Author

        BookStore.NoOfBooks+=1

    def Display(self):
        print(f"{self.Name} by {self.Author}. No of books: {BookStore.NoOfBooks}")

def main():
    obj1 = BookStore("Python Programing","Guido van Rossum")
    obj1.Display()

    obj2 =BookStore("Let Us C", "Yashavant Kanetkar")
    obj2.Display()

    obj3 = BookStore("Clean Code", "Robert C. Martin")
    obj3.Display()

if __name__=="__main__":
    main()

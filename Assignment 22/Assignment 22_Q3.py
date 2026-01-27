class Arithmetic:
    def __init__(self):
        self.Value1= 0
        self.Value2= 0

    def Accept(self):
            self.Value1= int(input("Enter the Value 1: "))
            self.Value2= int(input("Enter the Value 2: "))

    def Addition(self):
            self.Add = self.Value1+self.Value2
        
    def Substraction(self):
            self.Sub = self.Value1 - self.Value2

    def Muliplication(self):
            self.Mul = self.Value1 * self.Value2

    def Division(self):
            self.Div = self.Value1 / self.Value2
    

    def Display(self):
            print("Addition is: ",self.Add)
            print("Substraction is: ",self.Sub)
            print("Multiplication is: ",self.Mul)
            print("Division is: ",self.Div)
            
obj1 = Arithmetic()
obj2 = Arithmetic()

obj1.Accept()
obj1.Addition()
obj1.Substraction()
obj1.Muliplication()
obj1.Division()
obj1.Display()

obj1.Accept()
obj2.Addition()
obj2.Substraction()
obj2.Muliplication()
obj2.Division()
obj2.Display()
    

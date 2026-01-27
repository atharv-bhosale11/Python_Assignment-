class Circle:
    Pi=3.14 #class variable
    def __init__(self):
        self.Radius=0 #instance variable
        self.Area=0 #instance variable
        self.Circumference=0    #instance variable

    def Accept(self):   #instance method
        self.Radius=float(input("Enter the Radius: "))

    def CalculateArea(self):    #instance method
        self.Area = Circle.Pi*self.Radius*self.Radius
    
    def CalulateCircumference(self):    #instance method
        self.Circumference=2*Circle.Pi*self.Radius

    def Display(self):  #instance method
        print("Value of Radius is: ",self.Radius)
        print("Area of circle is: ",self.Area)
        print("Circumference is: ",self.Circumference)

obj1 = Circle() # creating object

obj1.Accept()
obj1.CalculateArea()
obj1.CalulateCircumference()
obj1.Display()



  


        

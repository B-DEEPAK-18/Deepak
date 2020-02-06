#Defining class object Student
class Studentclass:
        
        #Defining function __init__with parameter self,name,roll_no self is a predefined parameter
        def __init__(
                        self,name,
                        roll_no):
                self.name = name
                self.roll_no = roll_no

        #Defining function display with predefined parameter self to print the content
        def display(self):
                print("Name :",self.name)
                print("roll_no:",self.roll_no)

#Taking string input from user
name=str(input("Enter your name :"))
roll_no=int(input("Enter your roll_no :"))

#Calling function
s1=Studentclass(name,roll_no)
s1.display()

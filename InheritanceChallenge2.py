#Create User class
class User:
    name = "Mark"
    email = "mark@gmail.com"
    password = "1234abcd"
    
    #Define the method of login of the class USER
    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your email: ")
        entry_password = input("Enter your password: ")
        if (entry_email == self.email and entry_password == self.password):
            print("Welcome back, {}".format(self.name))
        else:
            print("You are not authorized for this page.")




#create child class Employee to parent class User 
class Employee(User):
    base_pay = 11.00
    department = "Warehouse"
    pin_number = "3980"
#This is the same method in the parent class "user".
    #the difference is that, instead of using entry_password, we're using entry_pin.

    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your email: ")
        entry_pin = input("Enter your pin: ")
        if (entry_email == self.email and entry_pin == self.pin_number):
            print("Welcome back, {}".format(entry_name))
        else:
            print("You are not authorized for this page.")

#create child class Customer to parent class User
class Customer(User):
    mailing_address = ""
    mailing_list = True


    #Define the method of login of the class USER
    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your email: ")
        entry_password = input("Enter your password: ")
        if (entry_email == self.email and entry_password == self.password):
            print("Welcome back, {}".format(self.name))
        else:
            print("You are not authorized for this page.")

#The following code invokes the methods inside each class for User and employee
user = User()
user.getLoginInfo()

employee = Employee()
employee.getLoginInfo()

customer = Customer()
customer.getLoginInfo()

#Create User class
class User:
    #Define the attributes of the class User
    name = "No Name Provided"
    email = ""
    password = "1234abcd"
    account = 0
#create child class Employee to parent class User 
class Employee(User):
    base_pay = 11.00
    department = ""

#create child class Customer to parent class User
class Customer(User):
    mailing_address = ""
    mailing_list = True



   

#User Greeting Function
#Calling function without parameter
def user_greeting():
    print("Hi there!")
    print("Welcome!")
    
    
user_greeting()

#Calling Function with parameter

def user_greeting(user):
    print("Hi" , user)
    print("Welcome!")
    
    
user_greeting("Maria")

# Function with multiple parameters
def name_age(name, age):  #(name, age) these are positional arguments and their order/position matters.
    print(f"{name} is {age} years old.")
    
    
name_age("Maria" , 23 )

#Keyword Arguments
def person_name(first_name , last_name):
    print(f"Hi {first_name} {last_name}")
    
    
person_name("Maria" , "Farooq")
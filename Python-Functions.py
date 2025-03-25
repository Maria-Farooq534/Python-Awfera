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
    
    
person_name("Maria" , "Farooq") #What if we give "Farooq" as first argument and then "Maria" as 2nd.
person_name("Farooq" , "Maria") #its output is: Hi Farooq Maria .. to avoid this, 
#Use keyword arguments
person_name(last_name="Farooq" ,first_name="Maria") 
# calc_cost(total=50, shipping=5, discount=1)
#In this example , It helps to understand that what actually each value represents.

#If you're using both positional arguments and keywords argument, use positional argument first, 
# otherwise python will raise error.
#person_name(last_name="Farooq" , "Nimra") This will raise syntax error
person_name("Maria" , last_name="Farooq")

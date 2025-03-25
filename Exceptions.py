#Exception is a kind of error that crashes our program.
#We will use try and except to show a proper error msg instead of error in the program and 
# program crash.

'''
result = int(input("Age: ")) #This will return age in integer
print(result , "years old!")

# If we give string as a argument , it will raise error and program will crash
#So, to solve this problem , we will use try and except 

try:
    result = int(input("Age: "))
    print(result , "years old!")
except ValueError:                   #its a value error We will get to know this from output.
    print("Invalid Input")

'''   
# Another error

try :
    user_age = int(input("Age: "))
    income = 20000
    risk = income/user_age
    print("Risk is: " , risk)


except ValueError:
    print("Invalid Value")
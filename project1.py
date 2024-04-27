my_string = input("Enter a string:")
a = len(my_string.strip())
print(f"the sring entered is: {a} characters")

my_string = input("enter a string:  ")
a = len(my_string)

if a < 4:
    print("invalid entry")
else:
    print("valid entry")



a = input("username:  ")
b = input("password:  ")

if a == b == 'admin':
    print("successfully login")
else:
    print("wrong username or password")


zip_code = input("please enter your zipcode:  ")
a = len(zip_code.strip())
b = zip_code.isdigit()
if a == 5 and b == True:
    print("your entry is valid")
else:
    print("please enter a valid zip code")   

email_address = input("enter your email address:  ")
if "@" not in email_address:
    print("invalid email")
else:
    print("valid email")    


int = int(input("enter interger 1:  "))
int2 = int(input("enter integer 2   "))
sum = int1 + int2
print("sum:", sum)


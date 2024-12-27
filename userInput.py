name = input("what is your name?:")
age = int(input("what is your age?:"))
height = float(input("how tall are you?:"))
#reason for typecasting : because str and int or float cannot be treated together  , so you need to typecast

print("hello "+ name)
print("you are " + str(age)+ " years old")  #typecasting because string and int or float cannot be concatinated
print("you are " + str(height)+ " cm's long")
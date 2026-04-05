age = int(input("input your age: "))

if age < 0:
    print("your age isn't a negative number")
elif age <= 12:
    print("You are a kid" )
elif age <= 17:
    print("You are a teen")
elif age <= 64:
    print("You are adult" )
else:
    print("You are old" )




#ask user to enter any expression
expression = input("Enter Python expression like (2+3*4): ")

#evaluate & show result
exec(f"result = {expression}")

#print result
print("The result of ", expression, "is:", result)
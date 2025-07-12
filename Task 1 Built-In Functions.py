#ask the user to enter something
value = input("Enter any value: ")

#by default it will always return string 
print("By Default data type is:", type(value))

#so here we can get exact datype by using this logic if we want to 
if value.isdigit():
#is.didgit checks string chaaracters
#use .replace instead of try except
    converted = int(value)
elif value.replace('.', '', 1).isdigit():
    converted = float(value)
else:
    converted = value  # keep it as string

print("Actual type is:", type(converted))
# Run Python code given as a string
code = input("Enter some Python code to run : ")
try:
        result = eval(code)
        print("Result:", result)
except:
    # If not an expression, try to execute it as a statement
          exec(code) 
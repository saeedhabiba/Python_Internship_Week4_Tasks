import datetime

#ask user to enter birth date
birth_input = input("Enter your birth date (YYYY-MM-DD): ")
#as by default input is str
#convert into datetime object
birth_date = datetime.datetime.strptime(birth_input, "%Y-%m-%d")

#get today's date
today = datetime.datetime.now()

#calculate age in years
age_years = today.year - birth_date.year

#adjust age if birthday havent completed yet 
if (today.month, today.day) < (birth_date.month, birth_date.day):
    age_years -= 1

#calculate total number of days lived
days_lived = (today - birth_date).days


print(f" You are {age_years} years old.")
print(f" You have lived for {days_lived} days.")

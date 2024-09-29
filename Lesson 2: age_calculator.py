first_name = "Mark"
last_name = "Stracener"
current_year = 2024
birth_year = 1995
age = current_year - birth_year

print ("Enter your first name: " +  first_name)
print ("Enter your last name: " + last_name)
print ("Enter the current year: " , current_year)
print ("Enter your birth year: " , birth_year)
print ("Hello " + str(first_name), str(last_name), sep= " ", end="!\n")
print ("You are " + str(age) + " years old this year", end=".\n")
print (f"In the next year, you will be {age + 1} years old", end=".\n")
print ("Completed by, " + str(first_name), str(last_name), sep=" ")

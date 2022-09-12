age = input("What is your current age?")
remage=90 - int(age)
age_months= remage * 12
age_weeks = remage * 52
age_days = remage * 365
test=(f"You have {age_days} days, {age_weeks} weeks, and {age_months} months left.")
print(test)

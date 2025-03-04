def life_in_weeks(age):
  rem = 90 - age
  rem_week = int(rem * 52)
  print(f"You have {rem_week} weeks left.")

#52 weeks in a year
# Call your function with hard coded values
life_in_weeks(12)
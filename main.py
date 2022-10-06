# Created by: Alex James
# Created on: 10/6/2022
# This program determines what kind of movies the user can watch
age = int(input("What is your age?: "))
if age>=17:
  print("You may watch R-Rated movies")
elif age>=13:
  print("You may watch PG-13 movies")
elif age<13:
  print("You may only watch G-rated movies")
  

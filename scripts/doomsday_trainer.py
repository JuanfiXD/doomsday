# Made by JuanfiXD
# I made this script in order to practice python syntax and also learn the doomsday method
# of telling the day of the week a date falls on by following an algorithm
# I did not generate any of the code using AI, I only used AI to remember python syntax and correct myself about Conway's doomsday formula
# This "trainer" script is using the already working and figured out script to generate a random day and promt the user
# to input the day of the week and tell them if they are right or wrong in order to train doomsday mind method

import numpy as np
import time

# define the days of the week in numbers, 0 for sunday, 6 for saturday
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
months = ["","January", "February", "March", "April", "May", "June","July","August","September","October","November","December"]

# Some UI shit
print("-------------------------------------------\nWELCOME TO THE DOOMSDAY TRAINER!\n-------------------------------------------\n")

loop = True

while loop:
    # Mark days in month
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    year = np.random.randint(1000,2201)
    month = np.random.randint(1,13)
    max_day = days_in_month[month]
    day = np.random.randint(1,max_day + 1)

    # Prompt the user with the question
    print(f"\nWhat day of the week was or will be on {months[month]} {day} of {year}?\n")
    start_time = time.time()

    # define century anchor doomsdays
    century_anchors = [2,0,5,3]     # this is the repeating doomsday pattern for centuries look up the doomsday method for more info
    # its just Tuesday, sunday, friday and wednesday respectivelly

    # calculate which century i am in
    century = year // 100           # the first 2 numbers from the year
    year_in_century = year % 100    # get the last 2 numbers from the year

    # calculate the anchor doomsday day for said century from the list and the century with the remainder of 4
    anchor = century_anchors[century % 4]

    # check if the year is a leap year
    is_leap = (year % 4 == 0 and year % 100 !=0) or (year % 400 == 0)

    # doomsday list index 0 is 0 to dont bother
    doomsdays = [0,3,28,14,4,9,6,11,8,5,10,7,12]

    # if it's a leap year the doomsdays change for january and february
    if is_leap:
        doomsdays = [0,4,29,14,4,9,6,11,8,5,10,7,12]

    # select nearest doomsday from list
    near_dd = doomsdays[month]

    # calculate 'distance' to nearest doomsday of the month
    b = day - near_dd

    result = ((anchor + (year_in_century//12) + (year_in_century%12) + ((year_in_century%12)//4))%7 + b) % 7

    text_result = days[result]

    user_answer = input("Please input your answer ----->  ")
    finish_time = time.time() - start_time
    print(f"Time taken: {finish_time:.2f} seconds")

    if text_result == user_answer:
        print("Congratulations! Go for the next one!! \n \n")
    else:
        print("Fucking dumbass the answer was ")
        print(text_result)
    if user_answer == "exit":
        loop = False

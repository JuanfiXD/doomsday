# Made by JuanfiXD
# I made this script in order to practice python syntax and also learn the doomsday method
# Of telling the day of the week a date falls on by following an algorithm
# I did not generate any of the code using AI, I only used AI to remember python syntax and correct myself about Conway's doomsday formula

# idk i just felt like importing a lib but i dont think i needed that shit
import numpy

# define the days of the week in numbers, 0 for sunday, 6 for saturday
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

# Some UI shit
print("-------------------------------------------\nWELCOME TO THE DAY OF THE WEEK CALCULATOR!\n-------------------------------------------\n")

# while loop variables
asking = True
days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# loop in case user inputs date wrong
while asking:
    # Ask for the date
    date = input("Please input the date in the dd/mm/yyyy format ---->  ")
    # Parse the date into the variables
    try:
        parts_of_date = date.split("/")     # return list
        day = int(parts_of_date[0])
        month = int(parts_of_date[1])
        year = int(parts_of_date[2])

        # check if the year is a leap year
        is_leap = (year % 4 == 0 and year % 100 !=0) or (year % 400 == 0)
        # deactivate while loop if its a proper date
        asking = False
    except:
        print("Invalid format, try again")
        asking = True
    if asking == False:
        if is_leap and month == 2:
            max_day = 29
        else:
            try:
                max_day = days_in_month[month]
            except:
                asking = True
    
        if not (1 <= month <= 12) or not (1 <= day <= max_day):
            asking = True
            print("Invalid date, try again")

# Holy fuck the difference between doing user proofing and not is abysmal in line count

# define century anchor doomsdays
century_anchors = [2,0,5,3]     # this is the repeating doomsday pattern for centuries look up the doomsday method for more info
# its just Tuesday, sunday, friday and wednesday respectivelly

# calculate which century i am in
century = year // 100           # the first 2 numbers from the year
year_in_century = year % 100    # get the last 2 numbers from the year

# calculate the anchor doomsday day for said century from the list and the century with the remainder of 4
anchor = century_anchors[century % 4]

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

print(days[result])
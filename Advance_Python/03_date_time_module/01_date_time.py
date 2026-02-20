import datetime

# print("Current date with time", datetime.datetime.now())

# We Create a time object with hr,min,sec,mili-sec
# datetime.time('H','M','S','MS','TZ')
my_time = datetime.time(2,24,10,12)
# print(my_time.minute)
# print(my_time.hour)
# print(my_time)

# it return date with current time
# today_date = datetime.datetime.today()

# it return only date
today_date = datetime.date.today()
# print("Today " , today_date)
# print(today_date.year)
# print(today_date.month)
# print(today_date.day)

specific_date = datetime.date(2025, 12, 25)
# print("Specific date:", specific_date)

# syntax : datetime.time(hour=0, minute=0, second=0, microsecond=0)


t = datetime.time(14, 30, 15)  # 2:30:15 PM
# print("Time:", t)



today = datetime.datetime.today()
tomorrow = today + datetime.timedelta(days=1)
last_week = today - datetime.timedelta(weeks=1)

# print("Today:", today)
# print("Tomorrow:", tomorrow)
# print("Last week:", last_week)

# timedelta(days=1) : return a datetime object 
# basically we use it when we want add 1-day/2-days....and...minus 1-days/2-days/1-week
# we can't less/add in datetime object
# print(datetime.timedelta(days=1))


current_date_time = datetime.datetime.now()

# formatting of date
formatted_str = current_date_time.strftime("%d-%m-%Y %H:%M:%S")
print(formatted_str)

# Parsing : convert string into datetime object
dt_string = "25-12-2025 10:30:00"
parsed_dt = datetime.datetime.strptime(dt_string, "%d-%m-%Y %H:%M:%S")
# print("Parsed datetime:", parsed_dt)
# print(f"Type of dt_str : {type(dt_string)}, Type of parsed_dt : {type(parsed_dt)}")

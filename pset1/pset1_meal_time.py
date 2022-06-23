# https://cs50.harvard.edu/python/2022/psets/1/meal/ ************* Click for the Question! 

def main():
    answer = input("What time is it? ")    # get the time from user
    time = convert(answer)    # call the convert function

    if time >= 7 and time <= 8:  # breakfast betweein hours: 7:00 and 8:00
        print("breakfast time")
    if time >= 12 and time <= 13: # lunch between hours: 12:00 and 13:00
        print("lunch time")
    if time >= 18 and time <= 19: # dinner between hours: 18:00 and 19:00
        print("dinner time")

def convert(time):
    hours, minutes = time.split(":")    # get hour and minute
    new_minute = float(minutes) / 60   # convert time into a float number
    return float(hours) + new_minute   # return the result to main function

if __name__ == "__main__":
    main()
from playsound import playsound
import datetime
import time
invalid = True
while(invalid):
    # Get a valid user input for the alarm time
    print("Set a valid time for the alarm (Ex. 06:30)")
    userInput = input(">> ")
    # For example, this will convert 6:30 to an array of [6, 30].
    alarmTime = [int(n) for n in userInput.split(":")]

    #Validate the time entered to be between 0 and 24 
    # #(hours) or 0 and 60 (minutes)
    if alarmTime[0] >= 24 or alarmTime[0] < 0:
        invalid = True
    
    elif alarmTime[1] >= 60 or alarmTime[1] < 0:
        invalid = True
    else:
        invalid = False
    


# How to Count How Long to Wait Until the Alarm Goes Off
# Number of seconds in an Hour, Minute, and Second
    seconds_hms = [3600, 60, 1] 

# Convert the alarm time to seconds
    alarmSeconds = sum([a*b for a,b in zip(seconds_hms[:len(alarmTime)],alarmTime)])
# Use the datetime.now() function to determine the current time. Convert the current time of day in seconds
    now = datetime.datetime.now()
    currentTimeInSeconds = sum([a*b for a,b in zip(seconds_hms, [now.hour, now.minute, now.second])])

# Calculate the number of seconds until the alarm goes off.
    secondsUntilAlarm = alarmSeconds - currentTimeInSeconds
# If the time different is negative, that means that the alarm needs to be set for the next day.

    if secondsUntilAlarm < 0:secondsUntilAlarm += 86400 

# number of seconds in a day
# Display a message to the user to let them know that the alarm has been successfully set.

    print("Alarm is  set!")
    print("The alarm will ring at %s" % datetime.timedelta(seconds=secondsUntilAlarm))

# Use time.sleep to wait for the amount of seconds required until the alarm needs to go off.

    time.sleep(secondsUntilAlarm)
# Display the "Wake up" message to the user when the alarm goes off.
    print("Ring Ring... time to wake up!")
    playsound('song.mp3')
    
    

    # To add a countdown for each second, use a for loop to print the seconds left to the user.

# Replace the time.sleep line. Add a for loop for each second until the alarm goes off, and display the seconds left to the user.
    for i in range(0, secondsUntilAlarm):
        time.sleep(1)
        secondsUntilAlarm -= 1
        print(datetime.timedelta(seconds=secondsUntilAlarm))

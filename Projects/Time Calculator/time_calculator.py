def add_time(start, duration, dayName=None):

    splitTime = start.split(" ")
    timeCode = splitTime[1]
    clock = splitTime[0].split(":")
    clockHour = clock[0]
    clockMinutes = clock[1]

    plusClock = duration.split(":")
    plusHour = plusClock[0]
    plusMinutes = plusClock[1]

    sumMinutes = int(clockMinutes) + int(plusMinutes)
    tempHour = 0
    while (sumMinutes >= 60):
        tempHour += 1
        sumMinutes -= 60

    sumHours = int(clockHour) + int(plusHour) + tempHour
    tempDay = 0
    while (sumHours >= 12):
        sumHours -= 12
        if (timeCode == "PM"):
            tempDay += 1
            timeCode = "AM"
        else:
            timeCode = "PM"

    if (dayName is not None):
        dayList = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        dayIndex = dayList.index(dayName.title())
        dayIndex = dayIndex + tempDay
        while (dayIndex >= 7):
            dayIndex %= 7
        dayNow = dayList[dayIndex]

    strHour = str(sumHours)
    strMinutes = str(sumMinutes)

    if (strHour == "0"):
        strHour = "12"

    if (len(strMinutes) == 1):
        strMinutes = "0" + strMinutes
    
    returnedString = f"{strHour}:{strMinutes} {timeCode}"

    if (dayName is not None):
        returnedString += f", {dayNow}"

    if (tempDay == 1):
        returnedString += " (next day)"
    elif (tempDay > 1):
        returnedString += f" ({tempDay} days later)"
    
    return returnedString


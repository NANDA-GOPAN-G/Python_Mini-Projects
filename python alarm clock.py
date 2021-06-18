from datetime import datetime
from playsound import playsound

confirm = input("Do you wish to set up an alarm(yes/no)? ").lower()
if confirm == "no":
    quit()

print("Enter the time for the alarm to be set:(HH:MM:SS:PP)")
print("HH -> hour\nMM -> minute\nSS -> seconds\nPP -> pm/am")
alarm_time = input(">> ")

alarm_hour = alarm_time[0:2]
alarm_minute = alarm_time[3:5]
alarm_second = alarm_time[6:8]
alarm_period = alarm_time[9:11].upper()
print("\nSETTING UP ALARM...")

while True:
    now = datetime.now()
    current_hour = now.strftime("%I")
    current_minute = now.strftime("%M")
    current_second = now.strftime("%S")
    current_period = now.strftime("%p")
    if alarm_period == current_period:
        if alarm_hour == current_hour:
            if alarm_minute == current_minute:
                if alarm_second == current_second:
                    print("Wake up!")
                    playsound('C:\Riseandshine\SlowMorning.mp3')
                    break
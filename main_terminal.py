from playsound import playsound
import time

CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[0H"
def alarm(seconds):
    time_elasped = 0
    print(CLEAR)
    while time_elasped < seconds:
        time.sleep(1)
        time_elasped+=1
        time_left = seconds-time_elasped
        minutes_left = time_left//60
        seconds_left = time_left%60

        print(f"{CLEAR_AND_RETURN}Alarm goes off in :{minutes_left:02d}:{seconds_left:02d}")
    playsound("alarm.mp3")

minutes = int(input("Enter the number of minutes"))
seconds = int(input("Enter the number of seconds remaining"))
tot_seconds = minutes*60+seconds
alarm(tot_seconds)

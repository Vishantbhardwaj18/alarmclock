import datetime
import time

def set_alarm(alarm_time):
    """Sets an alarm for the specified time."""
    print(f"Alarm set for {alarm_time.strftime('%H:%M:%S')}.")
    
    while True:
        # Get the current time
        current_time = datetime.datetime.now()
        
        # Check if the current time matches the alarm time
        if current_time.hour == alarm_time.hour and current_time.minute == alarm_time.minute:
            print("Alarm! Time to wake up!")
            break
        
        # Sleep for a while to avoid busy waiting
        time.sleep(1)

def main():
    # Get the alarm time from the user
    alarm_input = input("Set the alarm time (HH:MM:SS): ")
    
    # Parse the input into a datetime object
    try:
        alarm_time = datetime.datetime.strptime(alarm_input, '%H:%M:%S')
    except ValueError:
        print("Invalid time format. Please use HH:MM:SS.")
        return

    # Set the alarm
    set_alarm(alarm_time)

if __name__ == "__main__":
    main()

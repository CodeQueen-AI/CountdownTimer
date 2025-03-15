import time

def countdown_timer():
    print("Welcome to the Countdown Timer!")
    
    # Input: Time in seconds
    try:
        total_seconds = int(input("Enter the countdown time in seconds: "))
    except ValueError:
        print("Please enter a valid number.")
        return
    
    while total_seconds > 0:
        # Calculate minutes and seconds
        minutes, seconds = divmod(total_seconds, 60)
        time_format = f"{minutes:02}:{seconds:02}"
        print(time_format, end="\r")  # Overwrites the line
        time.sleep(1)  # Pause for 1 second
        total_seconds -= 1
    
    print("Time's up! ⏰")

# Run the timer
countdown_timer()


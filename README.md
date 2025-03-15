# 📝 Countdown Timer 
> A simple countdown timer that takes user input (time in seconds) and displays the remaining time in a MM:SS format until the countdown reaches 0

## ⚙️ How It Works
# 1️⃣ User Input
The user enters the countdown time in seconds

The program ensures that the input is a valid number

# 2️⃣ Countdown Process
The given seconds are converted into minutes and seconds using divmod()

The countdown runs inside a while loop

The timer updates every second using time.sleep(1)
# 3️⃣ Displaying Time

The remaining time is displayed in MM:SS format

The end="\r" parameter ensures that the time updates in the same line instead of printing a new line every second

# 4️⃣ Countdown Completion

When the timer reaches 0, the message "Time's up! ⏰" is displayed

# 🔧 Key Functions 

🔹 time.sleep(1) → Pauses the program for 1 second between each update

🔹 divmod(total_seconds, 60) → Converts total seconds into minutes & seconds

🔹 end="\r" → Ensures the output updates on the same line for a smooth countdown effect


### *Code Queen keeps building smart & efficient programs! 🚀* 


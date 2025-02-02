import time
from datetime import datetime
from playsound import playsound

# Function to set an alarm
def set_alarm(alarm_time, sound_file):
    print(f"Alarm set for {alarm_time}. Waiting...")

    while True:
        # Get the current time
        current_time = datetime.now().strftime("%H:%M:%S")
        
        # Check if the current time matches the alarm time
        if current_time == alarm_time:
            print("Wake up! It's time!")
            while True:  # This loop will keep playing the sound
                playsound(sound_file)  # Play the sound
                time.sleep(1)  # Optional: Add a small delay to prevent overwhelming the sound system
        
        # Wait for a second before checking the time again
        time.sleep(1)

if __name__ == "__main__":
    while True:
        alarm_time = ""  # Set this to your desired alarm time
        sound_file = ""  # Make sure this is the correct path
        set_alarm(alarm_time, sound_file)
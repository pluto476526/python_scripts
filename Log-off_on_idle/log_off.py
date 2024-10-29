import keyboard
import mouse
import os
import time
import logging
from datetime import datetime
from plyer import notification


# Settings
TIMEOUT = 60 # Log off after 1 hr of inactivity
REMINDER_TIME = 20 # 5 mins warning before log off
LOCK_SCREEN = False # Set True to lock screen instead of logging off

# Logging config
logging.basicConfig(filename="auto_logoff.txt", level=logging.INFO)


def show_notification():
    """"Display a desktop notification about an upcoming log off"""
    notification.notify(
        title="Log Off Warning",
        message="System will log off in 5 minutes.",
        timeout=10
    )

def check_activity():
    """Monitors system inactivity."""
    last_activity_time = time.time()
    reminder_shown = False

    notification.notify(
        title="Check for Idling",
        message="Script is running in background.",
        timeout=10
    )

    while True:
        # Detect a key press or mouse click
        if keyboard.is_pressed("space") or keyboard.is_pressed("enter") or mouse.is_pressed("left") or mouse.is_pressed("right"):
            last_activity_time = time.time()
            reminder_shown = False # Reset reminder if there is activity

        elapsed_time = time.time() - last_activity_time

        # Show 5 min warning
        if elapsed_time >= TIMEOUT - REMINDER_TIME and not reminder_shown:
            show_notification()
            reminder_shown = True
            logging.info(f"{datetime.now()}: Warning shown.")

        # Log off or lock screen after timeout
        if elapsed_time >= TIMEOUT:
            action = "locking screen" if LOCK_SCREEN else "logging off"
            print(f"No activity detected. {action.capitalize()} system.")
            logging.info(f"{datetime.now()}: No activity. {action.capitalize()} system.")

            if LOCK_SCREEN:
                # Lock screen on Linux machines (using gnome-screensaver)
                # os.system("gnome-screensaver-command -l")

                # Lock screen on windows
                os.system("rundll32.exe user32.dll, LockWorkStation")
            else:
                # Log off on Linux
                # os.system("gnome-session-quit --logout --no-prompt")

                # Log off on windows
                os.system("shutdown -l")
            
            break

        time.sleep(1)

if __name__ == "__main__":
    while True:
        check_activity()

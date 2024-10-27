import time
from plyer import notification

def send_notification() :
    notification.notify(title="Reminder", message="Record any burn sessions!", timeout=60)

def main() :
    while True :
        send_notification()
        time.sleep(10)

if __name__ == "__main__" :
    main()

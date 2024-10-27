from win10toast import ToastNotifier
import time

def send_notification() :
    toaster = ToastNotifier()
    toaster.show_toast("Reminder", "Record your burn sessions!", duration=10)

def main() :
    while True :
        send_notification()
        time.sleep(10)

if __name__ == "__main__" :
    main()

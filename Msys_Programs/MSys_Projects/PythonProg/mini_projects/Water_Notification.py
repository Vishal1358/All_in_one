import time
from plyer import notification

if __name__ == "__main__" :
    while True:
        notification.notify(
            title = "Please drink water",
            message = "Drink daily 3.7Ltr to 7.5Ltr water it's good for health",
            timeout = 2
        )
        time.sleep(6)

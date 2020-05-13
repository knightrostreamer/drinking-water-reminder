import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title = "**Please Drink Water Now !!",
            message = "The National Academies of Sciences, Engineering, and Medicine determined that an adequate daily fluid intake is:About 11.5 cups (2.7 liters) of fluids a day for you",
            app_icon = r"C:\Users\SHALINI MONDAL\Desktop\drinking water\water1.ico",
            timeout=6
        )
        time.sleep(60*60)
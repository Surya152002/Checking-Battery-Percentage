from pynotifier import Notification
import psutil
battery = psutil.sensors_battery()
percent = battery.percent

def check():
    if percent < 99 or percent < 90 :
        Notification("Battery Percentage",str(percent) +"%Percentage Remaining"+ "Un-Plug the Charger",duration=100000).send()

    if percent == 15:
        Notification("Battery Percentage", str(percent) + "%Percentage Remaining" + "Plug In Charger",duration=1000000).send()
        check()
Notification("Battery Percentage",str(percent) +"%Percentage Remaining"+ "Un-Plug the Charger",duration=100000).send()

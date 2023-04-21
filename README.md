# **Battery Percentage Notification Script**
This Python script uses the pynotifier and psutil libraries to notify the user about the battery percentage of their system. When the battery percentage falls below 99 or 90, a notification is displayed to unplug the charger. When the battery percentage reaches 15, a notification is displayed to plug in the charger.

# Dependencies
pynotifier
psutil
#Usage
1. Install the required dependencies using pip install pynotifier psutil
2. Run the script using python battery_notification.py
3. The script will continuously monitor the battery percentage and display notifications when required.

**Note:**
The script needs to be running in the background for it to work. It is recommended to run this script on system startup.

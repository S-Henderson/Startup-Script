"""
By: Scott Henderson
Last Updated: Apr 16, 2020
Purpose: Opens commonly used Windows Apps & URL Links to start workday

"""

import os

import subprocess
import webbrowser

from datetime import datetime

#--------------- ART ---------------


print(r"""
  _________ __                 __                   _________            .__        __    
 /   _____//  |______ ________/  |_ __ ________    /   _____/ ___________|__|______/  |_  
 \_____  \\   __\__  \\_  __ \   __\  |  \____ \   \_____  \_/ ___\_  __ \  \____ \   __\ 
 /        \|  |  / __ \|  | \/|  | |  |  /  |_> >  /        \  \___|  | \/  |  |_> >  |   
/_______  /|__| (____  /__|   |__| |____/|   __/  /_______  /\___  >__|  |__|   __/|__|   
        \/           \/                  |__|             \/     \/         |__|           
""")

#--------------- SETUP ---------------

# List of Windows Apps to open
app_1 = 'C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\OUTLOOK.EXE'
app_2 = 'C:\\Users\\shenderson\\AppData\\Local\\Microsoft\\Teams\\Update.exe --processStart "Teams.exe"'

# List of websites to open
url_1 = "https://login.360incentives.com/360Core/Login.aspx"
url_2 = "https://drive.google.com/drive/folders/0B-VKTqswzwr3MUt3ekJvaHBfb0E"
url_3 = "http://360incentives.freshdesk.com/en/support/login"
url_4 = "https://360insights.atlassian.net/wiki/spaces/CC/pages/806092938/Risk+and+Compliance+RAC"

#--------------- GREETING ---------------

print("Welcome Scotty!")

""" Optional Greeting to Other Users
import getpass
username = getpass.getuser()
print("Welcome", username)
"""

#--------------- DATE STUFF ---------------

# Fun function to display current date & time
def find_datetime():
    """
    This function finds the current date and prints it
    """
    now = datetime.now() # Current Datetime
    
    today = now.strftime("%A - %B %d, %Y") # Date
    print("Today's Date is " + today)
    
    current_time = now.strftime("%I:%M:%S %p") # Time
    print("The Current Time is " + current_time)

find_datetime()

#--------------- OPEN STUFF ---------------

print("*************************")

print("Opening Stuff...")

# Opens Email and Team Chat
def open_apps():
    """
    Opens Windows Apps
    """
    subprocess.Popen(app_1)
    subprocess.Popen(app_2)

open_apps()

# Opens Important Work Links
def open_urls():
    """
    Opens URL Links in Chrome
    """
    webbrowser.open(url_1)
    webbrowser.open_new_tab(url_2)
    webbrowser.open_new_tab(url_3)
    webbrowser.open_new_tab(url_4)

open_urls()

#--------------- ENDING ---------------

print("Script Completed")

print("*************************")

input("Press enter to exit :)")

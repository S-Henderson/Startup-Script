"""
By: Scott Henderson
Last Updated: Apr 22, 2020
Purpose: Opens commonly used Windows Apps & URL Links to start workday
"""

import os

import subprocess
import webbrowser

from datetime import datetime

#--------------- PURPOSE ---------------

print("Purpose: Opens commonly used Windows Apps & URL Links to start workday")

print("*************************")

#--------------- ASCII ART ---------------

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
app_list = ["C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\OUTLOOK.EXE",                         # Outlook Email
            'C:\\Users\\shenderson\\AppData\\Local\\Microsoft\\Teams\\Update.exe --processStart "Teams.exe"'] # Microsoft Teams Chat

# List of websites to open
url_list = ["https://login.360incentives.com/360Core/Login.aspx",                                             # 360core Login
            "https://360in.sharepoint.com/Risk%20&%20Compliance/SitePages/Home.aspx",                         # RAC Attack - Sharepoint
            "http://360incentives.freshdesk.com/en/support/login",                                            # FreshDesk Login
            "https://360insights.atlassian.net/wiki/spaces/CC/pages/806092938/Risk+and+Compliance+RAC",       # RAC Info Page
            "https://360insights.quickbase.com/db/bp6rgphzr",                                                 # QuickBase Report Tracking
            "https://www.youtube.com/"]                                                                       # Youtube           

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
    
    today = now.strftime("%A - %B %d, %Y")        # Date
    print("Today's Date is " + today)
    
    current_time = now.strftime("%I:%M:%S %p")    # Time
    print("The Current Time is " + current_time)

find_datetime()

#--------------- OPEN APPS & LINKS ---------------

print("*************************")

print("Opening Stuff...")

# Opens Email and Team Chat
def open_apps(app_list):
    """
    Open Windows Apps
    """
    for app in app_list:
        subprocess.Popen(app)

open_apps(app_list)

# Opens Important Work Links
def open_urls(url_list):
    """
    Open URL Links in default browser
    """
    for url in url_list:
        webbrowser.open(url, new = 2) # new = 2 means to open in new tab

open_urls(url_list)

#--------------- ENDING ---------------

print("Script Completed")

print("*************************")

print("Have A Great Day! Here Are Some Cats!")

print(r"""
      \`*-.                    
       )  _`-.                 
      .  : `. .                
      : _   "  \               
      ; *` _.   `*-._          
      `-.-"          `-.       
        ;       `       `.     
        :.       .        \    
        . \  .   :   .-"   .   
        "  `+.;  ;  "      :   
        :  "  |    ;       ;-. 
        ; "   : :`-:     _.`* ;
[bug] .*" /  .*" ; .*`- +"  `*" 
     `*-*   `*-*  `*-*"        
""")

print(r"""
          |\___/|
          )     (             .              "
         =\     /=
           )===(       *
          /     \
          |     |
         /       \
         \       /
  _/\_/\_/\__  _/_/\_/\_/\_/\_/\_/\_/\_/\_/\_
  |  |  |  |( (  |  |  |  |  |  |  |  |  |  |
  |  |  |  | ) ) |  |  |  |  |  |  |  |  |  |
  |  |  |  |(_(  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |  |
""")

print(r"""
   /\_/\
   >^.^<.---.
  _"-`-"     )\
 (6--\ |--\ (`.`-.
     --"  --"  ``-"
""")
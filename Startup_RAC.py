"""

  _________ __                 __                
 /   _____//  |______ ________/  |_ __ ________  
 \_____  \\   __\__  \\_  __ \   __\  |  \____ \ 
 /        \|  |  / __ \|  | \/|  | |  |  /  |_> >
/_______  /|__| (____  /__|   |__| |____/|   __/ 
        \/           \/                  |__|    

"""

import os
import webbrowser

desktopPath = os.path.join(os.environ['USERPROFILE'], 'Desktop')

#list of apps to open
app_1 = "slack.exe"
app_2 = "outlook.exe"

#list of websites to open
url_1 = "https://login.360incentives.com/360Core/Login.aspx"
url_2 = "https://drive.google.com/drive/folders/0B-VKTqswzwr3MUt3ekJvaHBfb0E"

print("Opening Stuff...")

#opens apps
os.startfile(app_1)
os.startfile(app_2)

#opens websites - uses default browser
webbrowser.open(url_1)
webbrowser.open_new_tab(url_2)

print("Script Completed")
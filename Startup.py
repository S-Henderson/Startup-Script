import os
import webbrowser

desktopPath = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

#list of apps to open
app_1 = "slack.exe"
app_2 = "outlook.exe"
app_3 = desktopPath + "\Data Management_V5.5.accdb"

#list of websites to open
url_1 = "https://www.youtube.com"
url_2 = "https://360in.sharepoint.com/Operations/POS/Forms/AllItems.aspx"
url_3 = "https://360insights.atlassian.net/projects/POS/queues/custom/243"
url_4 = "https://login.360incentives.com/360Core/Login.aspx"

print("Opening Stuff...")

#opens apps
os.startfile(app_1)
os.startfile(app_2)
os.startfile(app_3)

#opens websites
webbrowser.open(url_1)
webbrowser.open_new_tab(url_2)
webbrowser.open_new_tab(url_3)
webbrowser.open_new_tab(url_4)

print("Script Completed")
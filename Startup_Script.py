import os
import webbrowser

#list of apps to open
app_1 = "outlook.exe"
app_2 = "slack.exe"

#list of websites to open
url_1 = "https://login.360incentives.com/360Core/Login.aspx"
url_2 = "https://360in.sharepoint.com/Operations/POS/Forms/AllItems.aspx"
url_3 = "https://360insights.atlassian.net/projects/POS/queues/custom/243"

#opens apps
os.startfile(app_1)
os.startfile(app_2)

#opens websites
webbrowser.open_new(url_1)
webbrowser.open_new(url_2)
webbrowser.open_new(url_3)

#--------------- SETUP ---------------

# list of websites to open
url_1 = "https://login.360incentives.com/360Core/Login.aspx"
url_2 = "https://drive.google.com/drive/folders/0B-VKTqswzwr3MUt3ekJvaHBfb0E"
url_3 = "http://360incentives.freshdesk.com/en/support/login"
url_4 = "https://360insights.atlassian.net/wiki/spaces/CC/pages/806092938/Risk+and+Compliance+RAC"

#--------------- ACTION ---------------

# opens websites - uses default browser
open_websites <- function() {
  browseURL(url_1)
  browseURL(url_2)
  browseURL(url_3)
  browseURL(url_4)
}

print("Opening Stuff...")

open_websites()

print("Script Completed")

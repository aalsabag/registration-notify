# registration-notify
A python script to notify you when a registration site opens up
This script was designed to send you an email when a page is detected on a registration page. The goal is to keep you from waiting around refreshing a website every 2 seconds.

Requirements:
```
1. python3
2. A running local SMTP server (currently configured to run on port 1025)
```

To execute, you can just run:
```
python check.py -e your_email@email.com -w "https://registrationpage.com"
```
Even if you don't want to setup or use an existing smtp server. It is now configured to make a beeping noise when it detects a change to the registration page.
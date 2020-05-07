import requests
import argparse
import time
import os
import smtplib, ssl
import asyncore
import smtplib
import smtpd
import datetime

def check_page(webpage, email):
    starttime = time.time()
    initial_response = requests.get(webpage)
    while True:
        response = requests.get(webpage)
        contents = response.content
        if response.status_code != 200:
            print("I can't get to the page. The webpage appears to be down!")
        if contents == initial_response:
            continue
        else:
            send_email(webpage = webpage , email = email)
            break
        time.sleep(60.0 - ((time.time() - starttime) % 30.0))

def send_email(webpage ,email):
    fromaddr = "test@domain.org"
    toaddrs  = [email]
    
    # Add the From: and To: headers at the start!
    msg = "Hello, it looks like there was a change to the registration page. It may have opened up"
   

    print("Message length is", len(msg))
    with smtplib.SMTP(host = "localhost", port = 25) as smtp:
        smtp.sendmail(fromaddr, toaddrs, msg)
        smtp.quit()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-w', '--webpage',help="Webpage to check for every 30 seconds. Ex: https://google.com", type = str, required = True)
    parser.add_argument('-e', '--email', help="Email to send notification to. Be sure to check you spam folder. Ex: abc123@gmail.com", required = True)
    arguments = parser.parse_args()

    #send_email(arguments.webpage,arguments.email, arguments.password)
    check_page(webpage = arguments.webpage, email = arguments.email)

if __name__ == '__main__':
    main()
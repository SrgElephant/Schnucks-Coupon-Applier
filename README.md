# Schnucks-Coupon-Applier

  This program automates applying all of the digital coupons to a Schnucks account. Includes opening the web broswer, logging in, clipping coupons, and optionally sending an email with the updated coupon value.
  
  Created with Ubuntu as the OS, and Firefox as the web broswer. Two parts to this project:
  
* Python Setup
  
* CronJob Setup
  
Alternatively, manually visiting the website would be launching the terminal and running
  
  `let btns = document.querySelectorAll(".schnucks-red-bg");`
  
   `btns.forEach(btns => btns.click());`
  
## Python
  
  pip is required to install Selenium as well as the webdriver manager:
  
  `sudo apt update`
  
  `sudo apt install python3-venv python3-pip`
  
  `pip3 install selenium`
  
  `pip3 install webdriver-manager`
  
  To install pip for other operating systems:
  
  https://packaging.python.org/guides/installing-using-linux-tools/
  
  More info on the webdriver-manager:
  
  https://pypi.org/project/webdriver-manager/
  
  
  
  
  This program requires the email and password for a Schnucks account. Replace "SchnucksAcct@gmail.com" and "SchnucksAcctPW" with your Schnucks account info.
  
  `SchnucksAcctEmail     = "SchnucksAcct@gmail.com"`
  
  `SchnucksAcctPassword = "SchnucksAcctPW"`
   
   
   All requirements for Python Setup is complete.
   
   If you would like to send yourself emails, continue. Otherwise go to Cronjob Setup.
   
   
   Set sendEmails to True
   
   `sendEmails = True`
   
   Replace "sender@gmail.com", "senderPW", and "receiver@gmail.com" with your email account info.
   
   Note: https://myaccount.google.com/lesssecureapps Must be on for the sender
   
   `emailAddress  = "sender@gmail.com"`
   
   `emailPassword = "senderPW"`
   
   `emailAddressReceiver = "receiver@gmail.com"`
   
   By default, this program assumes gmail. Replace "smtp.gmail.com" and "465" to match the smtp server of your email provider.
   
   `smtp_server = "smtp.gmail.com"`
   
   `port = 465`
   
## CronJob
  

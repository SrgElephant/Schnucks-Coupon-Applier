# Schnucks-Coupon-Applier

  This program automates applying all of the digital coupons to a Schnucks account. Includes opening the web browser, logging in, clipping coupons, and optionally sending an email with the updated coupon value.
  
  <img src="https://github.com/SrgElephant/Schnucks-Coupon-Applier/blob/main/images/unclipped.png" width="900" height="700">
  
  ![clipped](https://github.com/SrgElephant/Schnucks-Coupon-Applier/blob/main/images/clipped.png)
  
  Created in Ubuntu and with Firefox. Parts to this project:
  
* Python Setup
* Initial Run
* CronJob Setup
  
Alternatively, manually visiting the website would be launching the terminal and running
  
  `let btns = document.querySelectorAll(".schnucks-red-bg");`
  
   `btns.forEach(btns => btns.click());`
  
## Python Setup
  
  pip is required to install Selenium as well as the webdriver manager:
  
  `sudo apt update`
  
  `sudo apt install python3-venv python3-pip`
  
  `pip3 install selenium`
  
  `pip3 install webdriver-manager`
  
  To install pip for other operating systems:
  https://packaging.python.org/guides/installing-using-linux-tools/
  
  More info on the webdriver-manager:
  https://pypi.org/project/webdriver-manager/
  
  Download sca.py to edit the email and password for a Schnucks account. Replace "SchnucksAcct@gmail.com" and "SchnucksAcctPW" with your Schnucks account info.
  
  `SchnucksAcctEmail    = "SchnucksAcct@gmail.com"`
  
  `SchnucksAcctPassword = "SchnucksAcctPW"`
   
   Minimum requirements for Python Setup is complete.
   If you would like to send yourself emails, continue. Otherwise go to Cronjob Setup.
   
   Set sendEmails to True
   
   `sendEmails = True`
   
   Replace "sender@gmail.com", "senderPW", and "receiver@gmail.com" with your email account info. The reciever can be identical to the sender.
   
   `emailAddress  = "sender@gmail.com"`
   
   `emailPassword = "senderPW"`
   
   `emailAddressReceiver = "receiver@gmail.com"`
   
   By default, this program assumes gmail. Replace "smtp.gmail.com" and "465" to match the smtp server of your email provider.
   
   `smtp_server = "smtp.gmail.com"`
   
   `port = 465`
   
   Note: If using Gmail, https://myaccount.google.com/lesssecureapps must be on for the sender.
   
## Initial Run
  
  In the folder with sca.py, open a terminal. Run
  
  `python3 sca.py`
  
  There should be a print statement in the terminal, and possibly an email sent depending on setup. If the script does not work, go back to Python Setup.
  
  ![output](https://github.com/SrgElephant/Schnucks-Coupon-Applier/blob/main/images/output.png)
  
## CronJob Setup
  
  In the terminal, run
  
  `crontab -e`
  
  Select a text editor if prompted.
  
  A website such as https://crontab.guru/ can help format the frequency of how often the script is run. For example, to run the script everyday at 1 am:
  
  __0 1 * * *__
  
  The format of a cronjob is [frequency] [command].
  
  For example, this cronjob runs sca.py everyday @ 1 am and has 2 commands:
  
  `0 1 * * * cd /home/{user}/Documents && /usr/bin/python3 /home/{user}/Documents/sca.py`
  
  Replace both
  
  __/home/{user}/Documents__
  
  with the location of the script. In this example, the sca.py script is located in {user}'s Documents.
  
  Save the cronjob edit.
  
  To view the new cronjob, run
  
  `cronjob -l`
  
  For more info on cronjobs: https://en.wikipedia.org/wiki/Cron

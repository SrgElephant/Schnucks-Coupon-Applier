# Schnucks-Coupon-Applier

  This program automates applying all of the digital coupons to a Schnucks account. Includes encrypting credentials, opening the web browser, logging in, clipping coupons, then optionally sending an email with the updated coupon value or login errors.
  
  <img src="https://github.com/SrgElephant/Schnucks-Coupon-Applier/blob/main/images/unclipped.png" width="300" height="600">
  
  <img src="https://github.com/SrgElephant/Schnucks-Coupon-Applier/blob/main/images/clipped.png" width="300" height="300">
  
  Created in Ubuntu + Firefox. Parts to this project:
  
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
  
  `pip install selenium && pip install webdriver-manager`
  
  Update all python packages:
  
  `pip list --outdated --format=freeze | grep -v '^\-e' | cut -d = -f 1  | xargs -n1 pip install -U`
  
  To install pip for other operating systems:
  
  https://packaging.python.org/guides/installing-using-linux-tools/
  
  More info on the Selenium and webdriver-manager:
  
  https://www.selenium.dev/
  
  https://pypi.org/project/webdriver-manager/
  
  ## Initial Run
  
  Make a new folder called SCA for holding both scaCredentials.py and sca.py. Download both files.
  
  Open the terminal in SCA - where scaCredentials.py and sca.py are located, then type
  
  `python3 scaCredentials.py`
  
  Type in the credentials. These will be encrypted to a text file. If a typo is made, just run the file again.
  
  Note: If using Gmail, https://myaccount.google.com/lesssecureapps must be on for the sender. OAuth is not currently implemented.
  
  Now in the terminal, type
  
  `python3 sca.py`
  
  There should be a print statement like the one shown below, and possibly an email sent depending on setup. If the script does not work, go back to Python Setup.
  
  <img src="https://github.com/SrgElephant/Schnucks-Coupon-Applier/blob/main/images/output.png" width="375" height="125">
  
## CronJob Setup
  
  In the terminal, run
  
  `crontab -e`
  
  Select a text editor if prompted.
  
  A website such as https://crontab.guru/ can help format the frequency of how often the script is run. For example, to run the script everyday at 1 am:
  
  __0 1 * * *__
  
  The format of a cronjob is [frequency] [command(s)].
  
  For example, this cronjob runs sca.py everyday @ 1 am and has 3 commands:
  
  `0 1 * * * cd /home/{user}/Documents/SCA && /usr/bin/python3 /home/{user}/Documents/SCA/sca.py`
  
  Replace both instances of
  
  __/home/{user}/Documents/SCA__
  
  with the location of the script. In this example, the sca.py script is located in {user}'s SCA folder.
  
  Save the cronjob edit.
  
  To view cronjobs, run
  
  `cronjob -l`
  
  For more info on cronjobs:
  
  https://en.wikipedia.org/wiki/Cron

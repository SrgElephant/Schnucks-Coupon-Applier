# Schnucks-Coupon-Applier

  This program automates applying all of the digital coupons to a Schnucks account. Includes encrypting credentials, opening the web browser, logging in, clipping coupons, then optionally sending an email with the updated coupon value or login errors.
  
  <img src="https://github.com/SrgElephant/Schnucks-Coupon-Applier/blob/main/images/unclipped.png" width="300" height="600">
  
  <img src="https://github.com/SrgElephant/Schnucks-Coupon-Applier/blob/main/images/clipped.png" width="300" height="300">
  
  Created in Ubuntu + Chrome. Parts to this project:
  
* Python Setup
* Chrome Setup
* Initial Run
* CronJob Setup
  
Alternatively, manually visiting the website would be launching the browser terminal and running
  
  `let btns = document.querySelectorAll(".schnucks-red-bg");`
  
   `btns.forEach(btns => btns.click());`
  
## Python Setup
  
  pip is required to install Selenium as well as the webdriver manager:
  
  `sudo apt update`
  
  `sudo apt install -y python3-venv python3-pip`
  
  `pip install selenium && pip install webdriver-manager`
  
  Update all python packages:
  
  `pip list --outdated --format=freeze | grep -v '^\-e' | cut -d = -f 1  | xargs -n1 pip install -U`
  
  To install pip for other operating systems:
  
  https://packaging.python.org/guides/installing-using-linux-tools/
  
  More info on the Selenium and webdriver-manager:
  
  https://www.selenium.dev/
  
  https://pypi.org/project/webdriver-manager/
  
  ## Chrome Install
  Skip if you already have Chrome installed. Run two commands:
  
  `wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb`
  
  `sudo dpkg -i google-chrome-stable_current_amd64.deb`
  
  ## Initial Run
  
  Make a new folder called SCA for holding both scaCredentials.py and sca.py. Download both files.
  
  Open the terminal in SCA, where scaCredentials.py and sca.py are located, then type
  
  `python3 scaCredentials.py`
  
  Type in the credentials. These will be encrypted to a text file. If a typo is made, just run the command again.
  
  Note: If using Gmail, https://myaccount.google.com/lesssecureapps must be on for the sender. OAuth is not currently implemented.
  
  Go to https://github.com/settings/tokens and create a token for the webdriver. Paste it in.
  
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
  
  Open the folder, click "Open in Terminal" and use
  
  `pwd` to see the path.
  
  Save the cronjob edit.
  
  To view cronjobs, run
  
  `crontab -l`
  
  For WSL:
  
  `sudo visudo`
  
  add to the bottom
  
  `%sudo ALL=NOPASSWD: /usr/sbin/service cron start`
  
  Go to
  
  C:\Users\{user}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup
  
  Create a shortcut
  
  `C:\Windows\System32\wsl.exe sudo /usr/sbin/service cron start`
  
  Reboot and check
  
  `service cron status`
  
  For more info on cronjobs:
  
  https://en.wikipedia.org/wiki/Cron

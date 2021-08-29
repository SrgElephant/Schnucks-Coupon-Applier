# Schnucks-Coupon-Applier

  This program automates applying all of the digital coupons to a Schnucks account. Includes opening the web broswer, logging in, clipping coupons, and sending an email with the updated coupon value. Created with Ubuntu as the OS. Two parts to this project:

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
  
  More info on the webdriver manager:
  
  https://pypi.org/project/webdriver-manager/
  
## CronJob
  

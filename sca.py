# Version 2.3
# https://github.com/SrgElephant/Schnucks-Coupon-Applier
ver = 2.3
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from cryptography.fernet import Fernet
import time, sys, smtplib
import os

os.environ['GH_TOKEN'] = "paste token here"

# Read key
f0 = open("key.txt","rb")
key = f0.read()
f0.close()
fernet = Fernet(key)

# Read credentials
f1 = open("cred.txt","rb")
lines = f1.read()
f1.close()
lines = fernet.decrypt(lines)
lines = lines.decode()
listLines = lines.split('\n')

SchnucksAcctEmail    = listLines[0]
SchnucksAcctPassword = listLines[1]

sendEmails = False
if len(listLines) > 3:
	sendEmails = True
	emailAddress         = listLines[2]
	emailPassword        = listLines[3]
	emailAddressReceiver = listLines[4]
	smtp_server          = listLines[5]
	port                 = listLines[6]

headerStr   = "Subject: Schnucks Coupon Applier\n"
errorStr    = "\nError occurred while trying to login." \
              "\nPlease make sure Schnucks credentials are correct and the script is up to date." \
              "\nCurrent Version: " + str(ver)
beforeStr   = "\nValue of coupons before: "
appliedStr  = "\nNumber of coupons applied: "
afterStr    = "\nValue of coupons after: "
footnoteStr = "\n\nhttps://github.com/SrgElephant/Schnucks-Coupon-Applier\n"


def get_coupon_total(driver):
    driver.refresh()
    time.sleep(5)
    return driver.find_element(By.CSS_SELECTOR, 'div.link-text').text;


def send_email(send_success_email=False):
    # body contents
    if send_success_email:
        body = headerStr + beforeStr + valueBeforeClicking + appliedStr + numOfUnclippedCoupons + afterStr + valueAfterClicking + footnoteStr

    else:
        body = headerStr + errorStr + footnoteStr

    # determine action
    if sendEmails:
        try:
            server = smtplib.SMTP_SSL(smtp_server, port)
            server.ehlo()
            server.login(emailAddress, emailPassword)
            server.sendmail(emailAddress, emailAddressReceiver, body)
            server.quit()
            print("Email sent to: " + emailAddressReceiver)
        except Exception as e:
            print(e)
            print("\n\nEmail not sent")
    else:
        print("Email info not setup")

    print("Body:\n" + body)


# Start the program
opts = Options()
opts.add_argument('--disable-gpu')
driver = webdriver.Chrome(ChromeDriverManager().install(), options=opts)

# Navigate to login page
driver.get("https://nourish.schnucks.com/web-ext/user/login?redirectUrl=https:%2F%2Fnourish.schnucks.com%2F")

# Wait for the page to load
time.sleep(5);

# Insert Schnucks credentials
driver.find_element(By.ID, 'username').send_keys(SchnucksAcctEmail)
driver.find_element(By.ID, 'password').send_keys(SchnucksAcctPassword)
driver.find_element(By.NAME, 'action').click()

# Wait for the page to load
time.sleep(5);

# Types of errors
try:
    errorLogin = driver.find_element(By.NAME, "login-error")
    errorEmail = driver.find_element(By.NAME, "schnucks-red")
    if len(errorLogin) + len(errorEmail) > 0:
        send_email()
        driver.close()
        sys.exit()
except:
    print("login successful")
# Navigate to the coupons page assuming no errors
driver.get("https://nourish.schnucks.com/web-ext/coupons")

# Wait for the page to load
time.sleep(5);

# Get current value of coupons
valueBeforeClicking = get_coupon_total(driver)

# Find number of unclipped coupons
unclippedCoupons = driver.find_elements(By.CLASS_NAME, 'schnucks-red-bg')
# '- 1' due to the hidden button
numOfUnclippedCoupons = str(len(unclippedCoupons) - 1)

# click buttons and wait for execution to finish
driver.execute_script("let btns = document.querySelectorAll('.schnucks-red-bg');btns.forEach(btns => btns.click())")
time.sleep(5)

# Update the impact of clipping coupons
valueAfterClicking = get_coupon_total(driver)

driver.close()

# Send email of before / after coupon values
send_email(True)

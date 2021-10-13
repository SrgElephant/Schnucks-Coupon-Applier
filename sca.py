# Version 1.91
ver = 1.91
from selenium import webdriver
from selenium.webdriver import FirefoxOptions
from webdriver_manager.firefox import GeckoDriverManager
from cryptography.fernet import Fernet
import time, sys, smtplib

# Read key
f0 = open("key.txt","rb")
key = f0.read()
fernet = Fernet(key)

# Read credentials
f1 = open("cred.txt","rb")
lines = f1.read()
lines = fernet.decrypt(lines)
lines = lines.decode()
listLines = lines.split('\n')
f1.close()

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
    return driver.find_element_by_css_selector("div.link-text").text;


def send_email(send_success_email=False):
    # body contents
    if send_success_email:
        body = headerStr + beforeStr + valueBeforeClicking + appliedStr + numOfUnclippedCoupons + afterStr + valueAfterClicking
    else:
        body = headerStr + errorStr + footnoteStr

    # determine action
    if sendEmails:
        try:
            server = smtplib.SMTP_SSL(smtp_server, port)
            server.ehlo()
            server.login(emailAddress, emailPassword)
            server.sendmail(emailAddress, emailAddressReceiver, (body + footnoteStr))
            server.quit()
            print("Email sent to: " + emailAddressReceiver)
        except Exception as e:
            print(e)
            print("Email not sent")
    else:
        print("Email info not setup")

    print("Body:\n" + body)


# Start the program
options = webdriver.FirefoxOptions()
options.headless = True
driver = webdriver.Firefox(options=options,executable_path=GeckoDriverManager().install())

# Navigate to login page
driver.get("https://nourish.schnucks.com/web-ext/user/login?redirectUrl=https:%2F%2Fnourish.schnucks.com%2F")

# Wait for the page to load
time.sleep(5);

# Insert Schnucks credentials
driver.find_element_by_id('logonId').send_keys(SchnucksAcctEmail)
driver.find_element_by_id('password').send_keys(SchnucksAcctPassword)
driver.find_element_by_class_name('login-button').click()

# Wait for the page to load
time.sleep(5);

# Types of errors
errorLogin = driver.find_elements_by_class_name("login-error")
errorEmail = driver.find_elements_by_class_name("schnucks-red")
if len(errorLogin) + len(errorEmail) > 0:
    send_email()
    driver.close()
    sys.exit()

# Navigate to the coupons page assuming no errors
driver.get("https://nourish.schnucks.com/web-ext/coupons")

# Wait for the page to load
time.sleep(5);

# Get current value of coupons
valueBeforeClicking = get_coupon_total(driver)

# Find number of unclipped coupons
unclippedCoupons = driver.find_elements_by_class_name('schnucks-red-bg')
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

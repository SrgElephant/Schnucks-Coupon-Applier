from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
import time, sys, smtplib, ssl

# TODO provide credentials
SchnucksAcctEmail = "SchnucksAcct@gmail.com"
SchnucksAcctPassword =  "SchnucksAcct"

# OPTIONAL TODO set sendEmails to True if desired; must provide email account details
sendEmails = False
emailAddress = "sender@gmail.com"
emailPassword =  "senderPW"
emailAddressReceiver = "receiver@gmail.com" # can be identical to emailAddress
smtp_server = "smtp.gmail.com:465"

# --- Setup done --- No modifications required after this line ---
headerStr   = "Subject: Schnucks Coupon Applier\n"
errorStr    = "\nError occured while trying to login. Please make sure credentials are correct and the script is up to date."
beforeStr   = "\nValue of coupons before: "
appliedStr  = "\nNumber of coupons applied: "
afterStr    = "\nValue of coupons after: "
footnoteStr = "\n\nhttps://github.com/SrgElephant/Schnucks-Coupon-Applier\n"

def getCouponTotal(driver):
    driver.refresh()
    time.sleep(5)
    return driver.find_element_by_css_selector("div.link-text").text;

def sendEmail(sendSuccessEmail = False):
    if(sendEmails):
        if(sendSuccessEmail):
            body = headerStr + beforeStr + valueBeforeClicking + appliedStr + numOfUnclippedCoupons + afterStr + valueAfterClicking
        else:
            body = headerStr + errorStr
        try:
            server = smtplib.SMTP_SSL(smtp_server)
            server.login(emailAddress, emailPassword)
            server.sendmail(emailAddress, emailAddressReceiver, (body + footnoteStr))
        except Exception as e:
            print(e)
        finally:
            print("Sent\n" + body)
            server.quit()
    else:
        print("Emails not setup")

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

# Navigate to the page and insert Schnucks credentials
driver.get("https://nourish.schnucks.com/web-ext/user/login?redirectUrl=https:%2F%2Fnourish.schnucks.com%2F")
driver.find_element_by_id('logonId').send_keys(SchnucksAcctEmail)
driver.find_element_by_id('password').send_keys(SchnucksAcctPassword)
driver.find_element_by_class_name('login-button').click()

# Wait for the page to load
time.sleep(5);

# Types of errors
errorLogin = driver.find_elements_by_class_name("login-error")
errorEmail = driver.find_elements_by_class_name("schnucks-red")
if (len(errorLogin) + len(errorEmail) > 0):
    sendEmail()
    driver.close()
    sys.exit()

# Navigate to the coupons page assuming no errors
driver.get("https://nourish.schnucks.com/web-ext/coupons")

# Get current value of coupons
valueBeforeClicking = getCouponTotal(driver)

# Find number of unclipped coupons
unclippedCoupons = driver.find_elements_by_class_name('schnucks-red-bg')
# '- 1' due to the hidden button
numOfUnclippedCoupons = str(len(unclippedCoupons) - 1)

# click buttons and wait for execution to finish
driver.execute_script("let btns = document.querySelectorAll('.schnucks-red-bg');btns.forEach(btns => btns.click())")
time.sleep(5)

# Update the impact of the coupons
valueAfterClicking = getCouponTotal(driver)

driver.close()

# Send email of before / after coupon values
sendEmail(True)
